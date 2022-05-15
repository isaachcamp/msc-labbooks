# Week 11

## 2022 May 13

### Composite Figures

Composite figures for the extreme (upper and lower 5% percent with a minimum of five data) events were generated. The composite mean of H500 mean height anomalies at the time of extreme events for a given index were plotted alongside the corresponding bandpass filtered variance anomalies. For SAM, SOI and DMI, the upper and lower quantiles are populated by positive and negative extremes, whereas ZW3 is always positive, so the lower qunatile is populated by the weakest events (_unsure of the value of this_). With ZW3, the sample size was below 100 for a given phase bin, hence it the quantile considered is greater than 5% to fulfil the minimum requirement of 5 data. This is true also of seasonal data for all indices, particularly ZW3 where the sample size shrinks to ~20. The upper and lower quantile values are presented in the figure subtitles.

#### SAM

##### Mean Composites

Textbook SAM pattern seen for upper and lower quantile events; the two are essentially a mirror image reflecting the oscillation between positive and negative modes. In the upper quantile -- the highly positive events -- there is a lower than average pressure over Antarctica extending out to 60S, and a ring of higher than average pressure between 40S and 60S. The central region is highly symmetrical, with the usual small protrusion out over the Pacific, whereas the positive ring around is ostensibly separated into three maxima over the three major oceans. What is quite notable is the asymmetry in the magnitude of mean height anomalies, the negative (lower than average) anomalies being much stronger than the positive anomalies. The lower quantile composite is almost an exact mirror image, except that the negative low over the Atlantic is much weaker than the positive high seen for the upper quantile compsite. This time the positive anomalies over the pole are much stronger than the weaker negative ring.

```{figure} ../figures/composites/sam/mean/mean_sam_composite.png
---
name: sam-mean-composites
scale: 40%
align: left
---
Mean Upper and Lower Quantile Composites for SAM Index, PC1 (Full Time Series).
```

Seasonally, there are much more distinct features that are smeared over in the full time series (yearly). Over the summer months presents a picture of SAM at its most symmetrical. There is a more distinctive, fuller ring of positive anomalies for the upper composite, with a near-perfect circle of negative anomalies over the pole and the Pacific protrusion is much reduced. In the lower composite there is a less symmetrical picture, with a the negative anomalies over the Pacific being almost non-existent. However, there still appear three maxima, though distributed over a limited range, between the Atlantic and Indian oceans. Winter sees a reduction in the magnitude of the maxima at 45S in the upper composite, and the asymmetry of the central region disintegrates slightly, with the Pacific protrusion more prominent. The lower composite presents another very nice mirror image of the upper -- even the Pacific protrusion is now a positive mean height anomaly. Autumn sees the upper composite's positive anomalies at their greatest magnitude, with three highly positive regions over the three major oceans around 45S. The Pacific protrusion is stronger still -- it seems at its most prominent during the transition seasons -- and is joined now by similar features over the Indian and Atlantic oceans, leading to a much broken positive ring. The same is true for the lower composite, however the Pacific protrusion is now the most anomalous feature on the map. A much broken negative ring and relatively asymmetrical central region. Spring is particularly interesting for two reasons: the Pacific protrusion is at its greatest extent, with strong negative anomalies reaching 45S; and the upper and lower composites are not alike. The lower composite has a much more symmetrical picture, with a more distinct negative ring at 45S, whereas the upper is highly asymmetrical, with a much more broken ring.

In winter and spring, there is a prominent positive anomalous region during strong El Nino events that aligns with the Pacific protrusion. There is a second positive region that aligns well with the protrusion over the Indian ocean during spring. During autumn there is good alignment between the positive region and the Pacific protrusion however, there is a highly negative anomalous feature in the SOI lower composite (strong El Nino events) adjacent to the positive zone that is unusual. There is no apparent equivalent region during summer. _Are the two connected?_


```{figure} ../figures/composites/sam/mean/DJF_mean_sam_composite.png
---
name: sam-djf-mean-composites
scale: 40%
align: left
---
Mean Upper and Lower Quantile Composites in Austral Summer for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/mean/JJA_mean_sam_composite.png
---
name: sam-jja-mean-composites
scale: 40%
align: left
---
Mean Upper and Lower Quantile Composites in Austral Winter for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/mean/SON_mean_sam_composite.png
---
name: sam-son-mean-composites
scale: 40%
align: left
---
Mean Upper and Lower Quantile Composites in Austral Spring for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/mean/MAM_mean_sam_composite.png
---
name: sam-mam-mean-composites
scale: 40%
align: left
---
Mean Upper and Lower Quantile Composites in Austral Autumn for SAM Index, PC1.
```

