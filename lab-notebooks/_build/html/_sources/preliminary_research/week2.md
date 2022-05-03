# Week 2

This lab notebook belongs to a set of [preliminary research](../preliminary_research.md).

## 2022 Mar 7

(Trenberth1991)=
### Storm Tracks in the Southern Hemisphere {cite}`trenberth_storm_1991`

````{sidebar}
```{note} Understanding Physics of Storm Tracks
"geostrophic theory and perturbation analysis applied to baroclinic systems" is a direct quote. Need to understand this better in order to paraphrase it. Look into this and baroclinic theory.
```
````

Trenberth summarises behaviour of key atmospheric characteristics associated with storm tracks taken from observations and forecasting from ECMWF 1979-89 dataset. He performs this analysis by calculating variance and covariance of several core variables available from the ECMWF dataset that can characterise storm track behaviour. He firstly identifies the principal location of the storm track in the NH and SH using maximum variance in geopotential height and notes some of the key differences in their respective seasonal behaviour & variability. He goes on to discuss other key characteristics associated with the storm track such as zonal and meridional flow, u and v respectively, divergence, delta, and vorticity, zeta. He suggests that some covariance measures between specific properties can be used as proxies for transport of momentum, heat etc. He finds that storm tracks are strongly linked to the tropospheric polar jet stream. Trenberth also suggests the schematic he provides of key variables and their meridional location of maximum variance can largely be explained by traditional "geostrophic theory and perturbation analysis applied to baroclinic systems".

- u = zonal velocity component
- v = meridional velocity component
- omega = vertical velocity component
- q = speific humidity

#### Questions to be answered

- What is the storm track?
    - Storm tracks are areas, generally across a discrete latitude band, with a high incidence-rate of storms. It is associated with the tropospheric polar jet stream, as this is an area with particularly high baroclinic instability. Storms tend to form from baroclinic instabilities in the mean flow, which is at it's highest close to the polar jet. This is due to the combination of the meridional temperature gradient driving winds upwards toward the tropopause and equatorwards, and the Coriolis effect forcing thermal winds in an easterly direction. This effect causes high-tropospheric winds to reach a maximum around 60 degrees from the equator, where the polar jets are found. Instabilities in the polar jets propagate downwards to the surface level (_find citation_).

- What will be the difference between my analysis and Trenberth's? Is it the dataset?
    - He uses ECMWF 1979-89 data in his study. Our study will use a more up to date dataset (ERA5 reanalyses) over a longer time period, therefore a more comprehensive and reliable study. The data that he used was limited by the data observations and a large portion of some fields (e.g. moisture and divergence in particular are named) have a "significant model element", in that they are computed through forecasting models.

- What are the methods he uses to describe storm tracks?
    - Trenberth uses variance and covariance of several characteristics common to climate datasets, such as height of a given geopotential surface, zonal and meriodional wind speeds, temperature, divergence, vorticity, specific humidity and vertical motions.

- What factors influence the position and topology of the storm track?
    - Meridional temperature gradient is the key driver of latitudinal position, due to its effect on the position of the tropospheric polar jet stream and its associated low-level baroclinicity.

- How is the storm track linked to SAM?
    - The storm track is driven by the meridional temperature gradient, which forms a pressure gradient driving thermal winds equatorwards. The changes in average pressures over the Antarctic region therefore affects the position of the storm track, as the weaker the temperature (pressure) gradient, the closer the jet (hence the storm track) is to the pole.

- How is the storm track linked to ENSO?
    - Sea surface temperatures (SSTs) are a major driver in the formation and propagation of storms (see {cite}`hoskins_new_2005`, extended notes found [here](Hoskins2005), and {cite}`trenberth_progress_1998` papers, extended notes found [here](Trenberth1998)), hence ENSO in its manifestation of high/low SSTs, depending on which phase of the cycle it is in, is a prominent forcing on the storm track.

```{note}
Need to better understand how SSTs and pressure gradient affect the storm track.
```

#### Points of Interest

- Trenberth suggests that the meridional temperature gradient in the SH is just as strong in the summer as it is in winter. Why would this be?
    - He states that Antarctica is a big enough heat sink to modulate the temperature between seasons. There is a slight decrease in gradient in summer, however nowehere near as significant as in the NH. There are also local variations where temperature gradients on the local level are in fact greater in summer than winter (see {cite}`hoskins_new_2005` paper, extended notes found [here](Hoskins2005))
