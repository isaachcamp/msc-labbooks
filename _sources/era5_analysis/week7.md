# Week 7

## 2022 Apr 11-15

```{warning}
These maps are out of date as the wrong dataset was used for mean height anomalies. They have been redone and a description can be found in the [Week 10](week10.md) notebook.
```

(correlation-maps)=
### Correlation Maps

The following sections detail the correlation maps of each index, except [ZW3](ZW3-correlations), with mean height field and variance anomalies. Both Pearson and Spearman rank correlations were used, rank being more robust, however very little difference can be seen between the two methods.


#### Correlations of Mean Height Field Anomalies

Correlations were also calculated between mean height anomalies and indices, for side-by-side figures. It is apparent that they show much weaker correlations.


#### SAM Correlations

For the variance anomalies, a clear annular structure can be seen with negative correlations centred around 60S and positive correlations centred around 40S, a very SAM-like structure. This means that when the SAM index is negative, there tends on average to be more storms (more bandpass variance, at least) over the southern ocean centred at ~60S and fewer storms in mid-latitudes, centred around 40S. This is the precisely how the SAM operates. The same is seen for rank correlations, the patterns almost exactly matching, however with dampened magnitudes. This is to be expected as the rank correlation method more robust, less swayed by outliers which would exaggerate the correlation.

The mean height anomalies shows a completely different pattern, with little physically explainable structure. There is no annular structure, and in some places resembles a wave-like structure in its alternating positive and negative correlations. There is an almost cross-like structure of positive correlation emanating from Antarctica. The maximum correlation value is only around 0.1, much weaker than those observed for variance anomalies. This reinforces the significance of the patterns seen with the SAM-variance correlations. 

:::{figure-md} sam_pearson

<img src="../figures/outdated_correlations/sam_pearson_correlations.png">

Pearson Correlations for SAM Index, PC1.

:::

:::{figure-md} sam_rank

<img src="../figures/outdated_correlations/sam_rank_correlations.png">

Spearman Rank Correlations for SAM Index, PC1.

:::
 

#### SOI Correlations

The SOI-variance correlations show little correlation except over the Pacific, which should be expected as this is the location of ENSO events. A strong band of positive correlation, a magnitude of around 0.25-0.3, exists between 40S and 60S, between NZ and South America, indicating this area is stormier when warm El-Nino events occur. There is also a small band of weakly negative correlation above the positive patch, that is likely caused by the changes in the westerlies across the Pacific. As with the SAM index, the rank correlation method shows no great discrepancies, again with slightly weaker correlations generally but with a similar maximum correlation.

The mean height anomalies correlations are again much weaker than for variance anomalies, with little apparent structure. The maximum correlation value is less than 0.1. This reinforces the significance of the patterns seen with the SOI-variance correlations. 

:::{figure-md} soi_pearson

<img src="../figures/outdated_correlations/SOI_pearson_correlations.png">

Pearson Correlations for SOI.

:::

:::{figure-md} soi_rank

<img src="../figures/outdated_correlations/SOI_rank_correlations.png">

Spearman Rank Correlations for SOI.

:::


#### DMI Correlations

The DMI-variance anomalies correlation maps have generally weaker magnitudes than both SOI and SAM index. There are coherent-looking effects over Australia and the Indian Ocean, as would be expected. There is a positive zone south of Australia, indicating more storms there during positive IOD events. Whereas a negative area exists over, and to the west of Australia, suggesting there are fewer storms here during positive IOD events. There is also a small patch of positive correlation over the south coast of Madagascar, suggesting stormier weather, which could be a local effect of the IOD however, the correlations are relatively small.

There are two more areas of positive correlation, equal in strength to that over the south of Australia, over the south Atlantic and off the southwest coast of South America. This could suggest that there are teleconnections between the IOD and these locations, or they could be incidental and indicate that the magnitudes of these correlations are too weak to draw any conclusions. 

The mean height anomalies correlations are again much weaker than for variance anomalies, with little apparent structure. The maximum correlation value is less than 0.1. 

:::{figure-md} dmi_pearson

<img src="../figures/outdated_correlations/DMI_pearson_correlations.png">

Pearson Correlations for DMI.

:::

:::{figure-md} dmi_rank

<img src="../figures/outdated_correlations/DMI_rank_correlations.png">

Spearman Rank Correlations for DMI.

:::

 
(ZW3-correlations)=
#### ZW3 Correlations

Initially correlations were done between variance anomalies and both ZW3 magnitude and phase, however this was deemed insufficient since ZW3 is quite mobile. This means that ZW3 events with high magnitudes could occur and affect the storm track strongly locally, but not on the other side of the globe. Therefore, due to the inconsistency of event locations, correlations would be weaker and local influences would go undetected. For this reason, ZW3 events of sufficient magnitude were separated into longitude bins and correlated those ZW3 magnitude time series with variance anomalies found in corresponding longitude bins. The code developed to achieve this can be [here](../sample_code/zw3_correlations.ipynb).

The ZW3-variance correlations also shows a annular structure, similar to the SAM-variance correlations, except weaker in magnitude and with no defined outer positive ring. This suggests there is stormier weather between 30S and 60S when the ZW3 is in a high magnitude state, and less storm weather south of 60S.

The weaker magnitude could be because of the mobility of ZW3, historically a difficult aspect to capture, which is not adequately considered with the longitude bins. This could be altered if the size of the longitude bins was altered, however reducing the bin size will mean that smaller samples (time series) would be used to calculate the correlations, which could lead to errors. There is little difference between Pearson and rank correlation methods as before.

The ZW3-mean height correlations as with each of the indices before shows little defined structure that can be explained physically. The absolute magnitudes are small again, less than 0.1.

:::{figure-md} zw3_pearson

<img src="../figures/outdated_correlations/zw3_pearson_correlations.png">

Pearson Correlations for ZW3.

:::

:::{figure-md} zw3_rank

<img src="../figures/outdated_correlations/ZW3_rank_correlations.png">

Spearman Rank Correlations for ZW3.

:::
