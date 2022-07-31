# Week 22

## 2022 July 25

### Organisation of Storm Track Anomalies by Recurring Low-Frequency Circulation Anomalies {cite}`branstator_organisation_1995`

Branstator (1995) argues that stationary waves (circulation anomalies which he defines from EOF patterns of the 300hPa streamfunction field) steer storm track anomalies and are in turn amplified by those anomalies {cite}`branstator_organisation_1995`, a fact reinforced by the earlier Branstator paper (1992) in which anomalous momentum fluxes were shown to be caused by the same EOF patterns {cite}`branstator_maintenance_1992`. This positive feedback has the effect of preferentially selecting those modes of variability, providing a dynamical advantage over modes that do not excite a positive feedback. This could be an indication of how ZW3 impacts storm track activity, as it is similarly excited in the sub-tropics and propagates poleward. -- Perhaps ZW3 is not one of those modes that excites a posiitve feedback loop, however, why would ZW3 be so prominent in the mean height field in that were the case? It must be something to do with the connection between mean height and variance. 


## 2022 July 26

### Downloading Data for Z500

Data downloaded for 20 models, see [model descriptions](../cmip6_output/model_descriptions.md) for details. 

Issues encountered:

Many of the models did not possess the desired resolution to match the ERA5 dataset (see [model descriptions](../cmip6_output/model_descriptions.md) for details). It was deemed acceptable to interpolate the data to a finer grid of 1 degree lat/lon resolution, as baroclinic storms have a typical scale of O(1000km), much greater than the nominal resolution for all the models selected. Also, Rohrer et al. (2020) {cite}`rohrer_sensitivity_2020` find that Eulerian methods are less sensitive to resolution beyond a threshold in their study on various reanalyses -- _check whether we are beyond this threshold or not_. It is understood that this interpolation does not increase the amount of information contained in these datasets, and interpretation will not go beyond what can fairly be inferred from the model's nominal resolution.

HadGEM3-GC31-MM operates on a 360-day calendar. At the moment the bandpass filter has been applied as usual, and the MCA on the results appears to give a fairly sensible picture. However, the CDO filter was aware of the differing timesteps and this may have caused some errors in the calculation. So far I haven't found an easy way to convert from the 360-day calendar to a noleap calendar.

MPI-ESM-1-2-HAM has missing data for all timesteps at 90S. The missing data has been filled by setting each longitude point at 90S equal to the zonal mean for a given timestep. Applying MCA presents sensible results, the expected picture for both mean and variance.


### Model Indices 

The indices for the phenomena all have to be calculated from the model output, as the real world indices should have no correlation through time with the variables outputted from the models, i.e., SAM or ENSO events should occur at times completely independent of real-world events. 

For this reason, data was downloaded for each model for the Sea Level Pressure (CMIP6 model variable name: psl) to calculate a model equivalent of NOAA's Southern Oscillation Index, as well as data for Meridional Velocity (CMIP6 model variable name: va) to calculate a ZW3 index according to Goyal's method {cite}`goyal_new_2022`.

The indices were derived using CDO commands in bash scripts, saved on Raapoi.

#### SOI Calculation

SOI is calculated as the differences in Mean Sea Level Pressure (MSLP) anomalies between Tahiti and Darwin. MSLP for Tahiti and Darwin must be interpolated for all model outputs as they are sub-grid resolution. These were interpolated using the python module xarray's function "interp", and method "linear" (see bash script on Raapoi for details).

Tahiti lat/lon: -17.6333308, -149.4499982
Darwin lat/lon: -12.46113, 130.84185
Coordinates taken from website: (latitude.to)

Methodology for SOI calculations from NOAA website (https://www.cpc.ncep.noaa.gov/data/indices/Readme.index.shtml#SOICALC), original from Ropelewski & Jones (1987) {cite}`ropelewski_extension_1987`:

"""
How is the SOI Calculated?

Note the anomalies are departures from the 1981-2010 base period.

Standard Deviation Tahiti = SQRT( SUMMATION(1) / N )

SUMMATION(1) - is the sum of all ((TA) ** 2)
TA - Tahiti anomaly = (actual(SLP) - mean(SLP))
N - number of months

So, Standardized Tahiti = (Actual Tahiti (SLP) - Mean Tahiti (SLP))
                                                  Standard Deviation Tahiti

Standard Deviation Darwin = SQRT( SUMMATION(1) / N )

SUMMATION(1) - is the sum of all ((DA) ** 2)
DA - Darwin anomaly = (actual(SLP) - mean(SLP))
N - number of months

So, Standardized Darwin = (Actual Darwin (SLP) - Mean Darwin (SLP))
                                                     Standard Deviation Darwin

To calculate the monthly standard deviation:

Monthly Standard Deviation (MSD) = SQRT( SUMMATION(3) / N)

SUMMATION(3) - is the sum of ((Standardized Tahiti - Standardized Darwin) ** 2)
N - total number of summed months

The SOI equation looks as follows: SOI = (Standardized Tahiti - Standardized Darwin) / MSD

"""

##### SOI Index

For the SOI index calculated for ACCESS-CM2, the spread of the values is not as large. The maximum and minimum values are smaller by around one unit, which could be significant. This might be somethign to look into, perhaps by calculating the variance or something similar. The indices are standardised so they should have unit variance, but there may be another statistic that explores the frequency of extreme values. This may be relevant for other indices as well.

#### ZW3 Calculations

To calculate a ZW3 index, Goyal and his fellow authors apply an EOF analysis to the meridional wind anomalies between 40-70S. They then use the first and second EOFs to calculate a magnitude and phase of ZW3.

ZW3 Magnitude:

```{math}
  \begin{equation}
    |ZW3| = \sqrt{PC1^2 + PC2^2}
  \end{equation}
```

ZW3 Phase:

```{math}
  \begin{equation}
    ZW3 Phase = tan^{-1}\frac{PC2}{PC1}
  \end{equation}
```

Issues encountered:

Goyal et al. 2022 {cite}`goyal_new_2022` find two of the models that we have selected to be incompatible with the definition of the index, as either or both of the leading two EOFs are actually ZW4 or some other pattern not connected to ZW3. Those models are:

- FGOALS-f3-L
- GFDL-CM4

These will be checked anyway, along with the other models to ensure that the EOFs are directly related to ZW3 before calculating the index.

