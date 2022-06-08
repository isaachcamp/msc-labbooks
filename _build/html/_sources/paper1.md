# Title

## Abstract


## Introduction

The seasonal and annual relationship between two fields -- mean height and short-timescale variance -- was investigated, with the variance field considered to be the analogue of storm activity.

# Methodology

_From proposal: European Centre for Medium-Range Weather Forecasts’ ERA5 reanalysis dataset uses historical observations combined with modelling and data assimilation techniques to provide global data. The 500hPa geopotential height field will be analysed at 1°latitude/longitude resolution - higher resolutions being unnecessary since extratropical storm systems are of synoptic scales (1000km)._


For this study, observational data for the 500hPa geopotential height field from the European Centre for Medium-Range Weather Forecasts (ECMWF) Reanalysis, 5th generation (ERA5) {cite}`Hersbach et al., 2020` dataset from 1979-2020. The data was regridded to a 1\degree x 1\degree latitude-longitude grid, which was determined to be adequately to resolve variance in the mean height field due to storms, with storms tending to be on the order of 1000km across -- maximum resolution here is no greater than ~100km. The seasonal cycle was removed from the data by subtracting the smoothed long-term daily mean. To isolate variance due to storm activity, a 2-8 day bandpass filter was applied to daily data in line with Trenberth 1991, the frequency of this band being on the order of the lifetime of an individual storm, whilst retaining maximal variance -- the filter 'turns-off' all variance signals outside that frequency range. The monthly average of the filtered variance anomalies and mean height anomalies were considered.

To examine the relationship between the two fields, Maximum Covariance Analysis (MCA) was used to identify the prominent modes of variation. This was done for the full monthly time series as well as for data grouped seasonally -- and for daily data? Only the first two modes of the full time series were non-degenerate according to the criteria according the North et al. rule of thumb, and seasonally only austral summer possessed any non-degenerate modes, again the first two. However, the following modes were ostensibly ZW3 patterns of various phases so were considered briefly, but should be treated with caution. 

The relationship between storm activity and the atmospheric phenomena was investigated using monthly time series of standard indices. The Southern Oscillation Index (SOI) was used to quantify ENSO, with data collected from NOAA. Empirical Orthogonal Function (EOF) analysis was conducted on the mean height field anomalies and the normalised first principal component was used to define SAM. For ZW3, the index formulated in Goyal et al, 2021 {cite}`goyal_new_2022` was used, with data retrieved from the author. This index defines a ZW3 magnitude and phase from the first and second principal components of 500hPa meridional wind field anomalies, the details of which can be found in the original paper. _The ZW3 index possesses a gamma distribution, such that before any linear statistics could be performed the sample was transformed into a normal distribution._ Correlations and covariance between indices and both mean height and short-timescale variance anomalies were calculated at each grid point, the significance of which was determined using 

- Spearman rank correlation is a non-parametric test and so makes no assumptions of a linear relationship nor about the distribution of a sample, hence why it was used for calculating correlations. It is also more robust to outliers skewing the result.
- Assessment of pros/cons of ERA5

# Results

- 8% of variance in MCA explained by ZW3, in agreement with Goyal et al. 2021 {cite}`goyal_zonal_2021`??


# Discussion

- Goyal finds strong seasonal cycle in phase and amplitude when using meridional winds with the seasonal cycle retained. 
    - 20-40 degrees between winter and other seasons and magnitude shift of 0.6-0.8, peaking in winter.
- Goyal uses CESM2 model of last 1200 years when considering the impact of ZW3 phase to make results more robust, this is the difficulty we have with only 20 data points for 60 degree bins. He also uses 20 degree bins. What impact does this have on our analysis?
- What impact does the linkage between meridional heat transport and ZW3 have on storm tracks?


- Two leading modes, SAM and ZW3
    - A-SAM component completely explains the connection between ENSO and SAM
    - ZW3 pattern driven by anomalous deep convection events in the tropics, e.g. ENSO events. 
    - Hence the two main modes of variation in ENSO can be interpreted as either SAM or ZW3 events.

# Conclusion

