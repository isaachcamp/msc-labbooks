# Week 10

## 2022 May 02 

### ZW3 Longitude Bins

Zonal Wave 3 is particuarly mobile, meaning that any index must consider its phase. For this reason the Goyal index {cite}`goyal_new_2022` was chosen, and the time series for ZW3 magnitude was split into 12 longitude bins, 30 degrees wide. Correlation and covariance maps were calculated for each of these bins by taking the data whose time stamp aligned with times in which the ZW3 was in a given phase. Thus a pair of reduced time series were used in correlation/covariance calculations. This left a particularly small sample when also splitting the data into seasonal, hence any time series with less than 10 data were ignored. 


### Yearly Correlation & Covariance Maps

Side-by-side figures created for mean height anomalies and short-scale variance anomalies of the 500hPa geopotential height field. This is conducted for both Spearman rank and Pearson product-moment methods.

#### SAM 

:::{figure-md} sam_rank

<img src="../figures/correlations/yearly/sam_rank_corr.png">

Spearman Rank Correlations for SAM Index, PC1.

:::

##### Mean Height Anomalies

Mean height anomalies show textbook SAM pattern, with positive correlations between 30S and 60S -- with a maximum value reaching roughly 0.5 -- and negative correlations over the pole -- reaching a low of around -0.8 -- extending to 60S, where the zero correlation is roughly found. The picture is highly symmetrical, however there are three apparent maximums for positive correlation in a band at approximately 50S, centred over the eastern Indian Ocean, the western Atlantic over South America, and western Pacific, south east of New Zealand. 

```{note}
Could this be a tracer for ZW3? This is the picture seen in the literature -- _remind yourself why the three maxima exist._
```

There is also a significant diminishing correlation around the central Pacific, and another, though not to the same extent, found south of Australia.

##### Short-Scale Variance Anomalies

Another textbook SAM pattern is seen, with alternating negative and positive annuli emanating from Antarctica. Negative correlations are centred over the pole, although relatively weak. A ring of positive correlations is found around 60S -- approximately over the mean height zero correlation line -- with three highs centred in the same locations as the highs for mean height anomalies, in the Indian, Atlantic and Pacific oceans. A further band of negative correlations are located equatorward, with a similar longitudinal pattern of three extrema in roughly the same locations, though less distinct. Where reductions in correlation values are found for mean height anomalies, so too are the found for the short-scale variance anomalies. Absolute correlation values are lower however, positive and negatives reaching a maximum/minimum of around 0.4 and -0.3 respectively.


#### SOI 

```{note}
Both mean height and variance anomalies colour bars are skewed positive. This is likely because of the positive skewing the SOI dataset. These maps should be corrected and redone. _Is this true?_
```

:::{figure-md} soi_rank

<img src="../figures/correlations/yearly/SOI_rank_corr.png">

Spearman Rank Correlations for SOI.

:::

##### Mean Height Anomalies

Mean height anomalies show a strong band of positive correlation over the Pacific ocean from north-east of New Zealand, around 30S, to southern South America, around 40S. This indicates average height of the 500hPa geopotential field is greater than average during cold La Nina events, and lower than average during warm El Nino events. The strongest correlation occurs in the western Pacific with a value of just less than 0.6, and another local maxima occurs off the the western coast of South America, about 0.4. Aside from this band that stretches from across the Pacific, there are a further two local maxima around 40S, one centred over the mid-Atlantic, another over the mid-Indian ocean. This also looks like a trace of ZW3.

```{note}
Could this be from ZW3 interfering in this correlation? In which case, could Partial correlations be of use?
```

There is also a strong minimum south of this narrow band, with a correlation of -0.35, as well as one located over south western Australia. The existence of these other alternating maxima and minima is suggestive of a ZW3 pattern.

##### Short-Scale Variance Anomalies

A similar band across the Pacific ocean can be seen, though further poleward, with one tail ending over the southern South American peninsula, the other tail wraps in towards the pole ending at around 60S. There appears to be two maximum connected by a narrow strip located in the centre of this band, reaching a maximum correlation of 0.3. A region of negative correlation is found directly north of the western end of the positive region, though the minimum value is only around -0.2. There are no more more particularly distinctive regions that might be physically meaningful.


#### DMI

:::{figure-md} dmi_rank

<img src="../figures/correlations/yearly/DMI_rank_corr.png">

Spearman Rank Correlations for DMI.

:::

##### Mean Height Anomalies

Negative correlation values are generally weak, indicating there may be little connection between the IOD and the mean height field. The positive skew could however be from the assumption of a normally distributed DMI -- this will be investigated in the future. There is a positive region located in the Indian ocean that stretches from off the south coast of India, across Australia to New Zealand's north island. A coherent, but weakly correlated negative region is seen directly south of New Zealand, around 60S, however the magnitude is weak enough to be inconclusive. There is a second prominent positive region located off west of the Antarctic and South American peninsulas, however this is also very weak and may not be physically meaningful. 

##### Short-Scale Variance Anomalies

The correlation values are generally weaker for the DMI than than seen for other indices, indicating that there may be little connection between the IOD and the storm track. A negative region stretching across the Indian ocean to north of New Zealand, reaching a maximum of -0.25 over Alice Springs, Australia, is well aligned with the positive region seen in the mean height field. This is a relatively coherent pattern and could indicate there is some physical reason for this.


