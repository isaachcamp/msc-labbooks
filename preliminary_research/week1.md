# Week 1

This lab notebook belongs to a set of [preliminary research](preliminary_research.md).

# 2022 Mar 2

## Overview
Read papers on Southern Annular Mode (SAM).

(Renwick2006)=
## Southern Annular Mode & New Zealand Climate {cite}`renwick_southern_2006`

This is a short article providing a brief outline of what the SAM is (how it physically manifests) and what the trend was in 2006 . 

### Summary

The SAM is a seemingly unpredictable phenomena which flips between two phases - positive & negative. The positive phase is identified by lower than average pressure over the Antarctic, and higher pressures over higher latitude bands around 40-50S (over the south island of New Zealand). This results in light westerly winds and more predictable weather over New Zealand latitudes, and stronger westerly winds over the Southern Ocean (50-70S). The negative phase is associated with the reverse, with weather around New Zealand more unsettled. 

```{note}
A phase shift can only be known a few days in advance, but the ensuing phase could last for several weeks.
```

Recent trends show that the SAM is more frequently in the positive phase, which indicates this might be something to expect in the future. 

There is strong evidence that the SAM phase is influenced by the ozone hole and the stratosphere (as detailed in [Thompson et al. 2011])(./week3.md) (Week 3 notebook). There are also strong ties between the SAM and storm tracks.

### Questions
- What are the current trends? (this was written in 2006)
    - Are the pressure differentials becoming more extreme? 
- What causes SAM?

```{note}
See [Thompson et al. 2011])(./week3.md) (Week 3 notebook) for answers to both questions.
```

(Fogt2020)=
## The Southern Annular Mode: Variability, trends, and climate impacts across the Southern Hemisphere {cite}`fogt_southern_2020`

This is a review article of the SAM, causes of its variability, and it's connections to other phenomena. It has a description of three types of SAM indices and a brief outline of some of the pros and cons - should be useful for determining how to characterise SAM.

If required, this article will help direct research in what influences the SAM phase and intensity (such as stratospheric connections, ENSO, Rossby wave breaking).

### Questions to answer

- What is the SAM?
- How does it affect Southern Hemisphere (SH) climate?
- What connections does it have to the wider SH circulation?

### Summary 

The SAM is a natural pattern of atmospheric circulation, an "internal mode of climate variability". In other words, humans have not caused the manifestation of this phenomenon. However, external (anthropogenic) forcings are causing the intensity and polarity of SAM phases to change. The primary forcing is ozone depletion, with greenhouse gas emissions and tropical sea surface temperatures having smaller impacts. This is generally driving the SAM into its positive phase for longer and more intense - possessing a greater SAM index value - periods. SAM is the largest contributor to atmospheric climate variability in the SH, at around 22-34%.

SAM practically covers the entirety of the extratropical SH. It effectively represents the pressure gradient between mid- and high-latitudes, and indicates the meridional position of the polar jet stream. It is largely zonally symmetric (symmetric across longitude bands) predominantly due to the lack of land mass effecting momentum transfer in the high latitudes of the SH. The poleward contribution of eddy momentum fluxes to the polar jet stream induces this symmetry, whereas other connections produce the spatial asymmetry that is observed, such as sea-surface temperature variability - linked to ENSO - and zonal wavenumber 3 (Fogt, Jones et al. 2012).

### Methods for Calculating a SAM Index

There are three methods outlined in this paper, the first of which is the method used by the author (may contain some bias in the claims of its effectiveness):
- First principal component of mean sea-level pressure (MSLP) or geopotential height from a regular gridded dataset.
    - It is claimed that this captures the zonal asymmetry inherent in SAM, whereas the following two methods do not.
- Difference of standardized zonal mean pressure between 40S and 65S (Gong & Wong 1999).
    - 40S and 65S chosen as they encapsulate the strongest anti-correlation (inverse) between the two oppositely signed pressure differentials.
- Similar to above, except that it uses pressure observations taken at stations at approximately 40S and 65S (Marshall 2003).

### Questions

- How does it affect storm tracks? Is it the governance over the location of westerly winds?
- What are the connections between SAM and ZW3? How does ZW3 cause asymmetry in SAM? -- Check out Fogt, Jones et al. 2012.

# 2022 Mar 3

## Overview

Formed a basic understanding of how global circulation patterns & phenomena arise. Read papers on storm tracks, tried to decipher what causes storm tracks and what characterises them. 

```{note}
See [Week 2 notebook](week2.md), Trenberth 1991 paper for more info on storm tracks and characteristics.
```

## Basics of Global Circulation

### Temperature Gradient

Global circulation patterns occur firstly because of the heating differential from the Sun. Locations at higher latitudes receive less heat due to their high angle of incidence, as well as the increased amount of atmosphere that must be penetrated due to this high angle, resulting in a higher absorption of insolation in the atmosphere and less surface heating. This creates a temperature differential between the equator and the poles that drives air circulation polewards. 

### Circulation Cells

The polewards circulation does not happen in one uniform circulating cell, but is split into three main cells: Hadley cells, Polar cells; and Ferrel cells. These cells are the predominant heat transport mechanisms.
- Hadley Cells:
    - Located between the equator and 30 degrees
    - Warm air rises at the equator (low pressure band), spreads out at the tropopause and cools, and sinks at 30 degrees (high pressure band)
- Polar Cells:
    - Located between poles and 60 degrees
    - Warm air rises at 60 degrees (low pressure band), spreads out at the tropopause and cools, and sinks at the poles (high pressure band)