- Trenberth uses covariance of some characteristics as a proxy for measuring the transport of heat, moisture and momentum:
    - covariance of u and v considered to be horizontal momentum transport
    - covariance of v and T considered to be meridional heat transport
    - covariance of u and omega and v and omega considered to be vertical momentum transport
    - covariance of v and q and omega and q considered to be moisture transport


#### Methodology

- Uses a 2-8 day band in order to retain maximal variance, whilst removing some of the variability associated with the diurnal cycle.
    - A 2-8 day band reportedly retains 20-30% more variance that Blackmon 1976 2.5-6 day band.
- Uses positional and spatial distributions of variance and covariance of several characteristics common to climate datasets, such as height of a given geopotential surface, zonal and meriodional wind speeds, temperature, divergence, vorticity, specific humidity and vertical motions.


#### Questions that follow

- What is the Eliasson-Palm flux and what does it represent?
    - Trenberth seems to use E-P flux as a proxy for representing eddy fluxes of several characteristics of storms
    - "the divergence of the E-P flux can be interpreted as the forcing on the westerly mean flow"
- What are the strengths and weaknesses of Trenberth's analysis?


## 2022 Mar 8

```{note} __On the Trend, Detrending and variability of nonlinear and nonstationary time series, PNAS online__
<https://www.pnas.org/doi/10.1073/pnas.0701020104>

Describes the Empirical Mode Decomposition method (EMD) for how to intrinsically identify trends in a given set of (potentially) nonlinear and nonstationary time series data. 

This could be used in analysis of trends over time to be found in the time series of SAM indices or ENSO3.4 indices.
```


(Shaw2016)=
### Storm track processes and the opposing influences of climate change {cite}`shaw_storm_2016`

This review article introduces a few new phenomena that I have yet to understand, such as stationary eddies, eddy-driven jets and the affect of Sea Surface Temperatures (SSTs). Although the article doesn't really provide answers, it references other publications that may hold clues. It also has a very useful description of factors influencing the behaviour of storm tracks (although there is more of a focus on NH), as well as a description of competing influences over how the storm tracks might be affected by climate change. These are based on the ERA-interim dataset, and analysis made prior to the release of ERA5-reanalyses.


Suggests that I have got the direction of shifting storm track due to changes in baroclinicity is the wrong way round... why?


#### Questions to be answered

- What are the factors that determine storm track location, intensity and variability?
    - "Seasonality of insolation" - the varying levels of solar heat absorbed with seasonal changes i.e. lower insolation during the winter which is particularly extreme at high latitudes. Poleward energy transfer (of which storms play a significant role) is greatest during winter when the strongest temperature gradient exists. Interestingly, the shifting of the jet stream is much more pronounced in the NH. [Trenberth 1991](Trenberth1991) suggests that this is because the Antarctic provides a constant heat sink that doesn't much change between seasons due to it being mostly land, whereas there is significant melting of sea ice in the Arctic.
    - Strong Hadley circulation weakens the meridional temperature gradient, resulting in an equatorwards shift.
    - Baroclinicity affected by vertical temperature gradients, therefore important in  understanding storm track behaviour... why?
    - Reduced baroclinicity also results in an equatorwards shift.
    - Warm ocean currents (SSTs??) increase baroclinicity, resulting in passing eddies being amplified, increasing their intensity, hence is intimately connected with interannual and decadal ENSO cycle.
    - Stationary eddies tend to destroy baroclinicity downstream... why?
    - Annular modes i.e. SAM, result in north-south displacment of the eddy-driven jet and changes in jet intensity.
    - SH Storm track has migrated polewards with ozone depletion, as formerly predicted. This is due to lower stratospheric cooling in the Antarctic, thus increasing upper tropospheric baroclinicity hence the polar jet which in turn propogates instabilites downwards to the surface. _Don't understand why reduced ozone leads to less stratospheric cooling... does this mean heat transferred from upper troposphere to the stratosphere?_

- How do storms transport heat polewards?
    - Claims that storms transport high amounts of high polewards through moist convection processes. Latent heat released during large convection events associated with cyclones/storms (low pressure centres) accounts for fully 50% of heat transfer polewards.


#### Points of Interest

- Pacific storm track intensity drops in mid-winter despite strong baroclinicity... why?


#### Follow-up Questions

- What are stationary eddies?
- What is the eddy-driven jet?
- Storm tracks converge momentum over mid-latitudes, maintaining westerlies against surface friction, in agreement with Trenberth... why?


## 2022 Mar 9

### Formation of Extratropical Cyclones