#### ZW3

##### Phase -180 to -150

:::{figure-md} zw3_-180_-150_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-180_-150_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -180 to -150.

:::

###### Mean Height Anomalies

Weaker ZW3 pattern here, with much less distinct extrema, both positive and negative, than can be seen in other phase bins. There are still strong positive regions off the coast of Antartica, in the Amundsen sea. and south of Australia, though the one that should be south of South Africa is weak. There are also strong negative regions east of New Zealand and east of South America.

###### Short-Scale Variance Anomalies

There is little distinctive pattern here, as is common to most of the following figures for variance anomalies. There is a cluster of local positive maxima over Antarctica, with the strongest maximum located over the Amundsen and Ross seas. The positive regions do however, vaguely resemble the structure seen in the mean height field anomalies.

A small, indistinctive positive region can be seen off the south western coast of South America, north of the Antarctic peninsula. It might not have been of note except for the presence of such a region in many, if not all of the graphs, which is also aligned very well with a negative region in the mean height field. Both these regions seem to have migrated poleward as compared to phases between 0 and 180, see note for [ZW3 Phase 150-180](first-common-feature).


##### Phase -150 to -120

:::{figure-md} zw3_-150_-120_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-150_-120_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -150 to -120.

:::

###### Mean Height Anomalies

As with the -180 to -150 phase bin, a weaker ZW3 pattern is observed, with missing positive and negative extrema, however still ostensibly resmembling ZW3 and the correlation values appear to be consistent with other phase groups. Again, there is a strong positive region off the coast of Antartica, in the Amundsen sea, although shifted equatorward, as well as south of Australia. Weaker regions of negative correlation exist between the positive ones, the strongest located east of New Zealand as per the previous phase group.

###### Short-Scale Variance Anomalies

Generally weaker correlations here than for other ZW3 phases. A cluster of positive correlations can be seen around the Antarctic, the strongest at 0.3 is found between the Amundsen and Ross seas. A negative region south of New Zealand aligns well with the equivalent negative region in mean height field anomalies. Once again, the pattern vaguely resembles that seen in the mean height anomalies.

A strong negative region centred on the coast of Brazil at around 30S is well-aligned with a region of positive correlation seen in the mean height anomalies. Whilst a region of positive located directly below the aforementioned negative region is possibly a common feature between phase bin maps, however it has migrated poleward along with the (potentially) associated negative region of the mean height field, see note for [ZW3 Phase 150-180](first-common-feature).


##### Phase -120 to -90

:::{figure-md} zw3_-120_-90_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-120_-90_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -120 to -90.

:::

###### Mean Height Anomalies

A strong ZW3-like spatial correlation pattern, with positive and negative extrema possessing correlations of 0.5 and -0.5 respectively. This is the expected result as the ZW3 is defined according to the mean height field. The three expected negative regions are however, much weaker and less distinctive -- the third region in the Indian ocean is very weak. 

###### Short-Scale Variance Anomalies

A region of strong positive, 0.4, is located above the Ross sea, whilst almost directly opposite, on the other side of Antarctica, there exists a strong negative region, -0.4, above the Lazarev sea. This negative region lines up well with the negative region of the mean height anomaly field, however the aforementioned positive region lies on the lower tail end of Pacific positive region of the mean height field, therefore no strong link can be inferred here. There is a particularly strong negative region in the central Pacific, around 35S, which aligns well with the mean height positive region. There is also a strong positive region north west of New Zealand, that could be linked to the mean height negative region present to the south east.


##### Phase -90 to -60

:::{figure-md} zw3_-90_-60_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-90_-60_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -90 to -60.

:::

###### Mean Height Anomalies

A very strong ZW3-like spatial correlation pattern, with positive and negative extrema possessing correlations of 0.6 and -0.5 respectively. The three expected negative regions are again weaker and less distinctive -- the third region south of Tasmania is very weak. _This is a consistent feature found across each of the phase groups -- weaker negative regions with a particularly weak third region._

###### Short-Scale Variance Anomalies

There appears to be three very strong positive regions in a ZW3-like pattern, however much less extensive and shift meridionally toward Australia. A positive region, 0.4, extends zonally to the south of South Africa whilst negative regions of considerable extent spread across the entire Pacific ocean, and from Australia poleward and toward the Indian ocean. These regions may be associated with the two mean height positive regions.


##### Phase -60 to -30

:::{figure-md} zw3_-60_-30_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-60_-30_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -60 to -30.

:::

###### Mean Height Anomalies

A strong ZW3-like pattern, although weaker than the previous phase group. The three negative regions are once again weaker and less distinctive. The positive region over the Atlantic is unusual in that it is weaker, and appears to extend westward and equatorward over South America, reaching a maximum somewhere over Brazil.

###### Short-Scale Variance Anomalies

Very little in the way of spatial pattern can be seen. The are a few strong positive regions around Antarctica, consistent with other phase groups. These regions vaguely resemble a ZW3 pattern, in that there are three distinct regions interupted by fainter negative ones, however there is a fourth strong positive extremum over the pole and the pattern is quite diffuse -- significance is hard to establish, _this could be where significance testing is useful_. There are other dispersed negative regions of considerable magnitude, however it is difficult to establish any context for them. Arguably, there exists three negative regions that align reasonably well with the mean height positive regions, however this could be fanciful.


