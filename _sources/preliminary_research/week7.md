# Week 7

## Apr 11-15

(correlation-maps)=
### Correlation Maps

#### Correlations of Mean Height Field Anomalies

Correlations were also calculated between mean height anomalies and indices, for side-by-side figures. It is apparent that they show much weaker correlations.

#### ZW3 Correlations

Initially correlations were done between variance anomalies and both ZW3 magnitude and phase, however this was deemed insufficient since ZW3 is quite mobile. This means that ZW3 events with high magnitudes could occur and affect the storm track strongly locally, but not on the other side of the globe. Therefore, due to the inconsistency of event locations, correlations would be weaker and local influences would go undetected. For this reason, code will be developed early [next week](./week8.md) that separates ZW3 events into longitude bins and correlates only those ZW3 magnitude time series with variance anomalies found in those longitude bins.


#### SAM Correlations

A clear annular structure can be seen with negative correlations centred around 60S and positive correlations centred around 40S, a very SAM-like structure. This means that when the SAM index is negative, there tends on average to be more storms (more bandpass variance, at least) over the southern ocean centred at ~60S and fewer storms in mid-latitudes, centred around 40S. This is exactly the textbook picture of how the SAM operates.

:::{figure-md} sam_pearson

<img src="../figures/correlations/sam_pearson_correlations.png">

Pearson Correlations for SAM Index, PC1.

:::
 

SOI: Very interesting. Coherent-looking effects only really over the Pacific. More storms between 40 and 60S between NZ and S America, less to the north and weakly over/west of NZ. This should tie up with changes in the westerlies across the Pacific. Such a pattern will be quite seasonal (well they all will be I think).

 

DMI: Also very interesting. Coherent-looking effects only over Aussie/Indian Ocean, and I guess over the South Atlantic, i.e. everywhere except the Pacific! Less storms over/west of Australia in the +DMI, more over the Australian Bight. I assume this is consistent with the literature, but I don’t know off the top of my head. More storms from Madagascar across the south Atlantic and southern South America, though most of the correlations are smallish.

 

ZW3: Interesting maps though I don’t think correlation is quite the way to go here, as ZW3 itself is a bit mobile. The phase map shows an interesting pattern across NZ and the Pacific. The magnitude map shows a vaguely SAM-like pattern across the Pacific side of the hemisphere. I think the best way to approach the ZW3 effect is to calculate average HF variance anomaly maps for longitude bins of the phase, provided the amplitude is large enough, say about the median amplitude.

 

For all these results, I am thinking “What does the correlation map with the mean height anomalies look like?” and I think it would be nice to calculate pairs of maps for each index. In theory, changes in the location of the strongest winds should track changes in the storminess/variance. And of course, do all this seasonally etc etc.

 