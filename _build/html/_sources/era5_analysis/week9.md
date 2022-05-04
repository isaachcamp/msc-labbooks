# Week 9

## 2022 Apr 25-29

(correlation-maps)=
### Updated Correlation & Covariance Maps

ERA5 data for the mean anomalies and the 2-8 day bandpassed variance anomalies of the 500hPa geopotential height field were correlated with the monthly time series of standard indices for the four phenomena being considered. 

```{note}
See [week 3](indices-source) for where the indices were sourced from, and [week 4](index-processing) for how these indices were formatted. 
```

The analysis was performed by first aggregating the ERA5 data into a monthly time series in line with the index time series, and trimmed to the region south of 20S -- this was done using CDO software. At each longitude-latitude grid point, the mean and variance time series were correlated with the index time series, and the covariance of the two time series was calculated in the same manner. This was done with both Pearson product-moment and Spearman rank methods -- in future, the rank method is preferred as it is more robust and resistant to outliers skewing the result. 

The same method was applied to ERA5 data grouped seasonally. This left a reduced time series which was correlated with the corresponding time stamps from each index. This enables seasonal effects and connections to be inspected.

The code used to calculating correlations and covariance can be found [here](../sample_code/corr_cov_maps.ipynb).

The resulting matrices were plotted using the cartopy library in Python: two subplots of mean height anomalies and variance, side-by-side, using an Orthographic projection for a clearer picture of the 20S to 90S region.

The code used to create these figures can be found [here](../sample_code/create_maps.ipynb).

The correlation and covariance figures are discussed in detail in [week 10](./week10.md) notes.
