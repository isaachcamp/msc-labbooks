# Week 3

This lab notebook belongs to a set of [preliminary research](../preliminary_research.md).

## 2022 Mar 14

(Hoskins2005)=
### A New Perspective on Southern Hemisphere Storm Tracks {cite}`hoskins_new_2005`

This article provides a detailed method for tracking storms using a number of upper and lower tropospheric variables including vorticity at a given geopotential height, in this case predominantly 250hPa and 850hPa, potential temperature and MSLP. This analysis method is used to investigate a variety of storm characteristics such as genesis/lysis (growth/decay), length of storm (lifetime), track, as well as mean attributes, such as intensity, growth/decay rate, speed. It also uses a similar method to Trenberth 1991, in that it uses Euler variance methods on a band-filtered dataset (2-6 days), although repeatedly makes reference to the limitations of this method.

#### Major Findings 

A few new insights are made which alter the picture of the storm tracks seasonal structure and position, as well as the impacts of interpaly between subtropical and polar jet streams at lower and upper tropospheric levels. It suggests, from vorticity fields at 250hPa and 850hPa using both centre-tracking and variance methods, there is a spiral structure in winter and a ring-like circumpolar structure in summer. This is at odds with the papers that I have read before (or at least I didn't notice this), in that the storm track remains annular but migrates between latitudes.

The winter storm track spirals in towards Antarctica. According to the vorticity analysis of individual storm systems, during winter there are two distinct storm track regions: one at a higher latitude in the Atlantic and Indian oceans, associated with the polar jet; the other at lower latitudes in the Pacific, associated with the subtropical jet.

The most intense storms are found during summer and exclusively in the Atlantic and Indian ocean regions, this is caused by the enhanced SST gradient between 35S and 55S during summer. 

The Andes have have two strong regions of cyclogenesis, one located on the downstream side of a region of perticularly strong cyclolysis, the other further north, unconnected to a region of cyclolysis on the other side of the Andes, that is associated with low intensity subtropical jet systems.

Claims that the asymmetrical spiral pattern observed in winter is driven by a positive feedback loop. Storms drive zonal winds, which strengthens SST gradients, which is beneficial for storm track activity.


#### Data & Techniques

Uses ERA-40 data, including data from pre-satellite era. Paper includes an appendix arguing for consistency of their findings pre- and post-satellite era.

Hoskins and Hodges suggest there are complications with seasonal analysis, including:
- lag in temperature response of 44 days (much higher than NH lag at 33 days) - _why is this important?_
- semi-annual oscillation in the latitude and strength of circumpolar pressure trough - _why is this important?_


#### Eulerian Variance Method

Uses vorticity to identify the differing seasonal structures as outlined above. Uses the 250hPa field to achieve this, although I'm unsure why they don't use the 850hPa field here, as they seem to be trying to make connections between the upper and lower troposphere, perhaps the vorticity doesn't translate down to the surface?

The storm track shifts only slightly with the seasons, moving cloer to the pole in winter, in accordance with previous studies. They also find that wind speed maximums at 850hPa are collocated with maximum SST gradients, suggesting a strong linkage. The same cannot be said of MSLP and SST gradients however.


#### Referenced Papers

- Berbery & Vera, 1996, found consistency between the storm track and baroclinicity of the mean flow.
- Nakamura & Shimpo, 2004, and Inastu & Hoskins, 2004, found a strong link between Atlantic and Indian storm track and enhanced SSTs, the latter by using specific experiments with GCMs. This is what causes the higher intensity sotrms found in this region.
- Vera et al. 2001 identified subtropical synoptic-scale waves at 300hPa. They used an extensive EOF study on variance fields to establish this, referenced here because this is somewhat unusual for a study on variance fields alone (one of the key weaknesses that Hoskins & Hodges identify).


#### Weaknesses of Variance Method Compared to Centre-Tracking

- Vorticity & Potential temperature (theta) show maximum average intensities associated with the subtropical jet, which is not apparent when using variance methods.
- Variance methods do not identify subtropical synoptic-scale waves at 300hPa, other than Vera et al. 2001. 
- Do variance methods have a way of analysing storm frequency? Most papers find little correlation between frequency and intensity, therefore the two must surely be considered separately.


#### Questions to be answered

- Why choose 2-6.5 day band instead of Trenberth's 2-8?
    - No real answer provided, other than suggesting that storms systems that it investigated reliably lasted 5-6 days (but couldn't this be skewed by the fact they filtered out storms above that time, or did they use the individual storms that they had tracked?). I think it would still be useful to extend the band to 2-8 days, if only to remain on the conservative side.
- What characteristics comprehensively characterise storms?
    - This paper looks specifically at vorticity, genesis/lysis, lifetime and track, as well as the variance in geopotential height. This is a reasonably comprehensive list, though Trenberth 1991 goes much further with the analysis of variance fields.
- What is vorticity and what are its implications?
    - Vorticity is essentially the curl of the horizontal velocity field, effectively a wind shear across the direction of travel, as well as the rotational motion associated. The implication being, this is a reasonable variable for characterising storms, as storms have high wind spreeds associated with them, hence will have high values of vorticity due to turbulent flow. _Or are the scales too small for turbulent flow to be improtant for vorticity fields?_


#### Questions that follow

- Is using the variance method alone enough to characterise storm track trends? Or trends of individual storms?


(Pezza2008)=
### Southern Hemisphere Synoptic Behavior in Extreme Phases of SAM, ENSO, Sea Ice Extent, and Southern Australia Rainfall {cite}`pezza_southern_2008`

This paper looks to identify the main causes of precipitation over two Australian cities by studying the effects of storm frequency and intensity, as well as the external drivers of storm tracks such as ENSO, SAM and sea ice extent (SIE). This paper has a strong focus on the effects of the sea ice extent and distribution, therefore not so useful, but can corroborate findings from other papers.

They suggest that the midlatitude drying pattern (lower rainfall) is partially associated with the positive SAM trend (_find citation_).


#### Major findings

When SOI is positive, there is an increase in cyclone frequency and intensity in the Tasman Sea and around New Zealand, whereas activity around Antarctica and South America is lower. 

When SAM is positive, there is an increased activity around Antarctica, whereas when in its negative phase, there is higher activity in the mid-latitudes (read: storm track migrates polewards in positive phase).


#### Questions to be answered

- What is the extent of their study?
    - Not extensive, look at SAM, ENSO, sea ice extent teleconnections with storm activity, specifically connections with rainfall over Perth and Melbourne.
- What is their methodology?
    - They take the five most positive and negative events of each phenomena's related index, such Southern Oscillation Index (SOI) and Antarctic Oscillation index (AAOI). They composite proxies for cyclone frequency and intensity for these events and minus negative from positive to identify strongest changes between the two event types. They use partial correlations to focus on the direct effects of each phenomena, using spatial correlations to identify any teleconnections to cyclone activity over Perth and Melbourne.
- What is the importance of this paper?
    - Reinforces what is known about SAM and ENSO effects on storm track behaviour. Should be used as a reference to back up argument.


#### Referenced Papers

- L'Hereux & Thompson, 2006, found that a significant portion of variance in SAM was related to ENSO (up to 25%?)


## 2022 Mar 15

(Trenberth1998)=
### Progress during TOGA in understanding and modeling global teleconnections associated with tropical sea surface temperatures {cite}`trenberth_progress_1998`

Review article that focuses on the interactions and teleconnections between the tropical convection anomalies, driven by SST anomalies associated with El Nino events, and extratropical atmosphere. It is focussed on the NH but has some mentions of the SH and much of the content seems transferrable to SH. It also contains a fairly comprehensive section of the theory of tropics-extratropics interactions including Rossby wave trains and vorticity transport, which includes the inclusion of a transient term (relating to the storm track) that plays an important role in vorticity flux. The details are beyond me for now, however will be useful in the future when I understand more about atmospheric dynamics.

```{note}
Look at Wallace & Hobbs again to understand the physical basis for atmospheric dynamics.
```

#### Major Findings

Strong convection events cause an increased Hadley overturning circulation, low-level convergence and upper-level divergence, which, coupled with the upper-level divergence at the descending branch of Hadley cell, produces the conditions for Rossby wave propagation. This paper once again reinforces the importance of Rossby wave trains in produing the teleconnection patterns observed such as the PSA. It reiterates that Rossby wave trains push the storm track equatorwards (_find citation_).

It is suggested that the storm track plays a key role in amplifying the wave trains and even control the structure, partially explaining commonality of observed features, such as the lengthening of the jet stream, despite forcing from SST anomalies that geographically distributed. The amplification is due to transient transportation of flux that enhances jet streams.

```{note}
Trenberth et al. use the streamfunction instead of geopotential height as they suggest the latter cna be influenced by strong winds in lower latitudes.
```


#### Questions to be answered

- What is the importance/relevance of the paper?
    - Role of storm tracks in amplifying the effects of Rossby wave trains as well as role in controlling the spatial teleconnection patterns observed. 
    - Explains role of Rossby wave trains in midlatitude circulation.
    - Explains some of the teleconnection patterns that are observed.


#### Teleconnection Patterns

Teleconnection patterns are not uncommon, in fact at least 13 in the NH have been documented, 6 directly related to forcings from SST anomalies. There are analogues to some in the SH, such the PSA, the southern analogue of the PNA. 

There are three classes of teleconnection patterns, as outlined in Schubert 1986 (_find citation_):
- those with timescales greater than a month.
- those with timescales between 10-30 days, in the SH these tend to be zonally orientated.
- those with timescales less than 10 days, prominant over midlatitude oceans.


#### Variability and Effects of Storm Tracks

Cyclone waves (storms) are particularly active downstream & polewards of the time-averaged jet streams, also that he initiation and propagation of cyclones are governed by zones of preferential cyclogenesis, and steered by stationary mean flow (Trenberth 1991).

Convergence of vorticity that occurs in the storm track enhance the upper tropospheric jet (in the NH, unsure of whether this is true of SH), whereas heat flux by the same mechanism serves to disspate the same mechanism. However, the magnitude of vorticity flux is greater than heat flux, therefore the action of storm tracks serves to reinforce zonally asymmetric mean flow in the upper troposphere (Lau & Holopainen 1984). In the lower troposphere, stationary waves are in fact dissipated by storms(... why? Is it due to the heat transport being greater at surface level, burning up the fuel of the waves?)

"Recent investigations", not so recent now, indicate that storm tracks have a key role in amplifying Rossby wave trains as well as controlling the observed structures. Specifically, it was suggested that low-frequency structures (what are these?) may preferentially select storm track flux patterns that create a positive feedback with wave trains, because they are dynamically favourable (Branstator 1995).  Hoerting & Ting 1994 suggest that the storm track plays a role in the consistency in geographical location of an elongated jet stream that is observed in association with El Nino warm events, despite the SST anomalies being distrbuted in space.


#### Referenced Papers

- Horel & Wallace 1981 and Pan & Oort 1983, found that latent heat released from large convection events warmed the upper troposphere causing enhanced Hadley circulation & subtropical westerlies.
- van Loon & Shea 1983 & 1985, Karoly 1989, found that the PSA is generally weaker and more variable than its NH hemisphere counterpart (PNA), exhibiting relatively weaker tropical forcing and zonal gradients.
- Kok & Opsteegh 1985, demosntrated importance of flux transport by storm tracks in producing midlatitude anomalies, specifically for the 82-82 El Nino event.


#### Questions that follow

- What are the important dynamical equations for storm tracks and tropical teleconnections? How do they affect the storm track? - Read more foundational physics textbooks.


### Signatures of the Antarctic ozone hole in Southern Hemisphere surface climate change {cite}`thompson_signatures_2011`

Makes case for strong link between ozone hole and SAM trend. Uses observations and controlled model experiments to argue that the physical fingerprint of the ozone hole is matched by that of SAM. Suggests that as the ozone recovers into the future, the SAM will trend toward negative phase, however, greenhouse gas forcing has a similar effect, though less pronounced, as ozone depletion and so will continue to push toward a positive trend.

Suggestions are made for the physical basis of the observed variability in SAM, detailed below.


#### Major Findings

The ozone hole is most pronounced during the SH summer, the physical pattern observed for ozone depletion is a good match for SAM, see below for details.

Suggests positive trend in SAM is caused by ozone depletion (supported by observations & models experiments in ref 28, 30, 31), but also that greenhouse gas forcing is pushing towards a positive trend (from experiment in ref 28). Greenhouse gases are driving the temperature gradient by heating the tropics.


#### Questions to Answer

- How does the ozone hole affect SAM?
    - Causes pertrubations to the meridional temperature gradient, creating the pressure differnces observed (exact mechanism remains unknown).
- What does this mean for the storm track?
    - Moves the position and strength of the storm track, due to it's effect on the temperature gradient.


#### Effect of Ozone Hole 

A depleted ozone leads to stratospheric cooling, although it is not fully understood how the troposphere and startosphere are connected, the stratosphere can extend all the way down to the Earth's surface during summer in Antarctica (see stratospheric geopotential height figure in paper), known as "deep vertical coupling", see ref 6-9. From the thermal wind relation, it is apparent that stratospheric cooling, increasing the meridional temperature gradient, will strengthen vertical wind shear, causing an acceleration of the stratospheric vortex.

The effect of the ozone hole is to lower the stratospheric geopotential height, Z, of the polar troposphere accompanied by an increased Z in midlatitude troposphere - just like SAM! This suggests that the positive trend of SAM is caused by 

##### Impacts on Surface Climate

Positive SAM:
- Strong westerlies around 55-70S.
- Lower temperatures on east Antarctic coast, higher temperatures on Antarctic peninsula and Patagonia.
- Higher precipitation over eastern side of Southern Alps NZ, lower precipitation on westward side.
- Increased temperature over much on NZ.

The opposite is generally true for negative SAM.


#### Variability in SAM

Variability in SAM is driven by heat and momentum fluxes of synoptic-scale atmospheric waves (are these storms?). During a positive SAM, changes in the wind field are driven by:
- anomalous poleward heat flux in lower troposphere at 60S
- anomalous poleward momentum flux in upper troposphere at 60S

It's thought that the ozone hole must in some way drive this, though exactly how is not known. There are two theories presented here:

- At the lower troposphere, the synoptic wave-driven fluxes that cause SAM variability are disturbed by the ozone hole. Synoptic-scale atmospheric waves tend to peak where the temperature gradient is strongest. The temperature gradient is perturbed by the cooling of the stratosphere, hence the atmospheric waves diffuse more heat flux. The ozone hole perturbs the surface termperature radiatively and dynamically. Radiatively in that stratospheric cooling lowers the total longwave radiation emitted back towards the surface, causing further surface cooling. Dynamic cooling is caused by atmospheric wave breaking in the stratosphere driving vertical motion toward the surface. The cooling effect occurs through adiabatic expansion and compression. 

- At the upper troposphere, numerical experiments suggest that the lower stratospheric flow, through it's acceleration by ozone depletion, causes changes to the upper tropospheric flow and momentum fluxes. Synoptic wave-breaking in the upper tropospheric flow causes a deceleration in the eastward flow that can change the meridional temperature gradient, whose effects reach down to the surface. 

```{note}
Check out atmospheric waves - what are they? how do they work?
```
 

## 2022 Mar 16

(indices-source)=
### Source of Indices Data

#### SOI 

Time series for Southern Oscillation Index taken from https://www.cpc.ncep.noaa.gov/data/indices/soi. 

Time series also available from http://www.bom.gov.au/climate/enso/soi_monthly.txt, though the two indices are different. Which one should I use?

Time series range 1979-2021 (full year, as with the ERA5 data).


#### SAM Index

Perform PCA on ERA5 500hPa geopotential height field for monthly data and use the first Principal Component (PC1), as per Hersbach et al., 2019 (_find citation_). "Based on detrended weighted (by cosine of latitude) 500 hPa geopotential height anomaly data from 20 to 90S" (Fogt & Marshall 2020). To weight the grid point just means to take into account the grid size, which varies with latitude, and equalize the variance.


#### DMI

Time series for Dipole Mode Index taken from https://psl.noaa.gov/gcos_wgsp/Timeseries/DMI/. 

Time series range 1979-2021 (missing final 3 months, periodically updated so check again at a later date).

See https://www.ncdc.noaa.gov/teleconnections/enso/soi for details on how the SOI is calculated.


#### ZW3 Index

Use Goyal 2021 method. Rishav has provided a time series of his index. Missing all of 2021, will either need to calculate this or only correlate up to 2020.


## 2022 Mar 17

### PCA Analysis, Chapter 11 from Statistical Methods in the Atmospheric Sciences {cite}`wilks_statistical_2006`

PCA is a technique used for exposing the origins of maximal variance within a dataset. It works by calculating the covariance matrix of X, a matrix formed from multiple readings through time of the vector x, and finding it's eigenvalues and eigenvectors. This essentially re-orientates the data into a "natural" coordinate system, whose eigenvectors, commonly named Empirical Orthogonal Functions (EOFs), point in the direction describing maximum variance - an "orthogonal transformation" which leaves magnitudes unchanged and retains all information provided the X matrix is nonsingular (no redundant information). The eigenvectors are organised in matrix E in descending order of variance, i.e. the first eigenvalue (and corresponding eigenvector) is the largest, explaining the most variance. The Principal Components (PCs) are essentially a mapping/projection of the original data matrix, X, onto the eigenvalue matrix, E, given by:

```{math}
    \begin{equation*}
      u_m = e_m^T x' = \sum_{k=1}^{K}e_{km}x_k' , m=1,2,...,M,
    \end{equation*}
```

where $u_m$ is the mth Principal Component, and $ x' = x - \overline{x} $, the normalised data field, or "anomalies". Using the anomalies is a vital step before PCA, else the results are essentially uninterpretable.

The elements of the eigenvector matrix are a linear combination of the elements of X. Important properties of the eigenvectors arise, specifically:
- Eigenvectors are orthogonal.
- There is no correlation between eigenvectors or principal components, they are mutually exclusive. 

PCA is frequently used in order to interpret the PCs as primary modes of variability of a given data field. This is possible because the elements of $e_km$ can be reprojected onto a map to show the locations that most contribute to the PC $u_m$, i.e. that have a high degree of variability corresponding to that principal component. Physical interpretation does have some limitations however, as detailed below.

PCA is also used for compressing data. For data with K variables, if there is any correlation between the variables there are likely to be some eigenvalues whose values are zero. Therefore the number of eigenvectors required to describe the data, M, is likely to be less than K. The data can be re-expressed in it's orignal form, or at least a close approximation, with minimal information lost. As the eigenvectors essentially represent the amount of variance in descending order, the first m eigenvectors can describe a significant proportion of the data, such that a subset of eigenvectors can be chosen (subjectively) to compress the data as much as possible with an acceptable amount of information lost. There are methods for selecting the subset, and the "acceptable" threshold of information loss, see the source reference for details. 


#### PCA of a Single Field

A 2D field can be subjected to PCA by vectorizing the field into a single column vector, x. Subsequently the number of columns in X are the number of time steps in the time-series.

#### Correlation Matrix vs Covariance Matrix

The covariance matrix is useful for identifying components of highest variability within a single field, or between multiple fields with variables of comparable magnitudes. However, the correlation matrix, which has been standardised by dividing by standard deviations (unitless), is more useful for comparing fields that have significantly different units between variables.

An example given in the book:
>"in analyzing gridded numbers of extratropical cyclones, Overland and Preisendorfer (1982) found that PCA on their covariance matrix better >identified regions having the highest variability in cyclone numbers, and that correlation-based PCA was more effective at locating the primary >storm tracks."


#### Restrictions to PCA

##### Buell Patterns 

Artefacts of the data sample space that have no physical meaning but can be key sources of variability when PCA applied to a spatial domain that is comparable to the spatial scale of variability e.g. if using a subset of data that covers approximately the same area that is covered by SAM - here SAM is the mode of variability, hence the spatial scale of the phenomena (40S-90S) would be of the order of extent of the dataset used (domain of 40S-90S).

##### Sampling Properties

PCA is exclusively conducted on a finite sample, whereas the calculation of the covariance matrix assumes that the sample is infinite, and therefore exact. However, the covariance matrix that is calculated is in fact an estimation of the true one, therefore the eigenvalues that are calculated are only estimates themselves. 

```{note}
There is a complicated explanation of the foundations of this, and how to estimate uncertainties, but which relies on knowledge of statistical distributions that I don't currently have... Need to go back to this - read some of the earlier chapters.
```

This result means that eigenvalues that are of comparable magnitude will possess well-defined corresponding eigenvectors, meaning that they may in fact encapsulate a mixture of the variance that would be explained by eigenvectors of the exact covariance matrix. Since higher order EOFs are generally closer together, these are often treacherous to interpret physically. A rule of thumb was derived by North et al. 1984 (_find citation_) to establish whether two eigenvalues can be considered distinct.

The bootstrap method cna be used to resample in order avoid the pitfalls around insufficient samples, with some caveats!


##### Orthogonality Constraint

The first Principal Component, PC1, is selected based on the maximum variance and can largely be considered linearly independent. However, all subsequent PCs must be orthogonal to PC1 by definition, this assumes that all PCs are independent modes of variability, when they may well not be. If modes of variability are not linearly independentm the PCs representing them will in fact be a jumble of variability stemming from different mechanisms/modes of variability.

As a work-around for this, it is possible to rotate the eigenvectors to a new orientation that exhibits a "simple structure" - one which maximises the number of near-zero elements and minimises the number of remaining non-zero elements that correspond to elements of another eigenvector. Eigenvectors can be rotated orthogonally, retaining their orthogonality property, or obliquely, relinquishing that property, but favourable for non-linearities. 

There are many ways to achieve a "simple structure", but one of the most popular is the varimax method, Kaiser 1958 (_find citation_).

```{warning}
This rotation does lose the property of PC1 bearing maximum variance.
```

When rotating eigenvectors, orthogonality and mutually uncorrelated PCs properties aren't necessarily retained. Depending on the scaling applied to the eigenvectors, one or the other, even both, can be lost. 
- For scaling $\lvert e\rvert=1$, orthogonality is retained. 
- For scaling $\lvert e\rvert=\lambda^{-1/2}$, uncorrelated PCs are retained. 
- For scaling $\lvert e\rvert=\lambda^{1/2}$, neither properties are retained.

For pros and cons of scaling eigenvectors, refer to reference.


#### SSA - Singular Spectrum Analysis: Time-series PCA

A method that can be used on time-series of a single variable, and can be extended to multiple time-series, known as multichannel SSA. It works by taking a rolling window vector, of chosen size, as it's x-vector. It effectively searches for signals of periodicity between "time fragments".

```{note}
This could be a useful method to apply to the time-series of our indices.
```


#### PCA in CDO

CDO automatically weights the grid points by cell size, so no need to do this step manually.