Extratropical cyclones are cyclones that form outside of the tropics, often referred to as lows or depressions. According to the Norwegian cyclone model, they form along a frontal boundary (between cold and warm fronts) where a temperature discontinuity is found. They are generally preceded and tailed by high pressure systems or highs. They form from broad areas of low pressure and, once an upper tropospheric disturbance intercepts the frontal boundary (_what impact does this have?_), the low sharpens resulting in a clockwise local circulatory pattern as cold and warm fronts rotate around the low and become more defined with the deepening low pressure. Eventually the cold front catches up with the warm front and becomes occluded, resulting in vertical motion of the warm air. After some time, the low moves deeper into the cold front, and into barotropic conditions, becoming disconnected from the original temperature discontuity which fuelled its formation, where it begins to decay.


## 2022 Mar 10

Data preprocessing and calculation of seasonal variance.
Climate Data Operators (CDO) bash commands were used. They were developed specifically for frequent operations performed in climate data analyses.

### Data Preprocessing

Downloaded sub-daily (12-hourly) files and monthly files. Regridded the files to one degree resolution, deseasonalised them by subtracting the monthly mean-through-time on the monthly files, and daily mean-through-time of the daily files. An extra step was added for the daily files, a smoothing operator was applied to remove the noise-like behaviour of daily mean-through-time. A bandpass filter was applied to the monthly file to check whether the command works. The daily files will have to wait for this step for more CPU and RAM to become available.


Example Script:

```
# Remaps data conservatively, retains information from surrounded higher resolution cells by including them in calculation of lower resolution value, by weighted mean.
# gridspec.txt holds the grid specification to map the input file to.
cdo remapcon,gridspec.txt era5_h500_daily_2011_2021.nc era5_h500_daily_2011_2021_1deg.nc

# Merges several files of the same variable with different timesteps, the files must have the same structure.
cdo -b f32 mergetime era5_h500_daily_1979_1990_1deg.nc era5_h500_daily_1991_2000_1deg.nc era5_h500_daily_2001_2010_1deg.nc era5_h500_daily_2011_2021_1deg.nc era5_h500_daily_1979_2021_1deg.nc

# Takes the mean of the time series of each day
cdo ydaymean era5_h500_daily_1979_2021_1deg.nc era5_h500_daily_1979_2021_1deg_seas_mean.nc

# Uses a 9-point weighted mean to smooth the daily mean-through-time, the datum has a weight of 1.0, the four sides have a weight of 0.5, and the four corners 0.3.
cdo smooth9 era5_h500_daily_1979_2021_1deg_seas_mean.nc era5_h500_daily_1979_2021_1deg_seas_mean_smoothed.nc

# Subtracts the smoothed daily mean-through-time from the original datset.
cdo ydaysub era5_h500_daily_1979_2021_1deg.nc era5_h500_daily_1979_2021_1deg_seas_mean_smoothed.nc era5_h500_daily_1979_2021_1deg_deseasonalized.nc

# Bandpass filter of 2-8 days, the two numbers following the 'bandpass' operator are 2- and 8-day frequencies (per year).
# The bandpass filter operates on a 365-day cycle therefore February 29th is removed from all leap years before applying the filter.
cdo bandpass,45.6,182.5 -del29feb era5_h500_daily_1979_2021_1deg_deseasonalized.nc era5_h500_daily_1979_2021_1deg_deseasonalized_bandpass.nc
```

### Seasonal Variance

Variance in geopotential height over monthly time series, saved as era5_h500_daily_1979_2021_1deg_month_var.nc.

```
# Calculates variance of every month, first takes monthly mean from daily data 
cdo ymonvar era5_h500_daily_1979_2021_1deg.nc era5_h500_daily_1979_2021_1deg_month_var.nc
```

## 2022 Mar 11

### Wallace & Hobbs, Ch.10: Climate Dynamics {cite}`wallace_10_2006`

"When the annular modes are in their high index polarity, the storm tracks and associated westerly wind belts are shifted poleward of their climatological-mean positions, and vice versa." SAM in a positive phase has lower than average pressures over Antarctica and higher than average over mid-latitudes, leading to a reduced pressure gradient. In line with the thermal wind relation, this results in  weaker winds and a shift polewards.

#### ENSO

ENSO is an internal mode of variability on a decadal timescale. It is characterised by higher than average SSTs in the eastern Pacific and lower than average SSTs in the western Pacific. This leads to a weakening of the easterly trade winds, as the east-west pressure gradient is weaker in ENSO years, followed by a relaxation (deepening) of the thermocline, reducing the amount of cold nutrient-rich upwellings in the east Pacific hence a reduction in productivity of the Pacific biosphere. The relative warming in the east Pacific also increases the sea level there.