##### Phase -30 to 0

:::{figure-md} zw3_-30_0_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_-30_0_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group -30 to -0.

:::

###### Mean Height Anomalies

A strong ZW3-like pattern, but three negative regions are significantly weaker. Only one negaitve region can be discerned, the others two appear to be subsumed by the positive regions that extend much further than for other phase groups. The positive region over the Atlantic again extends westward and equatorward over the South American peninsula -- this appears to occur often in other phase groups.

_Another possibly consistent feature seems to be the alignment of the mean height positive regions with negative regions in the variance anomaly field. This, alongside the variance positive regions closer to pole, and somewhat in alignment with the mean height negative regions, could be significant. This is particularly apparent for this phase group -- something to investigate._

###### Short-Scale Variance Anomalies

Another cluster of positive regions around the South Pole. Align reasonably well with the mean height negative region (that appear to be enveloped by the positive regions -- assuming that these are negative regions, as they are very weak in this phase group). Three negative regions align well with the mean height positive regions. There is also another negative region between South Africa and Antarctica that doesn't clearly align well with any thing.


##### Phase 0 to 30

:::{figure-md} zw3_0_30_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_0_30_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 0 to 30.

:::

###### Mean Height Anomalies

A very prominent ZW3 pattern can be observed, with strong correlations reaching an absolute maximum of 0.6. There is a reduction in correlation centred over the Antarctic, though only slight. This is the strongest ZW3 pattern between phase groups, with prominent positive and negative regions, however there remains the common feature of one negative region being weaker than the other two -- this one over the eastern Pacific ocean.

###### Short-Scale Variance Anomalies

Another indistinctive pattern here, although the absolute correlations are still strong at about 0.6 again. There are strong maxima of positive correlation centred over South Africa and west of South America. Three tails of strong negative correlations emanate from Antarctica roughly over the same location as the positive mean heights anomalies -- another common occurrence, though these regions are broader whereas other maps present tight, small negative regions aligning with the mean height positives.


##### Phase 30 to 60

:::{figure-md} zw3_30_60_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_30_60_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 30 to 60.

:::

###### Mean Height Anomalies

Another prominent ZW3 pattern can be observed, with strong correlations reaching an absolute maximum of 0.6. Two negative regions are once again less distinctive however, and a merge into a single weakly negative region stretching across the pole between the Atlantic and Indian oceans. This weak, diffuse region is however, very well-aligned with a band of strongly positive correlation found in the variance anomaly field.

###### Short-Scale Variance Anomalies

Again a confused pattern, difficult to draw any conclusions about. However the correlation values are extremely strong at 0.5 again. There is a spread of strongly positive regions clustered around the pole, hwich seem to align fairly well with the mean height negative regions. There is also a region of strong negative correlation, centred over the south island of New Zealand, that aligns well with a region of strong positive correlation in the mean height anomaly field.

In this phase group, a potentially common feature appears, with a strongly positive region at 20S-30S off the South American eastern coast aligns well with a mean height anomalies negative region.


##### Phase 60 to 90

:::{figure-md} zw3_60_90_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_60_90_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 60 to 90.

:::

###### Mean Height Anomalies

A less obvious ZW3 pattern but once again with strong correlations reaching an absolute maximum of 0.6. This occurs for a single one of the positive and negative extremes, the other extrema are much less distinctive, more diffuse. Two of negative extrema are weaker and less distinctive. There are also a further two local minima found equatorward of the prominent pattern, which may be indicative of Rossby wave trains -- _this seems a stretch_. 

###### Short-Scale Variance Anomalies

Strong positive correlations clustering around the pole, with a further positive region at lower latitudes off the east coast of South America. A strongly negative region follows the zero line of the mean height anomalies field to the south of New Zealand.


##### Phase 90 to 120

:::{figure-md} zw3_90_120_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_90_120_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 90 to 120.

:::

###### Mean Height Anomalies

Another strong ZW3 pattern, as expected. A negative skew in the maximum correlation values, seemingly localised to the negative extremum located in the central Pacific, whilst the other negative extrema are less pronounced. Strong positive extrema that extend and meet over the Antarctic, where the correlation is much weaker. 

###### Short-Scale Variance Anomalies

Indistinctive pattern here. One particularly pronounced positive region, a high of over 0.5, located close to Antarctica, south of the African continent, which lines up well with the positive region of the mean height field -- though this region is much more extensive. A couple of other, less pronounced, positive regions are located above South Africa and the off the south coast of Western Australia. A strong negative region on the south west coast of South America lines up well with another of the positive mean height anomaly field regions -- an inconsistent pairing, as noted above with the complete opposite case, therefore difficult to say whether this is significant. There is some alignment between negative regions and the mean height positive regions, as seen in many other phase groups, except for the aforementioned strongly positive region which in some way contradicts this.


##### Phase 120 to 150

:::{figure-md} zw3_120_150_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_120_150_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 120 to 150.

:::

###### Mean Height Anomalies

Another strong ZW3 pattern, highs and lows of 0.6. The location of the three highs and lows are circling the globe as would be expected with the changing phase. The third negative region is once again less prominent, and intruded upon by the two positive regions either side of it.

###### Short-Scale Variance Anomalies

