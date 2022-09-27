# Earth System Models (ESMs)

## Demystifying Climate Models {cite}`gettelman_demystifying_2016`

### Key Concepts in Climate Modelling

ESMs aim to characterise the probability distribution of weather states (the climate) by running time integrations -- or model runs -- over a long period with realistic mechanics and constraints. The model runs should be independent, zero correlation, and predict different states at each time step, however, the probability distribution will ideally be the same for every model run.

#### Uncertainty

Models can be wrong, and the likelihood of them being wrong is quantified as uncertainty. Uncertainty in models can be categorised into three sources.

- Model Uncertainty:
    - Structural errors, errors in the way the model is set up, e.g., physical mechanics such as cloud formation.
- Scenario Uncertainty:
    - Errors in the assumptions of how parameters change/evolve, such as the amount of CO2 emitted. This type of uncertainty dominates the long-term uncertainty.
- Initial Conditions Uncertainty
    - Errors stemming from the inability to be exact in the quantifying the initial conditions, which propagate into the future if the model is sensitive to initial conditions. This may not have strong effects on the long-term distribution, however, short-term forecasts can be severely affected.

Models are approximations and often produce mischaracterisations of the global mean
state. The likelihood of them being wrong is quantified as uncertainty. Uncertainty 
in models can be categorised into three sources: model uncertainty; scenario 
uncertainty; and initial conditions uncertainty{cite}`gettelman_demystifying_2016`. 
Model uncertainty arises from structural errors in the way the model operates. 
Knutti (2018) further splits model uncertainty into three sub-categories: model 
structure;  grid resolution; and parameterisation{cite}`knutti_climate_2018`. The 
latter two have been described above; an example of model structure uncertianty would 
be the intentional neglect of explicit ice sheet description or ocean dynamics, or 
errors in the equations representing physical mechanics; a prominent example being 
representing cloud formation. These types of uncertainty tend to create systematic 
errors warping the probability distribution of weather states in a consistent way, and 
are the core representational uncertainties in modelling the climate, solely belonging 
to model design. 

Scenario uncertainty stems from errors in the assumptions of how parameters change or 
evolve, such as the amount of anthropogenic CO2 emitted. This dominates the long-term 
uncertainty and is important in how it affects the non-stationarity property of 
climate. It is important for projections of future climate, but also how the model 
evolves up to the present day; over the elapsed period from initialisation to present 
day, CO2 forcing causes a shift in the mean climate state and affects other parameter 
values. Initial conditions uncertainty arises from the inability to be exact in the 
quantifying the initial conditions, errors which propagate into the future. Short-term 
forecasts can be severely affected by this type of uncertainty, however, it generally 
does not strongly effect the long-term distribution. Initial conditions and scenario 
uncertainties are beyond the scope of this study and will be largely ignored.

### Components of the Climate System

ESMs are usually composed of different building blocks, different systems that have specific boundaries where they can interact and specified mechanisms for those interactions. Typically these blocks are:

    - Atmosphere
        - Chemical make-up of air and all physical processes that occur within, including chemical interactions. Radiative budget and transfer of energy, momentum and mass are key components, so too are the carbon and hydrologic cycles.
    - Ocean
        - Chemical make-up of the oceans, physical properties such as carbon stores and acidity levels, large-scale ocean currents (circulation patterns), thermohaline circulation (stratification).
    - Terrestrial
        - Land use and resulting albedo, chemical interactions between this sphere and ocean & atmosphere.
    - Cryosphere
        - Sea ice, glaciers, ice sheets, snow.
    - Anthroposphere
        - Impacts of human activity.
    - Biosphere
        - Living organisms, soil, plants and animals.

Interactions between these systems occur on different timescales, and key elements of the Earth System, such as Carbon and Water, can cycle through different components. Understanding the interactions, movement and timescales of such cycles are of vital importance to creating a good ESM. 

### Essence of a Climate Model

"Coupling" refers to the binding and interactions between the systems, i.e., Coupled Model Intercomparison Project 6 refers to ESMs that simulate the evolution of coupled systems. 

Feedbacks change the energy budget -- the amount of energy in the Earth's system. This will cause a shift in the distribution function (or climate). 

Models are a combination of dynamical and empirical models. Dynamic models stem from an understanding of the underlying physical laws that govern, for example, motion and heat exchange. Whereas empirical laws stem from measurements and observations of the behaviour of some quantity. Empirical laws are constrained by the issue of the context of observations, i.e., the situation or environment that those observations were taken. This means that a model derived from empirical means may be insufficient under certain conditions. These empirical laws are often quantified as parameters, and herein lies a source of considerable uncertainty. These parameters and empirical models are constrained by physical laws such as conservation laws. 

Parameterisation is the process of representing the _effect_ of a physical sub-grid process at the grid resolution. For example, the effect of the presence and type of clouds within an element -- clouds exist at much smaller scales than grid resolution, such that the physical effect must be weighted by relative magnitude in calculating the state of the element. 

#### Basic Formulation and Constraints