### A Comparison of Southern Hemisphere Cyclone Track Climatology and Interannual Variability in Coarse-Gridded Reanalysis Datasets {cite}`eichler_comparison_2013`

This paper compares three reanalysis datasets on storm track behaviour and it's relations with ENSO, SAM and the Indian Ocean Dipole (IOD) in terms of intensity and frequency of storms. Less intersetingly to us, it finds that temporal limitations in some of the reanalysis datasets (1979-2010),  changes in data assimilation techniques and the inferiority of pre-satellite data make the comparison less significant, and some of the observed storm track behaviour is attributed to these deficiencies. However, there are some convincing trends across the datasets that allow for more secure inferences into storm track behviour and its associated drivers. 

They use a specific latitude band to investigate individual storm intensities and frequencies, differing from our proposed variance-field method. _It would be interesting to know if we can derive storm frequencies from our chosen analysis method._

Eichler and Gottschalk find that patterns consistent with the Pacific South American, equatorial Africa and East Indian Ocean patterns (see {cite}`trenberth_progress_1998` papers, extended notes found [here](Trenberth1998)) are strongly linked to variability in storm track bevhaviour in El Nino and positive IOD (and their respective opposing phases). These patterns are driven by anomalous convection in the tropics driven by the anomalous SSTs found in El Nino and positive IOD years. 

Most convincingly of all however, is the strong correlations between SAM phases and the variability in the storm track, suggesting that SAM phases are likely responsible for a significant amount of storm track variability.

#### Data Used

Eichler and Gottschalk provide a brief description of the data that they use, including ERA40, NCEP1 and NCEP2 datasets. They identify key deficiencies in their data, namely:
    - coarse spatial gridding
    - differences in assimilation techniques between reanalyses
    - short temporal period for chosen datasets 
    - use of pre-satellite data (pre-1979)

_Identify why ERA5 reanalysis will be better_

#### Methodology

- Counted individual storms in a particular region, identified intensity and frequency of those storms.
- Uses SAM index, ENSO3.4 and IOD data from previous paper (_ref. 35_)
    - We will use Southern Oscillation index (SOI) and (possibly) first coefficient of PCA.

#### Climatology

Highest frequency of storms were found in the southern Indian Ocean, stretching eastward to south of Australia, with the peak found just of the coast of Antarctica. This is attributed to the high baroclinic instability found in that region (Hodges et al. 2003, Murray & Simmonds, 1991). However, peak frequency band is located 10 degrees poleward of highest intensity band, where the most intense cyclones are located, as found in [Hoskins & Hodges 2005](Hoskins2005). It was suggested by Hoskins and Hodges that this is because areas towards the equator are associated with cyclogenesis, whereas polewards are areas of cyclolysis or decay.

The positive trend in SAM is linked to a reduction in cyclone frequencies in mid-latitudes and an increase in high latitudes ([Pezza et al., 2008](Pezza2008), Mendes et al., 2010).

#### Interannual Variability

To assess effects of ENSO, discrete years were identified with particularly strong El Nino or La Nina events, and composited together. Then the difference in frequency and intensity was calculated by El Nino minus La Nina years. Patterns were identified that are consistent with the patterns identified in other papers (Cai et al., 2011, Garreaud & Battisti, 1999) that outline the PSA. This is linked to Rossby wave trains that are initialised by the anomalous convection in the tropics.

```{note}
See paper for visualisations and descriptions of these patterns.
```

_Find out about Rossby wave trains._

A similar process was followed to identify the effects of IOD, with the difference between positive and negative phases identified. This lead to patterns similar to those seen in the ENSO composites, indicating that the ENSO and IOD are closely correlated.

SAM composites show interesting results, with a particularly strong correlation to storm track behaviour. The following was observed:
- Positive phase: fewer but more intense storms
- Negative phase: more but less intense storms

This follows from Simmonds, 2003, who found no strong correlation between sea level pressure (SLP) and cyclone intensity.

_This is something that could be investigated, why would this be the case?_

Eichler and Gottschalk also use partial correaltions of ENSO, IOD and SAM to eliminate external forcings from each respectively, more robustly quantifying the correlations specifically between each and storm track behaviour.

#### Questions that follow

- What are Rossby waves?
- What are Rossby wave trains?
- How does anomalous convection in the tropics affect global circulation patterns?
- What are the pros and cons of using ERA5 reanalysis?