A diffuse region of strong positive correlation is aligned well with the positive region of mean height field anomalies, stretched across the western side of the South American and Antarctic peninsulas. Whilst a second cluster of local positive maxima align well with the strong negative region of mean height field anomalies in the Atlantic. Again little obvious pattern can be discerned, however the correlation values remain high. _There is arguably three negative regions aligning with the three mean height positives, though again this could be a stretch._


(first-common-feature)=
##### Phase 150 to 180

:::{figure-md} zw3_150_180_rank

<img src="../figures/correlations/yearly/zw3_30_deg/zw3_150_180_rank_corr.png">

Spearman Rank Correlations for ZW3, Phase Group 150 to 180.

:::

###### Mean Height Anomalies

Very prominent ZW3 pattern, slight negative skew in the extrema with maximums of 0.5 and -0.6 for positive and negative respectively. The negative regions are much more distinct than other longitude bins.

###### Short-Scale Variance Anomalies

A strong positive region extends from South America's southern tip south and through Antarctica to the coastline south of Australia. This roughly follows the positive region in the mean height field correlations, however the extent is much reduced and almost a single line drawn directly between South America and Australia. There are a couple of negative regions in southern Indian ocean that also align well well a negative region of the mean height field. Another negative region off the southern coast of South Africa aligns well with a positive region in the mean height field. The same is true of negative regions to hte west of South America and south of Australia -- consistent with other phase groups.

Once more there is a region of positive correlation off the southern coast of Brazil, in the Atlantic ocean, which aligns well with a strong negative region in the mean height field. _Check this out, is it really significant?_

```{note}
__Ignore__. This is a common occurrence for ZW3 phase between 0 and 180 degrees longitude! A negative region in the mean height field located off the the eastern cost of South America, around 30S, which aligns very well with a positive region in the variance field.
```

##### ZW3 Summary

- The regions in the variance field are generally much less extensive than any that they may be associated with in the mean height field.
- There is most often three weaker negative regions in the mean height field, with one in particular being weaker than the others.


## 2022 May 03

### Seasonal Correlation Maps

#### SAM

```{figure} ../figures/correlations/seasonal/sam/DJF_sam_rank_corr.png
---
name: sam-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for SAM Index, PC1.
```

```{figure} ../figures/correlations/seasonal/sam/JJA_sam_rank_corr.png
---
name: sam-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for SAM Index, PC1.
```

```{figure} ../figures/correlations/seasonal/sam/SON_sam_rank_corr.png
---
name: sam-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for SAM Index, PC1.
```

```{figure} ../figures/correlations/seasonal/sam/MAM_sam_rank_corr.png
---
name: sam-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for SAM Index, PC1.
```

##### Mean Height Anomalies

Strongest, most distinct SAM signal is seen during austral summer months, as per literature. A highly symmetrical ring of positive correlation encircles the strongly negative correlative region over Antarctica, the zero line is found at about 60S. There are three to four maxima within the ring, the strongest are located over Atlantic and Indian oceans. The maximum located across the Atlantic, stretching to the western coast of South America is arguably two maxima, with a slight saddle between. The positive extrema are all quite narrow, and well-defined meridionally. There is also a cessation of correlation located over the south Pacific. Both results agree well with the literature. The maximum correlation is skewed negative, at about -0.9, whereas the positive correlation is only around 0.5-0.6. _The reason for this should be investigated._

In austral winter, the positive ring is broken up into three prominent maxima, located at roughly the same latitude, although with a small deviation equatorward -- the literature suggests the mean height field, or at least the storm track, should wander equatorward. These maxima occur over the southwest Atlantic, Indian and southwest Pacific oceans. The maxima are broader than in summer, and shifted longitudinally. The maximum positive correlation is higher than in winter however, which doesn't mean the winds are stronger, only that the pressure field is more closely correlated with the first mode of variation i.e. the first principal component. The symmetry is somewhat broken, particularly the circular negative region over the Antarctic seen during summer. Instead, a negative arm protrudes outward over the Pacific, intruding on the weakly positive ring. Maximum negative correlation remains roughly the same as for summer.

The transition seasons are similar to summer and winter seasons, but to a lesser extent. For example, the spring months (SON) possess three distinct maxima as seen in austral winter, however it also possesses a complete positive ring. This ring is intruded upon by the protrusion from the negative centre, but it does not break the ring as is observed in austral winter and autumn. Autumn months similarly display characteristic features of both winter and summer, with a highly broken ring, over both the central Pacific and over the south of Australia -- a greater extent than even in winter. Also seen is the longer maximum, arguably two maxima, that stretches from the coast of South Africa, across the Atlantic and over the eastern Pacific. The highest positive correlation values occur during winter and autumn months over the Indian ocean -- this is consistent with the literature, _find the reason why again_. A consistent change that occurs between seasons is the zonal shifting westwards of the three positive maxima as the seasons progress.

##### Short-Scale Variance Anomalies

All seasons present generally strong correlation values, of around +/- 0.4.

In austral summer, a strong positive ring is observed around Antarctica, centred over 60S, approximately where the zero correlation line occurs in the mean height anomalies. This positive correlation indicates that the storm track is more active in these regions during a SAM positive phase. There is little significant correlation over Antarctica, as expected, however a weaker, more diffuse negative surrounds the positive ring, between 50S and 30S, indicating less storm track activity over these regions during a positive SAM event. This agrees well with relevant literature. Where the positive region is weaker in the ring seen in the mean height anomalies field, there is a well-aligned, broader region in the variance anomalies field -- _not sure what this means?_. There is also region of relatively strong positve correlation located over central south Australia.