- Ferrel Cells:
    - Located between 30 and 60 degrees
    - Different to the Hadley and Polar cells in that the direction of circulation is reversed.
    - The work of these cells results in semi-permanent areas of high and low pressure.

```{note}
Ferrel cells are different in another way too; they are not driven by temperature, but are in fact driven by strong eddies created by the polar and subtropical jets (or Baroclinic instabilities and baroclinic waves?).
```

### Coriolis Effect

The Coriolis effect is a result of the rotation of the Earth. This rotating reference frame creates a virtual force to an observer assuming a stationary reference frame. 

The Coriolis force causes winds to be deflected to the left of their direction of motion (in the SH, it is reversed in the NH). This is due to the speed of rotation being greater at the equator than it is at the poles. This action means that by the time winds reach 30-40 degrees from the equator, they are largely moving in a westerly direction, creating the trade winds observed around these latitudes (southerasterlies in the SH).

### Jet Streams

As hot air rises and moves polewards, it migrates under the influence of the coriolis effect. This forces the rising air to travel in an easterly direction. Due to conservation of angular momentum, the speed of the winds originating at lower latitudes increases as they move polewards, reaching a maximum around 30 degrees in the Hadley cell, and around 60 degrees in the Polar cell, at which point they have almost lost their meridional velocity component. At these locations are found the jet streams, sub-tropical (between Hadley and Ferrel cells) and polar (between Polar and Ferrel cells). Jet streams are located at the top of the troposphere and are extremely strong winds, reaching up to 400kph.

The interactions between the upper-troposhere jet streams and surface pressure systems is complex. Surface-level pressure systems can influence where the jet streams are found and vice-versa. The jet streams are also not a simple uniform band structure, but wander between meridians, have areas of higher winds and lower winds. They also migrate with the seasons, moving equatorwards in the winter and polewards in the summer as the total insolation varies. In the Southern Hemisphere (unsure about the NH) there will be present only a single jet during summer, around 45 degrees, but during winter there are two distinct jets (_find citation_).

Following information obtained from Lower-Tropospheric Processes chapter in Synoptic Analysis and Forecasting by Milrad (2018) {cite}`milrad_lower-tropospheric_2018`:

Jet streams are in a large part driven by temperature gradient. The height of the troposphere is proportional to the temperature due to the corresponding density being greater at colder temperatures. Hence the height of the tropopause is lower at high latitudes than it is at the equator. 

```{note}
This is often why isobaric surfaces are preferred to altitude as it is a constant measure, whereas altitude of atmospheric characteristics varies with latitude. 
```

The height difference results in varying layer thicknesses between two isobaric surfaces. This is important when it comes to powering the jet streams. A higher temperature gradient increases the thickness of a layer and results in a higher pressure gradient between latitudes. Thus as the overturning circulation travels northward, the stronger the gradient the stronger the jet streams will be. This process is described by the thermal wind relationship {cite}`ams_thermal_2012`:

```{math}
  \begin{equation}
    \frac{\partial u}{\partial \ln p} = \frac{R}{f} \bigg( \frac{\partial T}{\partial y}\bigg)
  \end{equation}
```


# 2022 Mar 4

## Storm Track Dynamics chapter in The Global Circulation of the Atmosphere {cite}`swanson_storm_2007`

This book chapter provides a review of the understanding of storm track dynamics in 2007. By comparing simplistic models to models of increasing complexity, Swanson attempts to diagnose how some of the observed charateristics can be explained by current theoretical models and which remain beyond the scope of understanding. It details some of the theoretical models used to describe storm characteristics, such as path length and lifetime, firstly through the use of linear dynamics, stochastic models, finally addressing the influence of non-linear dynamics. This chapter will help to form a more comprehensive understanding of storm dynamics. It also suggests the bandpass filtered statistical method is preferred over tracing the path of individual storms.

```{note}
Transient is used synonymously with storm.
```

### Questions to answer

- What causes the storm track?
- What factors influence the position and topology of the storm track?
- What factors influence the storm characteristics?
- What are the trends associated with storm characteristics?
- How is the storm track linked to SAM and ENSO?

### Summary

Storm tracks show tremendous variability over intra- and interannual timescales.
The storm track is driven by the temperature gradient that causes baroclinic instability, also by asymmetries in sea surface temperature fields.
Linear theories attempt to link storm tracks to basic state flow.


(WallaceHobbs7)=
## Atmospheric Science: An Introductory Survey, Ch.7 Atmospheric Dynamics {cite}`wallace_7_2006`

Gives a general overview of key concepts and associated "primitive" equations that, when used together, give rise to a general circulation model that accurately describes observed large-scale circulations. The key equations include:
- horizontal equation of motion
- hypsometric equation
- thermodynamic energy equation
- continuity equation
where the final three equations govern vertical motion.

### Questions

- What is vorticity? What are its implications?

### Key Assumptions

- Large-scale: 
    - Horizontal scale on order of a few hundred kilometres.
    - Vertical scale on order of the depth of the troposphere.
    - Time scales of a day or longer.
- System in hydrostatic balance.
- Adiabatic processes.
- Vertical component of velocity vector is more than three orders of magnitude smaller than horizontal component.

### Key Equations

$$
    \begin{eqnarray}
      Vorticity, \zeta   & = & \nabla  \times  V \\
      Divergence, Div_H V & = & \nabla  .  V
    \end{eqnarray}
$$