##### Variance Composites

In the full time series composite, the two quantile composites are nice reflections of each other. The textbook SAM zonal ring-like structure around 60S is quite apparent, though somewhat broken. Interestingly, during extreme positive SAM events (upper composite) there is a broader, stronger negative region over the Atlantic side of the pole, whereas the equivalent feature (positive in sign) is on the opposite side of the pole, over the Indian and Pacific oceans. 

```{figure} ../figures/composites/sam/variance/variance_sam_composite.png
---
name: sam-var-composites
scale: 40%
align: left
---
Variance Upper and Lower Quantile Composites for SAM Index, PC1 (Full Time Series).
```

During summer, there is a distinct positive ring centred on 55S, encircled by a second ring of negative anomalies at 45S. Summer positive SAM events the only composite to display this kind of inner-outer annuli feature so distinctly. Others have positive and negative regions, but not seen in such an obvious pattern. For example, the same cannot be said of the negative SAM during summer, in which only a negative ring of anomalies is apparent. Interestingly, there appears to be a reduction in variance anomalies, positive or negative, at roughly the same location as the Pacific protrusion, over all months. This is even apparent during summer, where the Pacific protrusion is not clearly present in the mean height anomalies. Winter is the complete reverse of summer, with the upper composite (positive SAM) now showing a single prominent ring of positive anomalies, whilst the lower composite (negative SAM) takes on the double ring pattern, though the outer ring much more broken than that seen during summer positive SAMs. Autumn is the most interesting season, in that the patterns are less distinctive and far from the textbook pattern. There is an extensive positive region over the Pacific, South America and Atlantic ocean that wanders meridionally. There is also a strong negative region in the Indian ocean that also wanders meridionally, but at roughly the same latitude as the positive region. This seems to be a unique feature of the autumnal months. During spring, there is, what appears at first sight, a much less distinctive ring, however the strength of a few maxima distributed zonally over the same latitude is much higher than those seen in summer or autumn. There is arguably still a prominent ring however, due to the colour-bar scaling to these highly localised maxima, it is less obvious. A similar picture is apparent in the negative mode extreme events, with strong lows distributed around the pole in a ring-like structure, however there is a highly positive region in the Indian ocean that is not apprent in during positive SAM events.


```{figure} ../figures/composites/sam/variance/DJF_variance_sam_composite.png
---
name: sam-djf-var-composites
scale: 40%
align: left
---
Variance Upper and Lower Quantile Composites in Austral Summer for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/variance/JJA_variance_sam_composite.png
---
name: sam-jja-var-composites
scale: 40%
align: left
---
Variance Upper and Lower Quantile Composites in Austral Winter for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/variance/SON_variance_sam_composite.png
---
name: sam-son-var-composites
scale: 40%
align: left
---
Variance Upper and Lower Quantile Composites in Austral Spring for SAM Index, PC1.
```

```{figure} ../figures/composites/sam/variance/MAM_variance_sam_composite.png
---
name: sam-mam-var-composites
scale: 40%
align: left
---
Variance Upper and Lower Quantile Composites in Austral Autumn for SAM Index, PC1.
```

#### SOI

##### Mean Composites

Over the full time series, taken from any month, the extreme cool La Nina events (upper quantile composite) have a reasonably clear ring-like structure around 45S, that spirals poleward from the major positive region, around 30S, in the Pacific -- a clear SAM-like signal. There is a strong localised negative region in the Pacific, right where the SAM Pacific protrusion in the mean height field is found -- _the two might be connected_. The SAM-like signal is not replicated in the lower composite (warm El Nino events) however the same localised region of the opposite sign is still present in the Pacific, and an extended negative region in the Pacific lower latitudes is apparent, closest to where the physical manifestation of ENSO occurs. Note that the average magnitudes of the anomalies are much lower than those of anomalies associated with extreme SAM events (see above).

Throughout all seasons, the strongly negative Pacific region at 50S is present during strong La Nina events, likewise the equivalent positive region is present during strong El Nino events. Though the magnitude of the region drops off in spring for La Nina and in autumn for El Nino. During summer there is a prominent positive ring at 40S during La Nina, and a negative broken ring which is less prominent in El Nino events, with strong localised maxima in the Atlantic and Indian oceans. Winter sees this ring dissipate, to be replaced by a large central negative region over the south pole in La Nina events, whilst two positive regions over the Antarctic peninsula and in the Indian ocean at 50S stand out, along with the major positive region over the Pacific. The Pacific region is negative during El Nino events, as expected, however a positive region over Southern Ocean south of Australia is apparent, a feature that extends westward over the Indian ocean -- a feature that becomes more prominent and localised in spring, but does not appear elsewhere. In autumn there is a much more extended negative Pacific region in La Nina events that stretches over South America. The usual major positive region in the Pacific is weaker, and two stronger positive regions exist over the Amundsen sea and over the Atlantic at 40S. During El Nino events in autumn, there is an unusally large and strong region of negative varaince anomalies south of New Zealand. In both El Nino and La Nina events there is little impression of the ring structure seen in other seasons. In spring, there is another large central region of positive anomalies over the south pole during La Nina events -- the opposite to winter, and a strong positive region in the Pacific ocean but little in the way of negative anomalies are apparent. During El Nino events, there is a strong region of positive anomalies, the aforementioned persistent feature, encircled by a ring of negative anomalies. There is a further region of positive anomalies over the south of Australia that is als seen during winter, as mentioned previously.

