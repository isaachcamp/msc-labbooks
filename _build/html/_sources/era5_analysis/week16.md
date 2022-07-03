# Week 16

## 2022 June 13

### Composite Maps

- Results & Discussion

#### Zonal Wave 3

Composites of the mean height field for the full time series present very strong zonal wavenumber 3 patterns, with the patterns steadily circulating the pole in accordance with the phase shift. All composites have strong highs and weaker lows, with a single strong negative region. This negative region appears strongest when over the Pacific, though there are some phase bins with strong negative region over South America (phase bins 120E-60E and 120W-180W). There are regions of high variance consistent with regions of steep geopotential height gradient, though there does not appear to be any consistent structure. 

Strong ZW3 signals can be identified in all seasons and all phase bins in the mean height field. There are regions of strong variance anomalies, however, once more there is no consistent discernible structure in the hgih-frequency variance field. This could be because of the level of noise present with such a small sample size (each composite was constructed from only five months), however it is may be ZW3 has minimal effect on storminess. It has been suggested that ZW3 has an effect on the direction of storms and position of the storm track, however this was not clear in these composites. Provided a systematic shift in behaviour of individual storms, it can be expected that this coherence would be present in the composites. This is an unusual result, since the composites were not taken from a dataset that suppressed signals from other sources, and ZW3 signals are prominent in all the mean height composites. It could be expected therefore that there would be some more obvious structure to the high-frequency variance field also. Following Goyal et al. 2022, using the meridional wind field anomalies may reveal more coherent structure as ZW3 clearly has a much stronger influence on this field.

- Goyal finds strong seasonal cycle in phase and amplitude when using meridional winds with the seasonal cycle retained. 
    - 20-40 degrees between winter and other seasons and magnitude shift of 0.6-0.8, peaking in winter.
- Goyal uses CESM2 model of last 1200 years when considering the impact of ZW3 phase to make results more robust, this is the difficulty we have with only 20 data points for 60 degree bins. He also uses 20 degree bins. What impact does this have on our analysis?
- What impact does the linkage between meridional heat transport and ZW3 have on storm tracks?
- Goyal finds clear link between ZW3 phase and sea ice extent, which is also connected to the storm track, because a reduction in sea ice will reduce the meridional temperature gradient, reducing the speed of the polar jet and baroclinic instability, the potential energy store of storm tracks. This is a lagged relationship, as sea-ice extent does not respond immediately, meaning that some of the influence of ZW3 is missed in a simultaneous analysis.


### Maximum Covariance Analysis

Maximum Covariance Analysis (MCA) was performed on the variance and mean height fields for both monthly and daily data, to identify the main modes of variability between the two fields. Daily variance was unavailable so it was calculated using a rolling window on 12-hourly data. 

It was found that no one mode explains a particularly high percentage of variance, with maximum being a SAM-like pattern that explains 11.1% of variance. This suggests that many factors hold influence over the variance field, but the leading patterns are highly suggestive of the atmospheric phenomena 

_Why wouldn't there be a lot of variance explained by the leading modes?_

#### MCA with Monthly Data

Using North et al. Rule of Thumb, only the first two modes for the full time series and summer are unique. However, there are physical patterns such as ZW3 and ZW4 that appear in the higher order modes, and in other seasons, therefore these are considered but are not to be relied upon. 

A textbook SAM patttern is the leading mode for the full time series and each season -- except winter where the leading two modes explain the same variance to two significant figures -- explaining between 7.8% of variance in MAM and 11.1% in DJF. SAM is well-known to be the leading mode of variability across the SH so is to be expected, and supports the proposal of SAM as a controlling influence of feedback between mean height field and variance field. 

An ENSO signal appears consistently as the second mode of variability, except in winter where it is the leading mode. The leading two modes of the full time series for both variance and mean height modes are consistent, in that both resemble SAM and ENSO for modes 1 and 2, respectively. However, the modes in summer are not clear-cut ENSO patterns, but strongly resemble the picture identified in the covariance analysis between the two fields for summer (see below for details). There are signs of physical signals being separated between modes, for example in autumn; the second and third modes appear to be two separated components of ENSO, which is likely due to their assumed degeneracy. 

{cite}`goyal_new_2022` finds ZW3 explains a greater amount of variance in the meridional wind anomalies field, therefore there is a greater likelihood of non-degeneracy using this field in place of the geopotential height. The same paper uses a larger dataset -- a historical simulation of the last 1200 years from the CESM2 model -- which would again improve the chance of finding unique modes, which would also help investigate whether there are modes of variability that are stronger at different timescales, e.g., weekly or monthly. 