During austral winter, the ring is more broken, with three more distincitve maxima, as per the mean height field. They are well aligned, but are situated further poleward. There is however, another region of strong positive correlation that doesn't align with any seen in the mean height field, found directly south of Tasmania. There is a strong region of negative correlation found between South Africa and western Australia, however generally there remains a weakened positive signal across the lower latitudes, which may be an indicator of the splitting jet stream -- the presence of a sub-tropical jet.

Once more the transition seasons display characteristics somewhere in between summer and winter. Spring months have a symmetrical ring, characterstic of austral summer, however the ring is more diffuse. There is also the positive region over Australia, but it is extended and has migrated northand westward, stretching over the eastern Indian ocean. The positive ring is encircled by a weaker negative region, as per summer, in agreement with a typical SAM pattern. In autumn, the positive ring is much more broken, with several maxima including one particularly large region of positive, east of the Antarctic peninsula. There is a region of weakly positive correlation over the central Pacific, equatorward of the ring -- the weakness of this region means it could be an insignificant feature -- however, otherwise there is the usual equatorward negative annulus otherwise seen in spring and summer.


#### SOI

```{figure} ../figures/correlations/seasonal/soi/DJF_SOI_rank_corr.png
---
name: soi-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for SOI.
```


```{figure} ../figures/correlations/seasonal/soi/JJA_SOI_rank_corr.png
---
name: soi-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for SOI.
```


```{figure} ../figures/correlations/seasonal/soi/SON_SOI_rank_corr.png
---
name: soi-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for SOI.
```


```{figure} ../figures/correlations/seasonal/soi/MAM_SOI_rank_corr.png
---
name: soi-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for SOI.
```

##### Mean Height Anomalies

In austral summer, there is a SAM-like signal present: almost a whole ring of positive correlation encricles the pole. However, this ring is more equatorward, and is less symmetrical -- the strongest maximum over the western Pacific is at 30S-40S. The positive region indicates that during La Nina events, there is a higher than average mean height; the opposite is true of El Nino events. The maximum negative correlation is much lower than that seen for SAM, however the positive maximum is in fact higher. The ring is broader, and there is little negative correlation to be seen over Antarctica. 

In austral winter, the strong maximum over the Pacific remains present -- a strong band of correlation stretching from north of New Zealand to the South American peninsula. However, other than a weak, diffuse positive region, the other maxima seen in summer disappear. There is a weak region of negative correlation poleward of the positive band that is consistent across all months. There is also a band of relatively strong, though much weaker than the positive band, negative correlation stretching from New Zealand, across the Indian Ocean to the South African coast. The negative maximum is much less than the positive maximum -- positive skewing -- which is seen in most seasons for SOI, but is particularly pronounced in winter.

Autumn and spring possess the same positve band in the Pacific, the extent differs between the two seasons however. In autumn, the band is much weaker and less extensive. There is still a second positive region in the Atlantic ocean not seen in winter, and a further weakly positive region stretching across Antarctica which is. The poleward negative region is more pronounced here, though it is even more pronounced in springtime, and seems as though it could be seasonal -- the region seems to exist over the pole in summer and migrate equatorward over the central Pacific through autumn, summer and transitions back in spring. In the spring, the positive band becomes even more extensive and the picture begins once more to resemble the SAM-like pattern seen in summer. The positive maximum east of New Zealand is particularly strong, being about 0.75. 

##### Short-Scale Variance Anomalies

There is another SAM-like signal for DJF months, though it is less distinct. Of note are the strong positive regions in the Pacific, wrapping around and poleward from South America to south of New Zealand. There are also two positive maxima west of the Antarctic peninsula and off the coast of the Amery ice shelf. There are also considerable negative regions in the Atlantic and Indian oceans at 40S, though the significance of this is to be determined. 

In austral winter, there is still a ring-like structure, again more diffuse, however it is generally at lower latitudes. The strong positive region seen across the Pacific faithfully follows the line of zero correlation in the mean height field -- a consistent feature for all seasons (as it is for all SAM correlation maps). This region has the strongest positive correlation value, around 0.35, however there are several other strongly positive regions: south of South Africa, off the Brazilian coast at approximately 35S, off the east coast of Madagascar and from central Australia spreading west across the Indian ocean. There is little in the way of negative correlation; what little there is is quite weak.

The strong positive band that is seen in all seasons is once again present for both spring and autumn. In both seasons, the region is well-aligned with the zero-line of mean height anomalies correlation field, consistent with summer and winter. In autumn, this band is generally weaker than spring, and more diffuse, also further east along the Pacific. Whereas, the band in spring is quite narrow, and wraps around the pole more, whilst the autumn band almost traces a line between South America and the New Zealand's north island, dipping to higher latitudes before returning equatorward. Two other positive regions are present in autumn, one over the Weddell sea, a second further eastward. In spring, the ring-like structure of summer is still absent, though the positive band strongly resembles a portion of the ring. There is a strong negative region equatorward of the positive band, well-aligned with the positive maximum observed in the mean height field.


## 2022 May 04

### Seasonal Correlation Maps

#### DMI