##### Variance Composites

The expected mirror image is apparent between El Nino and La Nina events for the full time series. More storminess is found during La Nina events in the Pacific, spiralling poleward over the Indian ocean. There is less storminess just south of Australia during La Nina events, a feature common to both La Nina and El Nino. During extreme El Nino events there is greatly reduced storm activity in the southern Pacific, but seemingly does little to increase storminess anywhere across the SH.

During austral summer, ther eis a higher amount of storm activity around 60S during La Nina events, and less storminess equatorward, around 40S, mostly over the Atlantic and Indian oceans. There are also a few localised negative and positive maxima. During summer El Nino events, there is less storminess over the Pacific in general, as well as over the Indian ocean. There is however, a couple of conspicuous regions of strong positive anomalies south of South Africa and in the central Atlantic. There is not the obvious meridional separation of positive and negative regions that is seen in the La Nina composite. La Nina events during winter display a general increase in storminess poleward of 40S, with a couple of particularly stormy regions south of South Africa and in central south Indian ocean. The reverse is true with El Nino events, with a general decrease in storminess with a particularly prominent minimum over hthe Pacific, in contrast to La Nina. Autumn sees a semi-ring of positive storminess over the Pacific and Atlantic, adjacent to a poleward region of negative storminess. The other half of the hemisphere is less structured, with interspersed positive and negative of varying strength. Autumn is interesting in that the effects of El Nino events are not clearly the inverse of those of La Nina. Similar to La Nina, there are adjacent bands of positive and negative, with negative further poleward, however the positive region has shifted zonally toward New Zealand. Once more, the other half of the hemisphere has no distinct structure. Back on more solid ground, springtime sees the usual mirror image of the effects of La Nina and El Nino events. The hemisphere is apparently split in two halves, with two semi-rings of positive and negative storminess, meeting south of Australia and over the Antarctic peninsula. The positive region, in the central Pacific, wanders slightly meridionally, but the central region lies approximately at the same latitude as that of the negative region, at 50S. Antarctica experiences more storminess overall, which is a common feature between La Nina and El Nino events. The opposite is seen in El Nino events, with the negative region located over the Pacific, the positive over the Indian and Atlantic oceans. There is a notable positive high storminess south of Tasmania and New Zealand, the reason for which is unclear.


#### ZW3 

30 degree bins were checked for the full time series, whereas too few data were available to repeat this for seasonal data, hence 60 degree bins were used. This could change if consistency is more important. The whole library of ZW3 figures has not been fully explored at this time, but will be done at a later date.

##### Mean Composites

Strong ZW3 signal in all of the phase group upper composites. It is not unusual for one high and one low to dominate in magnitude, but the overall signal is remarkably consistent across all upper composites and for all seasons as well as yearly -- excluding DJF, more on that later. As expected, the lower composites, with weaker ZW3 indices, is much less distinctive and possesses little consistent pattern. There is frequently a ZW4-like signal observed, and just often no zonal wave at all. This is true for both the full time series and for seasonal data.

##### Variance Composites

There are no clear patterns, often the signal looks similar to SOI or SAM variance patterns. A closer inspection of a few ZW3 figures would be a good approach to begin with, comparing the timestamps of ZW3 indices with SAM and SOI, which are known to cause a high degree of variance. Perhaps strong SAM or SOI events are drowning out the ZW3 signal, thus they may be subtracted to get an isolated picture of ZW3.


#### DMI

Magnitudes of mean and variance anomalies for DMI is much lower than other phenomena. There are some consistent features in the mean height anomalies field, however the signal seen in the variance is similar to SAM and SOI. This could indicate that they have similar effects, but given the generally smaller anomalies, it is more likely that the variance observed is due to other phenomena. Research into DMI will not be pursued further at this time.


- Get the behaviour of the SOI at the same timestamp as SAM extreme events, and vice versa. What does this say?