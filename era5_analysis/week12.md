# Week 12

## 2022 May 17

### El Nino-Southern Oscillation Complexity {cite}`timmermann_ninosouthern_2018`

_Contains a useful glossary of terms relating to ENSO spatio-temporal complexity, including feedbacks and observed phenomena that characterise an El Nino and a La Nina event. Refer to this paper for explanations._

ENSO events have distinct spatial and temporal characteristics that mean no two events are totally alike. This is due to a number of coupled atmospheric and oceanic positive feedback loops, as well as a delayed negative oceanic feedback, known as recharge/discharge depending on the event being either El Nino or La Nina, that plays a key role in determining the length of time an event is sustained. Along with these feedbacks, there is a stochastic, state-dependent element in the form of Westerly Wind Events (WWEs) that are known to be the major driver in initiating El Nino events. Greater complexity is added to the mix by the consideration of ocean basin-scale phenomena such as the North and South Pacific Meridional Modes (NPMM and SPMM), tropical atmospheric waves and the South Pacific Booster (SPB). There are two prominent spatial modes of El Nino events, the Eastern Pacific (EP) event and Central Pacific event (CP). These two modes capture a large degree of the spatial variance in El Nino events and are driven by a different combinations of feedbacks. Another complication arises with non-linearities in atmospheric deep convection and oceanic heat advection.

#### ENSO Basic Model

El Nino at its most basic level can be characterised as a damped linear oscillator (though this model does not capture the spatial variability). Non-linearities and temporal complexities can be well represented by incorporating terms into parameters that mediate the model, for example in the damping terms. The basic model is described by:

```{math}
  \begin{align}
    \frac{dT_e}{dt} &= I_{BJ}T_e + Fh \\
    \frac{dh}{dt} &= -\epsilon h - \alpha T_e 
  \end{align}
```

where $T_e$ is the equatorial eastern Pacific SST, $h$ is the zonal mean thermocline depth, $I_{BJ}$ Bjerknes stability index, or ENSO linear growth rate, which parameterises Bjerknes feedbacks (see below for definition of various feedback mechanisms), $\epsilon$ is the damping rate of the thermocline feedback, $F$ parameterises the thermocline feedback and $\alpha$ parameterises the recharge/discharge delayed negative feedback process. Another term can be added to $I_{BJ}$ that parameterises the stochastic nature of WWEs, mulitplicative noise, and non-linearities in atmospheric deep convetion and oceanic heat advection.

#### Feedbacks

The following feedbacks are reversed for La Nina events, where weakening becomes strengthening, and positive becomes negative etc.

- Bjerknes Feedback -- Encapsulates a variety of positive feedbacks, decreased SST gradient causes weakening equatorial trade winds, which further decrease the SST gradient.
- Ekman Feedback -- Positive feedback. Decreased SST gradient causes weakening equatorial trade winds, which reduces upwelling of cold subsurface waters, further decreasing the SST gradient.
- Zonal Advective Feedback -- Positive feedback. Decreased SST gradient causes weakening equatorial trade winds, which reduce cold water from the eastern Pacific being advected westward, further decreasing the SST gradient. Plays a prominent role in CP events.
- Thermocline Feedback -- Positive feedback. Decreased SST gradient causes weakening equatorial trade winds, which causes a mean upwelling of warm subsurface water, further decreasing the SST gradient. Plays a prominent role in EP events.
- Recharge/Discharge Process -- Negative feedback. Meridional heat transport poleward, driven by changes to equatorial wind anomalies. Lagged process that controls the length of a given event. Generally weak during CP events, but strong during EP events with higher anomalies, resulting in a La Nina event the following winter.
- Thermal Damping Feedback -- Negative feedback. SST-induced changes in surface radition & turbulent heat fluxes serves to reduce the magnitude of a given event. Influenced by tropical clouds and atmospheric convection processes.
- Multiplicative Noise -- Positive feedback. Introduces some of the positive skew toward El Nino observed. Warmer ocean base states encourage more frequent and stronger WWEs that initiate and drive strong El Ninos.

#### Spatial Complexities

Spatial complexity can largely be described by the first two EOFs of tropical Pacific SSTAs:
- EOF1 -- classic El Nino pattern, corresponds to EP mode. Varies on a 3-7 year timescale and explains 49% of the observed variance.
- EOF2 -- Characterises CP mode. Varies over a longer timescale of 7-15 years, and explains 10% of the observed variance. Events with a strong positive projection onto EOF2 tend to be CP events. 

EP & CP events are modulated and characterised by the combination and relative strengths of thermocline and zonal advective feedbacks.

Typical Characteristics of EP & CP Events:
- 
- Strong relaxtion of thermocline zonal tilt.
- Prominent thermocline feedback.
- Large eastward convection shift.
- Strong heat discharge (with a La Nina event likely to follow).

```{table} Typical Characteristics of EP & CP Events
:name: enso-spatio-table

| EP | CP | 
| :-- | :-- |
| Basin-scale wind anomalies. | Local wind feedbacks. |
| Strong relaxtion of thermocline zonal tilt. | Little change to thermocline zonal tilt. |
| Prominent thermocline feedback. | Prominent zonal advective feedback. |
| Large eastward convection shift. | Weak convection shift. |
| Strong heat discharge. | Lower meridional heat discharge. |
| La Nina event likely to follow. | La Nina event less likely. |
| Longer period of event. | Earlier termination of event. |
| Weak thermal damping. | Strong thermal damping. |
```

#### Seasonal Characteristics

El Nino events usually begin during austral autumn, grow during winter and spring and reach their maximum intensity during the following summer. They then decay rapidly during late summer and autumn and, in most cases, a La Nina event occurs by the following winter. The above case is by no means a given, but merely occurs most often, however seasonal cycles of other drivers and influences serve to increase the temporal complexities of ENSO events. 

There are seasonal variations in oceanic-atmospheric coupling strength. This can be incorporated into the linear oscillator model by adding a seasonally varying term to $I_{BJ}$. Interactions between the seasonal $I_{BJ}$ cycle and interannual ocean temperature signal generates variability over 9-18 month periods -- this interaction is known as combination tone frequencies or C-modes.

#### Unifying Framework

The framework that Timmermann et al. proposes combines the linear oscillator model with a "duplet" of eigenmodes (derived from a model but with high similarity with the Pacific SSTA EOFs) and a number of excitation mechanisms. The first and second eigenmodes vary on a four-yearly and two-yearly basis respectively. These modes capture the features that characterise EP and CP events, and remain close to a nuetral state under realistic base states, meaning that these modes can be easily excited. Proposed excitation mechanisms include the NPMM, SPMM, SPB, WWEs and tropical instabilty waves. Greater excitation of El Nino events is incorporated into the linear oscillation model through the addition of a non-linear term parameterising atmospheric deep convection and oceanic heat advection. This model in it's totality goes a long way to describing the observed spatio-temporal complexities in ENSO events.