Models are essentially a series of processes described by a set of eqations, which are solved for "finite elements", i.e., points on a gridded lattice. These points are distributed over a geometry that is representative of the Earth, with 3 dimensions in the zonal, meridional and vertical directions. The vertical direction often stretches through the atmosphere, for descriptions of vertical motion and interactions between atmospheric layers, also penetrating the ocean depths. Each finite element will have specified properties, described by an initial state, and the distribution of these properties or quantities will evolve according the governing equations -- each element will undergo changes in state. How to distribute finite elements such that the Earth is accurately represented is a problem for scientists, since the Earth is round meaning the size of the elements varies between the equator and poles. This has led to grid descriptions of hexagonal patterns, or variable grid resolution. The element is the basic unit, with the next level being the vertical column. 

Models are time integrations. This means that the state of the system (composed of the state of individual elements) is calculated at finite time steps. A model can be reduced to the simple notion of the repetition of a sequential procedure. The procedure is composed of those processes/equations that are calculated in a chosen order. The chosen order can affect the outcome of the model, therefore must be chosen carefully, however, the logical ordering is constrained by physical laws. The prodecure is split into following steps:

    1. Calculate the rates of processes and the exchange of mass/energy. e.g. evaporation/condensation of water and the associated latent energy change.
    2. Estimate flux of quantities between elements within a column, e.g. precipitation, deep convection, surface run-off.
    3. Estimate flux between different components, i.e., land-atmosphere, ocean-atmosphere, e.g., absorption of moisture by soil after rainfall, or the uptake of CO2 by the ocean.
    4. Solve physical laws ensuring the conservation laws are abided by, such as energy flux by radiative transfer.
    5. Calculate motion/dynamics between columns, and the associated flux of quantities such as water vapour. 

These steps are repeated for each time step.

When running dynamical models, they are split into modules and sub-modules that must be able to communicate with each other, e.g., columns are split and computed on separate modules, but need to communicate with each other since the present state of adjacents columns influence the future state of a given column. 

### Simulating the Atmosphere

Key components of the atmosphere include clouds, chemistry and water vapour concentrations. Global Circulation Models (GCMs; atmospheric models that simulate the entire global atmosphere, with basic boundary conditions at the top and bottom through which energy can flow) operate by coupling the processes that govern these key components, and calculating "sources" and "sinks" for them. Those sources and sinks are then used as "forcing terms" to calculate the dynamics on a rotating sphere.

Forcing terms include:
    - Changes in chemistry, e.g. water vapour to cloud vapour.
    - Radiative transfer.
    - Clouds.

Sub-grid processes that are near the grid scale are most difficult to resolve (scales at less than 1km are well-described by statistics, because they are well-removed from the grid resolution). This has to do with sample size. If there are, say, clouds of 20km, in a grid of 100km resolution, there are only 25 sub-units of this size. This means that estimating the number of sub-units that are covered by clouds will leave a large relative error if wrong, e.g., the error in estimating two 20km sub-units are covered by cloud, when in reality there are four covered by cloud, is a large relative error ($2/25$ instead of $4/25$). This sub-grid variability is another key source of uncertainty in climate models.

The "dynamical core" is a term used to describe the part of the model that solves the equations of motion of various quantities -- fluxes between adjacent horizontal elements. This includes the motion induced by difference in densities of two air parcels, the effect of drag, and the transportation of vapour, cloud drops, ozone and aerosol particles by the wind. 

### Sources of Uncertainty

- Fundamental errors in the representation of physical processes. (direct quote)
- Errors in parameterisation that lead to long-term error growth.
- Representing processes at scales below but close to the grid resolution.
- Feedbacks between processes introduce significant non-linearities and ensuring these processes respond in an appropriate fashion can be difficult to manage with the way climate models are set up.
- Cloud feedbacks are particularly difficult to model, given their effect on radiative budget and movement of heat and vapour. They are small-scale and transitory, making them very difficult to represent in ESMs.

Particularly relevant for storm tracks:
Storms are fed by the convective movement of water vapour (_find citation_), which is why storms are associated with large cloud banks. There are significant uncertainties around the representation of clouds in climate models. This is because cloud processes are numerous and complicated (_find citation, surely in AR6_) and representing them at sub-grid scales is a challenge. Statistical approaches are often inadequate because clouds exist at scales close to the the grid resolution, so that they cannot be sampled with great accuracy. Clouds provide the largest uncertainty in climate models. This is another reason why it is important to accurately represent the storm track because changes in meridional position, storm frequency and intensity can have significant impacts on cloud climatology. 

### Coupling of Earth Systems 

Coupling Ocean models to Atmospheric models is of importance for storm tracks as storms are often intensified by positive SSTAs in the mid-latitudes (which could be due to the increased presence of water vapour and the associated increase in convection (_find citation_)).

Issues arise with coupling models as small errors in the component models will affect the boundary conditions that are fed to other components of the model, e.g., if the ocean SSTs are systematically too low, this effect will be felt by the atmospheric model component as they share a boundary (sea surface).

### Model Evaluation