```{figure} ../figures/correlations/seasonal/dmi/DJF_DMI_rank_corr.png
---
name: dmi-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for DMI.
```


```{figure} ../figures/correlations/seasonal/dmi/JJA_DMI_rank_corr.png
---
name: dmi-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for DMI.
```


```{figure} ../figures/correlations/seasonal/dmi/SON_DMI_rank_corr.png
---
name: dmi-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for DMI.
```


```{figure} ../figures/correlations/seasonal/dmi/MAM_DMI_rank_corr.png
---
name: dmi-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for DMI.
```

##### Mean Height Anomalies

A strong positive ring is consistently located between 20S and 45S, broken in places with weaker correlations during the transition seasons. The ring is most prominent during austral summer. The strongest regions are found around Australia, extending from the western Pacific to south of the Indian subcontinent in austral summer, however it can vary significantly. The region appears over the Indian ocean during the autumn months, whilst it is quite prominent over Australia and poleward during the winter and spring months. The region for these months is much reduced as compared to summer.

A strongly negative region appears over South America during winter and spring months, with a significant positive region located directly beneath this region during spring. This positive region exists in other season, however it is much weaker.

##### Short-Scale Variance Anomalies

There is a consistent negative region that moves across from the central Indian ocean during during summer, with the negative extremum migrating eastward -- found over Australia in the winter months. During the transitional seasons, the extent of this region grows and the maximum shifts eastward. This region aligns fairly well with the positive region in the mean height anomalies field.

A positive region located south of this negative region is observed in all seasons. It is much weaker during spring, however another, possibly associated, positive region is located east of New Zealand.

There is a second consistent positive region in the central Atlantic, between 20S and 40S appearing in all seasons except austral summer. This is a particularly strong patch, which may suggest a teleconnection between the IOD and this region.

#### ZW3 30 Degree Phase Bins

Many of these figures were not produced as the sample size was too small -- some phase groups have a figure for a single season. There are approximately 516 data in a full time series, in this case these are grouped into 12 phase bins and four seasons, a total of 48 groups, leaving an average sample size of less than 11. There is also little obvious coherence in spatial patterns and the figures are quite coarse-grained. For these reasons, for seasonal maps at least, new phase bins of 60 degrees will be used for correlation & covariance maps.

```{note}
Is one reason why there is little pattern because it is blurred out due to ZW3's mobility? Such that the regions of maximum correlation are so strong and yet so small because they are highly consistent for the whole phase bin, whereas the surrounding regions are smeared out?
```

## 2022 May 05

### Seasonal Correlation & Covariance Maps

#### ZW3 60 Degree Phase Bins

```{note}
ZW3 is defined by the mean height field, therefore, in referring to the mean height anomalies correlation maps, regions that are components of a ZW3-like signal are referred to as such, e.g. the ZW3 low in the Pacific, or ZW3 high in the Indian ocean etc.
```
```{warning}
The interpretation of these maps are risky at best. There are some consistent features, but may well be physically meaningless. There are no obviously persistent trends depsite the correlation values being quite strong.
```

##### Phase -180 to -120

```{figure} ../figures/correlations/seasonal/zw3_60_deg/-180_-120/DJF_zw3_-180_-120_rank_corr.png
---
name: zw3--180--120-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for ZW3, Phase Bin -180 to -120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-180_-120/JJA_zw3_-180_-120_rank_corr.png
---
name: zw3--180--120-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for ZW3, Phase Bin -180 to -120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-180_-120/SON_zw3_-180_-120_rank_corr.png
---
name: zw3--180--120-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for ZW3, Phase Bin -180 to -120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-180_-120/MAM_zw3_-180_-120_rank_corr.png
---
name: zw3--180--120-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for ZW3, Phase Bin -180 to -120.
```

###### Mean Height Anomalies

In austral summer there is a clear ZW3 signal. There are regions of alternating positive and negative, though two of the negatives are either indistinct or completely missing. There is a single localised negative region southwest of South America. The ZW3 associated features are the only ones of note. Winter similar to summer; other than the ZW3 signal, there is a large positive region stretching from the central Pacific to north of New Zealand. 

There appears to be a transition between the seasons, in that the positive regions which are apparent in a sea of negative correlations for winter and summer, and to some extent in spring, whereas the reverse is true for autumn. This occurs for other phase bins too.

Spring and autumn both have distinctive ZW3-like patterns. In autumn, three strongly negative regions surround a positive region that extends across Antarctica -- the three expected positive regions have merged into a single central on with three protuberances. Little aligns with this region in the variance anomalies, however where a small recess in the central positive zone occurs, there is a particularly strong negative region in the variance map, though very limited in extent. Conversely, the spring months have more localised positive regions, howeever they are relatively weak. There are two strong negative regions and a third much weaker one in the Indian ocean.

###### Short-Scale Variance Anomalies

In DJF months, a large extended negative region in south of Australia aligns well with the positive region of the mean height anomalies, however it appears to extend further into the Indian ocean and poleward; a feature not reproduced in the mean height anomalies. There is a medium-sized negative region that corresponds with one of the ZW3 highs (positive) in the Pacific. There is also a strongly positive region west of South Africa that aligns with a negative region in the mean height map. The same is true of a region in the central Indian ocean. Over the winter months, there is a cluster of positive correlations over Antarctica that do not align with anything. There is a positive region east of Madagascar that aligns with the ZW3 negative region in that zone. Similarly, there is a negative region south of Australia that corresponds to the ZW3 negative. This is a reasonably persistent pattern in this season, but not always true.

