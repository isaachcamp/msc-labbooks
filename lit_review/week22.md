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

The data, once filtered, is averaged to monthly data, such that the number of data points is the same between models. When taking mean values, the CDO command "yearmonmean" weights each month by the number of days contained within that month, so that it becomes irrelevant. Use this command in combination with "timmean" to find the true mean of the time series. However, if CDO doesn't know that these are actually thirty day months, it will assume that it contains the usual number of days. Therefore, just use the "timmean" command for HadGEM3.

MPI-ESM-1-2-HAM has missing data for all timesteps at 90S. The missing data has been filled by setting each longitude point at 90S equal to the zonal mean for a given timestep. Applying MCA presents sensible results, the expected picture for both mean and variance.