- 8% of variance in MCA explained by ZW3, in agreement with Goyal et al. 2021 {cite}`goyal_zonal_2021`??

#### MCA with Daily Data

##### Zero-Lag

Of the two windows tested, 7- and 15-days, it was found that the 15-day window leading modes explained more variance -- _why_? -- and the patterns were more consistent -- _again, why_? -- in the full time series and across seasons. Only the leading five modes were inspected, despite more higher order modes being non-degenerate, however the amount of variance explained was less than 5% after these first five modes. Inspecting modes higher than the leading three is ill-advised as the higher modes tend to be either have no physical basis or a combination of variance from different mechanisms. This is what is seen here, with the higher order modes explaining very little variance and possessing unusual patterns that aren't clearly associated with known phenomena or previous results, _(are there any previous results that support these findings?)_. 

SAM appears as the first mode of variability once again, across all seasons and in the full time series.

The second mode is less consistent, but resembles an ENSO-like pattern across all figures. Key features such as the large band across the subtropical Pacific and oppositely signed-region over the Amundsen Sea are not consistently identified in the second mode, and have differing geometry and locations to the picture seen in composite and covariance figures. The typical ENSO pattern, assumed to be the same as that seen in figure (_get figure number_), is identified in higher order modes in a few datasets, e.g. the fourth mode in JJA and fourth mode in the full time series. It is likely that the typical features expected from an ENSO signal are distributed across several modes, given the close connection with SAM. However, the composite maps, discussed in detail below, suggest the manifestation of ENSO is season-dependent, and a typical ENSO pattern is only seen in spring. There are features in other seasonal composite figures that appear to correspond with features seen in higher order modes. _Correlate SOI with other modes._ To investigate what modes are linked with ENSO, correlations were calculated between the second principal component (PC2) and the SOI. Correlations are fairly low in all time series except for SON, when ENSO records its strongest events. PC2 in spring has a very similar pattern to the extreme events for the same season (see composite figure), which agrees with the higher correlations, but other seasons have quite different patterns, with features resembling some of the higher order MCA modes. There are different types of ENSO events that occur, so this may indicate that some event-types, e.g. central Pacific El Ninos, are more common in some seasosn more than others, _(however, ENSO events have typical timescales longer than a single season, so this may not make sense)_.

__Correlate other PCs with SOI__

##### Lagged Data

A 5- and 10-day lag was added to the variance field to investigate whether short-timescale variance response to mean height field anomalies is simultaneous or delayed, in a similar fashion, though limited in scale, to the analysis performed by Lorenz and Hartmann 2001 {cite}`lorenz_eddyzonal_2001`. It was found, in the analysis with the full time series, applying a lag generally decreases the explained variance in higher order modes, but increases the amount explained for the leading two modes. Another common feature, with few exceptions, is 10-day lag explaining more variance than 5-day lag for the leading two modes. As a rule, autumn explains lower variance than any other season by a couple of percentage points. Correlations between mean height and variance PCs are of roughly the same magnitude for leading two modes, but are lower for higher order modes, in opposition to the trend found in explained variance. _Why would this be?_

There is a similar pattern in seasonal data for the modes, though the difference in explained variance is likely insignificant. Generally, greater lag has lower correlations between the two PCs, though the 5-day lag doesn't appear to be significantly different from the zero-lag for the leading PC. The second PC, which generally has higher correlations between variance and mean height PCs than the leading PC, has considerable differences between lagged analyses in all seasons except SON, which is consistently high.

_To establish which mode is most closely associated with ENSO, the time series of PCs 2-5 were correlated with the SOI._ Generally, correlations steadily decrease between PC2 and SOI with increased lag in all seasons except JJA, which is highly correlated with zero-lag, a magnitude of 0.41, but has minimal correlation with 5- and 10-day lagged analyses, ~0.05. 

##### Presence of ZW3 Signal in Leading Modes

Aside from the leading modes, ZW3-like signals are common in the higher order modes from the monthly data MCA. However, no ZW3 pattern emerges in any of the leading five modes from MCA with daily data. There are higher order modes in the daily data analysis, not clearly associated with ENSO, with zonal wave signals; ZW4 and ZW5 signals appear, as well as Rossby wave trains in the subtropics. This could be an artifact of the rolling window averaging, or it could indicate something about the timescale on ZW3 operates. Again it should be noted monthly modes after the second mode are not unique according North et al. Rule of Thumb, however they do appear physically interpretable. 


