# Week 6

## 2022 Apr 4-8

### Sample Calculations

Five random points at two different pre-selected timestamps were used to test whether the CDO software accurately calculated pre-processing steps as well as anomalies, means and variances. The code used can be found [here](../sample_code/sample_calculations.ipynb). 

The bandpass calculation was not recreated as the process is computationally expensive -- CDO took over two days of CPU time, even with various optimisation procedures.

Deseasonlisation and long-term averages show no discrepancies between the sample calculations and CDO. Neither do the variance and mean height anomalies -- use of CDO module is considered valid.


### Correlation Maps

Correlation between the time series of each index, DMI, SOI, SAMI, ZW3 magnitude and phase, and the variance time series at each latitude/longitude point south of 20S was calculated using normalised anomalies. The result was saved as a NetCDF file so that it could be viewed with Panoply. The files show the spatial distribution of correlations between variance and each index. 

The code used to calculate correlations can be viewed [here](../sample_code/correlation_spatial_patterns.ipynb).

Some show very apparent patterns like the SAM, however most do not have very obvious patterns and the correlations are relatively weak, between 0.1 and 0.2, for SAM it is stronger with a maximum of around 0.3. Figures and descriptions can be found in [Week 7](correlation-maps).
