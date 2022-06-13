# Week 16

## 2022 June 13

### Composite Maps

- Results & Discussion

#### Zonal Wave 3

- Goyal finds strong seasonal cycle in phase and amplitude when using meridional winds with the seasonal cycle retained. 
    - 20-40 degrees between winter and other seasons and magnitude shift of 0.6-0.8, peaking in winter.
- Goyal uses CESM2 model of last 1200 years when considering the impact of ZW3 phase to make results more robust, this is the difficulty we have with only 20 data points for 60 degree bins. He also uses 20 degree bins. What impact does this have on our analysis?
- What impact does the linkage between meridional heat transport and ZW3 have on storm tracks?
- Goyal finds clear link between ZW3 phase and sea ice extent, which is also connected to the storm track, because a reduction in sea ice will reduce the meridional temperature gradient, reducing the speed of the polar jet and baroclinic instability, the potential energy store of storm tracks. This is a lagged relationship, as sea-ice extent does not respond immediately, meaning that some of the influence of ZW3 is missed in a simultaneous analysis.


### Maximum Covariance Analysis

Maximum Covariance Analysis (MCA) was performed on the variance and mean height fields for both monthly and daily data, to identify the main modes of variability between the two fields. Daily variance was unavailable so it was calculated using a rolling window on 12-hourly data.

#### MCA with Monthly Data

- 8% of variance in MCA explained by ZW3, in agreement with Goyal et al. 2021 {cite}`goyal_zonal_2021`??
- Two leading MCA modes with monthly data, SAM and ZW3
    - A-SAM component completely explains the connection between ENSO and SAM
    - ZW3 pattern driven by anomalous deep convection events in the tropics, e.g. ENSO events. 
    - Hence the two main modes of variation in ENSO can be interpreted as either SAM or ZW3 events. __But this doesn't agree with the daily analysis, where it looks very likely that ENSO is the second mode of variation and ZW3 is completely absent...__
- {cite}`goyal_new_2022` finds ZW3 explains a greater amount of variance in the meridional wind anomalies field, therefore there is a greater likelihood of significance using this field in place of the geopotential height. This is true also for the MCA analysis.

#### MCA with Daily Data

##### Zero-Lag

Of the two windows tested, 7- and 15-days, it was found that the 15-day window leading modes explained more variance -- _why_? -- and the patterns were more consistent -- _again, why_? -- in the full time series and across seasons. Only the leading five modes were inspected, despite more higher order modes being non-degenerate, however the amount of variance explained was less than 5% after these first five modes. Inspecting modes higher than the leading three is ill-advised as the higher modes tend to be either have no physical basis or a combination of variance from different mechanisms. This is what is seen here, with the higher order modes explaining very little variance and possessing unusual patterns that aren't clearly associated with known phenomena or previous results, _(are there any previous results that support these findings?)_. 

A textbook SAM patttern is the leading mode for the full time series and each season, explaining between 6.8-9.8% of variance. This is well-known to be the leading mode of variability across the SH so is to be expected, and supports the idea of SAM as a controlling influence of feedback between mean height field and variance field. 

The second mode is less consistent, but resembles an ENSO-like pattern across all figures. Key features such as the large band across the subtropical Pacific and oppositely signed-region over the Amundsen Sea are not consistently identified in the second mode, and have differing geometry and locations to the picture seen in composite and covariance figures. The typical ENSO pattern, assumed to be the same as that seen in figure (_get figure number_), is identified in higher order modes in a few datasets, e.g. the fourth mode in JJA and fourth mode in the full time series. It is likely that the typical features expected from an ENSO signal are distributed across several modes, given the close connection with SAM. However, the composite maps, discussed in detail below, suggest the manifestation of ENSO is season-dependent, and a typical ENSO pattern is only seen in spring. There are features in other seasonal composite figures that appear to correspond with features seen in higher order modes. _Correlate SOI with other modes._ To investigate what modes are linked with ENSO, correlations were calculated between the second principal component (PC2) and the SOI. Correlations are fairly low in all time series except for SON, when ENSO records its strongest events. PC2 in spring has a very similar pattern to the extreme events for the same season (see composite figure), which agrees with the higher correlations, but other seasons have quite different patterns, with features resembling some of the higher order MCA modes. There are different types of ENSO events that occur, so this may indicate that some event-types, e.g. central Pacific El Ninos, are more common in some seasosn more than others, _(however, ENSO events have typical timescales longer than a single season, so this may not make sense)_.

__Correlate other PCs with SOI__

##### Lagged Data

A 5- and 10-day lag was applied to the variance field to investigate whether the storminess response is simultaneous or delayed, in a similar fashion, though limited in scale, to the analysis performed by Lorenz and Hartmann 2001 {cite}`lorenz_eddyzonal_2001`. It was found, in the analysis with the full time series, applying a lag generally decreases the explained variance in higher order modes, but increases the amoung explained for the leading two modes. 
However, correlations between mean height and variance PCs are of roughly the same magnitude for leading two modes, but are lower for higher order modes, in opposition to the trend found in explained variance.

There is a similar pattern in seasonal data for the modes, though the difference in explained variance is likely insignificant. Generally, greater lag has lower correlations between the two corresponding PCs (for mean height and variance fields), though the 5-day lag doesn't appear to be significantly different from the zero-lag for the leading PC. The second PC, which generally has higher correlations between variance and mean height PCs than the leading PC, has considerable differences in lagged analyses in all seasons except SON.

Generally, correlations steadily decrease with increased lag in all seasons except JJA, which is highly correlated, magnitude of 0.41, with zero-lag but has minimal correlation with 5- and 10-day lagged analyses, ~0.05. 

##### Emergence of ZW3 in Leading Modes

Interestingly, no ZW3 pattern emerges in any of the 5 leading modes from MCA with daily data. However, aside from the leading modes, higher order modes from the monthly data MCA were all ZW3-like in nature.

There are higher order modes in the daily data analysis, not directly associated with ENSO, with zonal wave signals or Rossby wave trains; sequential highs and lows in the subtropics with wave numbers of four and above. 

- No ZW3 patterns obvious in daily (with 15 day average), but instead ZW4 and ZW5 seem apparent, as well as atmospheric wave trains.