## 2022 June 14

### Hoskins & Hodges 2005 {cite}`hoskins_new_2005`

Large SST gradients more prevalent in summer, why?

Agrees with our analysis: 

- "The summer storm track (DJF; Fig. 2a) is almost circular but has largest magnitudes in the central and eastern Indian Ocean and a break in the region of South America. In autumn (MAM; Fig. 2b) the maximum is in the same location, but the storm track is more broken east of New Zealand. For winter (JJA; Fig. 2c) the picture has changed considerably. The storm track that was present in summer now occupies only the Atlantic and Indian Oceans, after which it spirals in toward Antarctica."
- "Circumpolar loop lost in the winter at 850hPa."
- "The winter and summer storm tracks as shown by the variance in V850 are nearly collocated with the maximum SST gradients shown in Figs. 1c,d."
- "the Southern Hemisphere winter storm track can appear weaker or stronger than that in the summer, depending on the diagnostic used. This closer similarity between the solsticial seasons is consistent with the small area of continental regions. The SST gradients (Figs. 1c,d) are very similar in the two seasons and are in fact slightly stronger in summer than winter between 35° and 55°S."
- "In vorticity, and even more in $\theta_{PV=2}$, the maximum average intensities are associated with the subtropical track. However, the polar track dominates when using geopotential height, for example."
- "Also, in agreement with others, and consistent with the thermal inertia of the largely ocean-covered surface, the Southern Hemisphere equinoctial season storm tracks tend to have similarity with those in the preceding seasons: autumn with summer, and spring with winter."


Other characteristics to check:

- "Winter spiral arms poleward from SA to South Indian Ocean, and from Australia to south of SA."
- "Clearly separated jet stream in winter and spring in upper troposphere" - doesn't appear the same in our results, not well-defined.

Points of Interest:

- "raises again the notion that there may be a positive feedback between the storm track and the SST gradients: the storm track leads to surface winds that drive the currents that lead to SST gradients, and these may be favorable for the storm track. If this coupled perspective is valid, the basic driving of the asymmetric SH winter storm track structure in both the upper and lower troposphere is by the asymmetries in tropical convection."

Inatsu and Hoskins (2004), using controlled experiments with an atmospheric GCM confirmed that the zonal asymmetry of SST was crucial for the lowlevel winter storm-track structure.


## 2022 June 15

### Fredricksen & Fredricksen 1993 {cite}`frederiksen_southern_1993`

Simulate "cyclogenesis modes" and conclude that the regions of maximum cyclogensis are located downstream of the regions of maximum baroclinicity -- strongly suggesting baroclinicity manufactures synoptic-scale waves. They also find modes that exhibit similar structures to common atmospheric phenomena such as ZW3 and ENSO signals.

Other Charateristics to check:

- Summer finds a prominent mode with a ZW3 signal, whereas the most prominent mode in winter is similar to a teleconnective pattern identified in Karoly 1989b.

Points of Interest:
- Anomaly patterns are different in different ENSO events, discussed in Karoly 1989a. Could be due to various event types, EP and CP... might be useful for explaining the variation of MCA modes.

### Berbery & Vera 1996 {cite}`berbery_characteristics_1996`

Synoptic-scale waves develop downstream of maximum baroclincity. Can be identified with filtered and unfiltered data. Present a wave-packet view of storms, and suggest that the wave-packet is most prominent in the subtropical jet where baroclinicity is weaker.

"Trenberth describes fluxes caused by the storm track of properties such as heat, momentum, moisture."

### Karoly 1989 {cite}`karoly_southern_1989`

In agreement with our results:
- Geopotential height anomalies roughly circular around 60S, SAM-like signal, during summer, but much more wave train-like in winter, with a high over the Amundsen sea, and low equatorward and westward of that.
- Maxima greater in Indian ocean, lower in Atlantic, lowest in Pacific.

Other characteristics to check:
- Winter ENSO events show a fair amount of variability, however, of the four El Nino events investigated, three of them display discernable ZW3 signals.


## 2022 July 16

### Sensitivity of Blocks and Cyclones in ERA5 to Spatial Resolution and Definition {cite}`rohrer_sensitivity_2020`

#### Summary

ERA5 is state-of-the-art for investigating storm tracks. Using the full resolution is unnecessary as lower resolution performs equally well, therefore computation can be saved by using lower resolution since it is insensitive beyond a certain resolution. They find that the Eulerian method (the same as ours) is much less sensitive to changes in dataset and resolution than the Lagrangian method, where the tracking method introduces a greater amount of variation in storm behaviour and characteristcs.