Autumn is again inconsistent, some features align as in other seasons but not always in the same manner. The aforementioned localised negative maximum located over the Weddell sea aligns well with the zero-correlation region in the same location of the mean height map. A negative region off the Argentine coast sits just off-centre to a large mean height positive region, however this is not part of the ZW3 signal.Negative regions centred over Tasmania and off the South American west coast align with two ZW3 highs, and a positive region corresponds to one of the ZW3 lows in the Indian ocean. In spring, the only feature of note is the alignment of an extended negative band across the Pacific at 50S with the ZW3 positive region, however the size and shape is not coherent.


##### Phase -120 to -60

```{figure} ../figures/correlations/seasonal/zw3_60_deg/-120_-60/DJF_zw3_-120_-60_rank_corr.png
---
name: zw3--120--60-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for ZW3, Phase Bin -120 to -60.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-120_-60/JJA_zw3_-120_-60_rank_corr.png
---
name: zw3--120--60-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for ZW3, Phase Bin -120 to -60.
```

```{figure} ../figures/correlations/seasonal/zw3_60_deg/-120_-60/SON_zw3_-120_-60_rank_corr.png
---
name: zw3--120--60-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for ZW3, Phase Bin -120 to -60.
```

```{figure} ../figures/correlations/seasonal/zw3_60_deg/-120_-60/MAM_zw3_-120_-60_rank_corr.png
---
name: zw3--120--60-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for ZW3, Phase Bin -120 to -60.
```

###### Mean Height Anomalies

ZW3-like pattern is much more apparent throughout the seasons for this phase bin, except for autral summer where the signal is difficult to discern. In summer, a strong negative region exists over New Zealand, adjacent to a poleward, strongly positive region over the Ross and Amundsen seas. Semblences of the other expected lows and highs are visible, but are indistinct. There is a strongly positive region over South America, unconnected to the ZW3 signal. In austral winter, the ZW3 signal is much more apparent; three positive regions are very prominent, whilst the third negative zone is indistinct. It is hard to say definitively whether these two seasons are anti-phase given the summer months' lack of ZW3 signal, the story is different for the two transition seasons however. The anti-phase seen in the previous phase bin is not replicated here, though there is a wandering aspect to the highs and lows.

Another distinctive ZW3 pattern is found in spring, with three clear negative regions. There is a strong positive signal centred over Antarctica that protrudes equatorward over the Pacific and Atlantic oceans, and to a lesser extent over the Indian ocean. The expected localised positive regions appear to have been swallowed by this large positive zone. Autumn possesses with three positive regions and two negative, with a weaker third negaitve region.  

###### Short-Scale Variance Anomalies

The correlations remain strong for all seasons despite difficulty in establishing a pattern or common threads -- _why is this?_. 

No obvious patterns for any season. At this point, it seems wise to get a second opinion on whether documenting each isolated common feature is a good idea or not.


##### Phase -60 to 0

```{figure} ../figures/correlations/seasonal/zw3_60_deg/-60_0/DJF_zw3_-60_0_rank_corr.png
---
name: zw3--60-0-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for ZW3, Phase Bin -60 to 0.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-60_0/JJA_zw3_-60_0_rank_corr.png
---
name: zw3--60-0-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for ZW3, Phase Bin -60 to 0.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-60_0/SON_zw3_-60_0_rank_corr.png
---
name: zw3--60-0-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for ZW3, Phase Bin -60 to 0.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/-60_0/MAM_zw3_-60_0_rank_corr.png
---
name: zw3--60-0-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for ZW3, Phase Bin -60 to 0.
```

###### Mean Height Anomalies

- What are the correlation maximum values?
- Are there any regions that align with features in the variance maps?
    - Negatives over positives, positives over positives?
- Is there a clear pattern?
- Do they make sense physically?

Weak, but fairly clear ZW3 pattern seen in all months except austral winter, once again strongest during the transition seasons. Austral summer is missing the third negative region and the others are also weak. There is a very strong area of positive correlation over South America centred on 30S, around 0.7. A large negative region over the high latitudes can be seen in winter, stretching from 90S to 40S in some locations. There is an indistinct ZW3 pattern present. 

A much more prominent ZW3 pattern is observed in autumn, though the negative regions are once again weak, and displaced from the expected location for a ZW3 signal. The regions are of about the same magnitude as in the other seasons, however they are tighter and more localised. In spring there is another strong ZW3 signal, however the positives are fairly weak and diffuse and there is a a single negative region over the Antarctic, extending out to 40S only over South America. The other expected negative regions are subsumed by the broader positive zones. There is a highly positive region that extends across South America, but it is not well-aligned with any feature in the variance anomalies correlation map -- although there exists an extended, strongly negative band across the Atlantic at the same latitude, though displaced eastward.

###### Short-Scale Variance Anomalies

Very high positive and negative correlations despite there once more being no clear pattern. In most cases, the variance correlations are in fact larger than for the mean height anomalies -- _seems counter-intuitive also, when ZW3 is defined according to the mean height field_.

