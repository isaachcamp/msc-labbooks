# Indices Calculations


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