They conclude that ERA5 is similar to ERA-interim in quality of results. This means that previous results based on ERA-interim are able to validate our results. When comparing models, it is advised to use the same resolution.


### An Evaluation of Surface Climatology in State-of-the-Art Reanalyses over the Antarctic Ice Sheet {cite}`gossart_evaluation_2019`

#### Summary

Diagnoses biases in humidity, near-surface temperature, wind speed, and snow cover for four reanalyses products: ERA-5, ERA-interim, MERRA2, and NCEP CFSR. ERA-5 places too great an emphasis on the relative humidity seasonal cycle, with values too low for winter, _this could have repercussions for convection, hence atmospheric waves_. The conclusion drawn here is that the katabatic flow is too dry and sublimation from blowing snow is not parameterised. There are known biases for near-surface winds around Antarctica; ERA-5 underestimates winds along the coast and in the interior over the entire year, and overestimates winds over the Antarctic peninsula -- this is likely transmitted vertically and present in Z500 field {cite}`gossart_evaluation_2019`.


### What Makes ERA5 Unique?

Compared to previous generations, ERA-5 incorporates improvements in physics, data assimilation techniques and an updated numerical weather prediction model. It makes use of the Integrated Forecasting System (IFS) Cy41r2, a decades worth of improvement on the previous generation. Data acquisition comes from more sources, incorporates updated boundary conditions, such as radiative forcings from CMIP5, and more correction procedures are in place that make use of observational data. Improvements in representing key quantities in the troposhpere are considerable from the previous generation, ERA-interim. {cite}`hersbach_era5_2020`  The greatest improvement in ERA-5 is the increased spatial, horizontal and vertical, and temporal resolution. However, Rohrer et al., 2020 find that Eulerian methods are insensitive to spatial resolution beyond a point {cite}`rohrer_sensitivity_2020`. 


### The Zonal Asymmetry of the Southern Hemisphere Winter Storm Track {cite}`inatsu_zonal_2004`

### Summary 

The authors use a GCM to establish the relationship of aymmetrical SSTs and orography in the SH. They conclude that tropical SSTs generate stationary waves that strongly influence the strength of the upper-tropospheric storm track, and local SSTs strongly influence the lower tropospheric storm track, resulting in the observed asymmetries. Orographic features, i.e. the Andes and South African Plateau, influence the storm track through their contributions to downstream cyclogenesis, leading to maxima in corresponding ocean basins.

SST gradients intensify passing storm systems, and have been linked to intensification of the jet stream through vertical motion driven by enhanced convection on the warm side, provided the anomalies are localised around the jet stream {cite}`brayshaw_basic_2011` (_not 100% sure on this, need to double check_).


### Opposite Phases of the Antarctic Oscillation and Relationships with Intraseasonal to Interannual Activity in the Tropics during the Austral Summer {cite}`carvalho_opposite_2005`

#### Summary 

Suggests that ENSO plays a role in modulating SAM phase, driving negative mode during El Nino, and positive mode during La Nina. /they also suggest that the predominant driver of SAM phase is anomalous convection patterns over the Pacific warm pool that drive Rossby wave trains poleward, similar to Goyal et al. 2021, which he suggests is also the driver of ZW3. Combine this with Campitelli et al. 2022, where the asymmetrical component of SAM is a ZW3-like pattern, that is completely explained by forcing from ENSO, this suggests that all three are intimately intertwined. 

In agreement with our results:

- Similar circular structure of wind anomalies around the pole during austral summer, with highs in Pacific, Indian and Atlantic oceans.

### Trend and teleconnection patterns in the climatology of extratropical cyclones over the Southern Hemisphere {cite}`reboita_trend_2015`

#### Summary

Authors propose there is a positive trend in the frequency of high intensity and low intensity storms, and it is likely that a poleward shift of the baroclinic region (storm track) will occur with global warming.

Results to compare:

"EN years are associated with higher cyclones track density from central South Pacific Ocean to extreme south of South America and in southern-central South Atlantic Ocean. At the same time, lower cyclones track density occurs in the mid-latitudes of the Indian Ocean, except in its west sector. Opposite spatial pattern is obtained during LN years. The higher frequency of cyclones in lower latitudes during EN years when compared to LN can be associated to the strengthening and slight displacement towards the equator of the subtropical jet (Trenberth et al. 1998)"