In austral summer, there is little coherence. Some regions align relatively well, though this not seen consistently across the whole map. These regions include the negative region over the Antarctic peninsula in mean height field aligning well with a diffuse positive region just west of the peninsula, and a mean height field positive located off the Antarctic coast, south of Australia, aligning with a diffuse negative region. There is another strongly negative region of around -0.8, however it is not clear how this lines up with anything seen in the mean height field. There are also a dispersed group of strongly positive regions in the Pacific, in the same location as a weakly negative region in the mean height. In winter, there exists a region of strongly positive correlation over the central Pacific that aligns well with a negative region in the mean hieght anomalies field. There is a high proportion of positive correlation that is matched by a highly negative mean height anomalies map, though the distributions do not align exactly, the vast majority is located in the higher latitudes. A strongly negative region over Australia aligns very well with a highly positive region in the mean height map.

In autumn, there is little that can be said to be features consistent with other phase bin correlation maps, with few regions reflecting what's seen in the mean height anomalies. Around New Zealand, there is a negative region that aligns with a positive mean height region, whislt equatorward there are similarly aligned zones of opposite sign, over eastern Australia. In austral spring, there is a positive band across the Pacific ocean, from the southern tip of New Zealand to the southern tip of South America, this aligns well with the zero correlation region. Otherwise, there is a positive region over the Lazarov sea that aligns well with a strongly positive mean height field.


##### Phase Bin 0 to 60

```{figure} ../figures/correlations/seasonal/zw3_60_deg/0_60/DJF_zw3_0_60_rank_corr.png
---
name: zw3-0-60-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for ZW3, Phase Bin 0 to 60.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/0_60/JJA_zw3_0_60_rank_corr.png
---
name: zw3-0-60-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for ZW3, Phase Bin 0 to 60.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/0_60/SON_zw3_0_60_rank_corr.png
---
name: zw3-0-60-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for ZW3, Phase Bin 0 to 60.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/0_60/MAM_zw3_0_60_rank_corr.png
---
name: zw3-0-60-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for ZW3, Phase Bin 0 to 60.
```

###### Mean Height Anomalies

All seasons are possess less distinctive ZW3 patterns than other phase bins, particularly in summer and winter the signal is very weak. In summer, there are only two positive and negative regions in the expected positions, however one negative region is very central, displaced toward higher latitudes. There is also a third positive region at almost 90S, confined to a small area. In the summer, there is almost no signal at all, with particularly weak correlations between 40S and 90S. There are still strongly positive regions in the subtropics, around 20S to 4S, 
notably off the west coast of South Africa, and in the Indian ocean.

In autumn, there is once more a weak ZW3-like signal, if you squint. Again weak correlations in high and mid latitudes. There is a single region of strong correlation in the central Pacific at 40S, and a strongly negative region northeast of there. These overlap reasonably well with oppositely-signed regions in the variance correlations. Spring in this phase bin is almost a perfect reflection of the same season but for phases -60 to 0 -- _what can this mean?_. A very strong, extensice positive region exists over the south pole, surrounded by three diffuse negative regions that are much more equatorward, between 50S and 30S.

###### Short-Scale Variance Anomalies

Austral summer sees a mirroring of positive variance correlations and negative mean height correlations, though inexact to be sure. The region centred over the south pole is particularly positive, well-matched with the extensive negative region of the mean height map in the same location. Winter brings some relief, there is a pattern! Sort of, there appears to be a spiral-like structure in the mean height field, that is somewhat mirrored by the positive regions visible in the variance map. Specifically, two arms emanating from the south pole curve outward from the Antarctic peninsula to the west coast of Australia, and from west of the Ross sea equatorward toward South America. _This is seemingly unique to this map, are there any other maps that follow the same pattern?_

Autumn brings little in the way of coherence, with a cluster of positive correlations in the high latitudes that correspond to the negative polar region in the mean height map. There is the aforementioned positive and negative regions aligning between the two maps (see above), however there is little else of note. In spring there is little obvious pattern, as always. A high proportion of positive correlations mirrors the high proportion of negative observed in the mean height map, however the location of the highly positive mean height region is also positive in the variance map. In the hemisphere cented over New Zealand there is a reasonable alignment between positive variance correlation and negative mean height correlations. 


##### Phase Bin 60 to 120

```{figure} ../figures/correlations/seasonal/zw3_60_deg/60_120/DJF_zw3_60_120_rank_corr.png
---
name: zw3-60-120-djf-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Summer for ZW3, Phase Bin 60 to 120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/60_120/JJA_zw3_60_120_rank_corr.png
---
name: zw3-60-120-jja-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Winter for ZW3, Phase Bin 60 to 120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/60_120/SON_zw3_60_120_rank_corr.png
---
name: zw3-60-120-son-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Spring for ZW3, Phase Bin 60 to 120.
```


```{figure} ../figures/correlations/seasonal/zw3_60_deg/60_120/MAM_zw3_60_120_rank_corr.png
---
name: zw3-60-120-mam-rank-corr
scale: 40%
align: left
---
Spearman Rank Correlations in Austral Autumn for ZW3, Phase Bin 60 to 120.
```

###### Mean Height Anomalies

A relatively consistent ZW3 signal observed here 

###### Short-Scale Variance Anomalies


### El Nino-Southern Oscillation Complexity {cite}`timmermann_ninosouthern_2018`

Contains a useful glossary of terms relating to ENSO.