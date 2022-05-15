# Week 5

This lab notebook belongs to a set of [preliminary research](preliminary_research.md).

## 2022 Mar 28

### Introduction to Dynamic Meteorology {cite}`holton_intro_`

- How do baroclinic instabilities form?
    - Do they propagate down from the polar jets? If so, how?
- How do vertical temperature gradients affect baroclinic instabilities?
    - Is it something to do with the static stability/stratification?
- What are stationary eddies?
- What are the most important equations/physical processes relating to storm tracks?


#### Assumptions

- Continuum approximation - a mass of air (or air parcel) is assumed to take on the average property of all the particles that make up that air parcel, contained within, such that the air parcel may take on a continuum of values.
- Conservation laws
    - Conservation of momentum (Newton's third law).
    - Conservation of mass.
    - Conservation of energy (first law of thermodynamics).
- Atmosphere follows ideal gas law.
- Atmosphere remains in hydrostatic balance (except for weather systems such as tropical cyclones & squall lines).
- Geostrophic balance between coriolis force and pressure gradient, only a valid approximation for large-scale motions in the midlatitudes.
- It is assumed that dry processes are approximately adiabatic, and moist processes, such as precipitation, are diabatic processes.


#### Introduction

All forces are per unit volume, per unit mass, in order to standardise the units for manipulation. There are two types of forces involved in meteorology:
- surface forces - act on a boundary (of an air parcel), independent of mass e.g. pressure gradient force.
- body forces - act on centre of mass, dependent on magnitude of mass e.g. gravitational force.

Forces of interest in meteorology are: gravitational; pressure gradient; and frictional forces. Apparent forces, centrifugal and coriolis forces, are also important to consider.

##### Pressure

Proportional to gradient of the pressure, not to the absolute value:

```{math}
  \begin{equation}
    F_p = \frac{1}{\rho} \nabla p
  \end{equation}
```


##### Viscosity

Viscosity forces arise when there is a spatial asymmetry, when random motion of molecules results in a transport of momentum to areas of lower pressure. This force acts along the face of the air parcel, creating shear $\tau = F/A$, where A is the surface area of the face experiencing viscosity effects. Shear is linearly proportional to the fluid speed, to a good approximation for air, giving $\tau = \upsilon \frac{\partial u}{\partial z}$, where $upsilon$ is the kinematic viscosity coefficient, per unit density. In three-dimensions,

```{math}
  \begin{equation}
    F_{\upsilon} = \upsilon \nabla^2 u
  \end{equation}
```

Each component of represents diffusion of momentum in each direction. This equation states that there is a loss of momentum from the maximum to the surrounding regions, known as "downgradient diffusion".

Viscosity effects are negligible below 100km because $\upsilon$ is so small, with the exception of the first few centimetres above the surface, called the molecular surface boundary layer. Elsewhere, turbulent eddies are the biggest transporters of momentum.


##### Gravitation

Gravity works on the centre of mass of an air particle, stemming from Newton's law of Gravitation, with a reference frame that begins at sea level, the "true" value of $g$, $g^*$, is given by,

```{math}
  \begin{equation}
    g^* = \frac{g_0^*}{(1 + z/a)^2}
  \end{equation}
```

However, this is offset by the centrifugal force, which in a rotating reference frame appears to add a horizontal component to the force, changing the direction of motion according to the observer in that rotating reference frame. This is accounted for in the calculation and use of the gravitational constant $g$, such that the "apparent gravity" g is,

```{math}
  \begin{equation}
    g = g^* + \Omega^2 R
  \end{equation}
```

where $\Omega$ is the angular velocity of the Earth, and R is the radius of the Earth.

##### Coriolis Force

Arises due to the conservation of angular momentum in a rotating reference frame. Horizontal components are,

```{math}
  \begin{align}
    \frac{Du}{Dt} &= 2\Omega v\sin{\phi} = fv \\
    \frac{Dv}{Dt} &= 2\Omega u\sin{\phi} = fu 
  \end{align}
```

where $f = 2\Omega\sin{\phi}$, the coriolis parameter, and $\phi$ is the latitude.


##### Static Atmosphere

Assumption of air as an ideal gas, $p = \alpha RT$, where $\alpha = \rho^{-1}$, and atmosphere is in hydrostatic balance,

```{math}
  \begin{equation}
    p(z) \int_{z}^{\infty} \rho gdz
  \end{equation}
```

This gives two important equations, geopotential height,

```{math}
  \begin{equation}
    \Phi (z) = \int_{0}^{z} gdz
  \end{equation}
```

and the Hypsometric equation, 

```{math}
  \begin{equation}
    \Delta \Phi (z) = R \int_{p_2}^{p_1} Tdlnp
  \end{equation}
```

This is important for a number of reasons. It tells us that in an isothermal atmosphere, pressure decreases exponentially, $p(z) = p_0 \exp^{\frac{-z}{H}}$, where H is the isothermal scale height. It can also tell us the thickness of a given atmospheric layer, between two heights. It also tells us that pressure varies with height monotonically, so can be used as a vertical coordinate. 

In this isobaric coordinate system, horizontal pressure gradient is measured by the gradient of geopotential height at constant pressure,

```{math}
  \begin{equation}
    -\frac{1}{\rho}\bigg( \frac{\partial p}{\partial y}\bigg)_z = -\bigg( \frac{\partial \Phi}{\partial y}\bigg)_p
  \end{equation}
```


##### Kinematics

Kinematics is a description of a fluid flow at an instant in time. Four quantities are useful for this:

```{math}
  \begin{align}
    \frac{du}{dx} + \frac{dv}{dy} &= \delta, \ divergence \\
    \frac{dv}{dx} - \frac{du}{dy} &= \zeta, \ vorticity \\
    \frac{du}{dx} - \frac{dv}{dy} &= d_1, \\
    \frac{dv}{dx} + \frac{du}{dy} &= d_2
  \end{align}
```

$d_1$ and $d_2$ represent deformation of the flow, along the axis of contraction and axis of dilatation respectively. They are positioned at 45\textdegree  to each other, hence are not independent patterns. 

Linear variations in a flow can be described by these for quantities as such,

```{math}
  \begin{align}
    u(x_0 + \delta x, y_0 + \delta y) \approx u(x_0,y_0) + \frac{1}{2}(\delta + d_1)\delta x + frac{1}{2}(d_2 - \zeta)\delta y \\
    v(x_0 + \delta x, y_0 + \delta y) \approx v(x_0,y_0) + \frac{1}{2}(\zeta + d_2)\delta x + frac{1}{2}(\delta - d_1)\delta y
  \end{align}
```

```{note}
Character of atmospheric motions depends heavily on the horizontal scale, hence derivations of mechanics are justified using sclaing explanations.
```


#### Basic Conservatation Laws

##### Complete Equations of Motion

```{math}
  \begin{align}
    \frac{Du}{Dt} - \frac{uv\tan{\phi}}{a} + \frac{uw}{a} &= -\frac{1}{\rho} \frac{\partial p}{\partial x} + 2\Omega v\sin{\phi} - 2\Omega w\cos{\phi} + F_{rx} \\
    \frac{Dv}{Dt} - \frac{u^2\tan{\phi}}{a} + \frac{vw}{a} &= -\frac{1}{\rho} \frac{\partial p}{\partial y} - 2\Omega u\sin{\phi} + F_{ry} \\
    \frac{Dw}{Dt} - \frac{u^2 + v^2}{a} &= -\frac{1}{\rho} \frac{\partial p}{\partial z} - g + 2\Omega u\cos{\phi} + F_{rz}
  \end{align}
```  

These equations completely describe the motions of all atmospheric dynamics, including sound waves (sound waves are always filtered out however, based on scale analysis the solution is negligible).


##### Frames of Reference

There are two frames of reference, each possessing particular advantages.
- Eulerian reference frame
  - A fixed parallelipiped, $\delta x\delta y\delta z$,through which fluid flows, fluxes of energy, mass and momentum flow in and out through the faces.
  - Easier for solving problems as the coordinate system requires no transformation with time.
- Lagrangian reference frame
  - A parallelipiped that travels with the fluid motion.
  - Easier for deriving the conservation laws.


##### Rates of Change

There are two types of rates of change, the rate of change of a field variable with the fluid flow, and the rate of change at a fixed point. These are given by the total derivative, and the partial derivative with respect to time, respectively,

```{math}
  \begin{align}
    \frac{D}{Dt} &= \frac{\partial}{\partial t} + u\frac{\partial}{\partial x} + v\frac{\partial}{\partial y} + w\frac{\partial}{\partial z} = \frac{\partial}{\partial t} + \vec{U} \cdot \nabla \\
    \frac{\partial}{\partial t} &= \frac{D}{Dt} - \vec{U}\cdot \nabla
  \end{align}
```

The second equation is the relation between the two rates of change. If the total derivative is zero, then the field variable is conserved, and the local change at a point is entirely due to advection.


##### Scale Analysis

Elimination of terms can be done on the basis of scale of the process being considered. This can greatly simplify the equations of motion. One example would be the assumption of Geostrophic wind at the mid-latitudes. At this location, the pressure gradient and coriolis forces are a couple of orders of magnitude greater than any other term (in the complete equations of motion given above), therefore these are the only two that need be considered. This is a very good approximation for the mid-latitudes, however at higher and lower latitudes other forces become important. The Rossby number is a measure of the validity of the approximation, given by the characteristic scales of the pressure gradient and coriolis forces.

```{math}
  \begin{equation}
    R_o = \frac{U^2/L}{f_0U} = \frac{U}{f_0L}
  \end{equation}
```

##### Conservation of Mass

Mass must be conserved across the globe. Any divergence observed in 2-D is a sign of vertical motions, maintaining the conservation of mass.

```{math}
  \begin{equation}
    \frac{1}{\rho}\frac{D\rho}{Dt} + \nabla\cdot \vec{U} = 0
  \end{equation}
```

##### Conservation of Energy

Stemming from the first law of Thermodynamics, the mechanical energy equation can be derived, which relates the rate of change of mechanical energy to the rate of work done by the pressure gradient. In this case, mechanical energy is the sum of geopotential energy and kinetic energy of an air mass.

```{math}
  \begin{equation}
    \rho\frac{D}{Dt}\bigg( \frac{1}{2}\vec{U}\cdot\vec{U} + \Phi \bigg) = -\vec{U}\cdot\nabla p
  \end{equation}
```

This can be restructured into the familiar Thermodynamic energy equation,

```{math}
  \begin{equation}
    c_v\frac{DT}{Dt} + p\frac{D\alpha}{Dt} = J
  \end{equation}
```

where $J$ is the heating by conduction, latent heat etc. per unit mass.


##### Thermodynamics of a Dry Atmosphere

Assuming adiabatic processes is often a reasonable approximation for most circumstances, where the atmosphere can be assumed to be dry. Because of the decreasing temperature with height, it is often convenient to compare the "potential temperature" of a given air mass using the surface pressure as a reference point. For adiabatic processes, $dq = 0$, hence from the first law, $D(c_p\ln{T} - R\ln{p}) = 0$, which can be integrated to give,

```{math}
  \begin{equation}
    \theta = T\Big( \frac{p}{p_s} \Big)^{R/c_p}
  \end{equation}
```

where potential temperature, $\theta$, is the temperature that an air mass at temperature, $T$, and pressure, $p$, would have it was expanded/compressed to the surface pressure, $p_s$. This is only valid for dry adiabatic motions, of which synoptic-scale motions outside of precipitation regions is often a good approximation. Potential temperature is invariant for a parcel being lifted and compressed or descending and expanding. Isentropic lines, lines of constant potential temperature, are natural lines for parcels motion to follow since no work need be done on the parccel, nor any change in heat (due to the adiabatic assumption).

The equation for potential temperature can be manipulated to give the gradient of potential temperature with height, by taking logarithms, and differentiating with respect to height, $z$,

```{math}
  \begin{equation}
    \frac{T}{\theta}\frac{\partial\theta}{\partial z} = \frac{\partial T}{\partial z} + \frac{g}{c_p}
  \end{equation}
```

which, for an atmosphere with constant potential temperature, informs us that the dry adiabatic lapse rate for the lower atmosphere is constant(where this is a fair approximation),

```{math}
  \begin{equation}
    \Gamma_d = \frac{g}{c_p}
  \end{equation}
```

If the atmosphere doesn't have a constant potential temperature however, the change in potential temperature can be given as the difference between the dry adiabtaic lapse rate, $\Gamma_d$, and the atmospheric lapse rate, $\Gamma$,

```{math}
  \begin{equation}
    \frac{T}{\theta}\frac{\partial\theta}{\partial z} = \Gamma_d - \Gamma
  \end{equation}
```

If $\Gamma_d > \Gamma$, the atmosphere is "stably stratified", dampening the ability of buoyant air to ascend for long distances. Buoyant air parcels will instead undergo "buoyancy oscillations", and no large-scale convection events will occur. The conditions for atmospheric stabilty are given by,

```{math}
  \begin{align}
    \frac{d\theta_0}{dz} &> 0, \ statically\ stable \\
    \frac{d\theta_0}{dz} &= 0, \ statically\ neutral \\
    \frac{d\theta_0}{dz} &< 0, \ statically\ unstable
  \end{align}
```


##### Thermodynamics of a Moist Atmosphere

When water vapour is present in the atmosphere, this has a significant effect on the dynamics of the atmosphere. Water vapour influences the stability condition through partial pressure, and is the main reason why large-scale convective motions up to the tropopause can occur. A convection event is possible if the saturated lapse rate, $\Gamma_s < \Gamma$. This is known as conditional stability, and the conditions for stability are given in terms of equivalent potential temperature of an equivalent atmosphere, $d\ln{\theta_e*} = d\ln{\theta} + d(L_cq_s/c_pT)$, where $q_s$ is the saturated mixing ratio of moist and dry air. The conditions for stability are,

```{math}
  \begin{align}
    \frac{d\theta_e^*}{dz} &> 0, \ conditionally\ stable \\
    \frac{d\theta_e^*}{dz} &= 0, \ conditionally\ neutral \\
    \frac{d\theta_e^*}{dz} &< 0, \ conditionally\ unstable
  \end{align}
```

The equations given above for a dry atmosphere must be amended to account for the presence of vapour. The pressure of the air parcel is now, by Dalton's law, $p = p_d + e$, where $e$ is the vapour pressure. More conveniently, this is expressed in terms of $T_v$, virtual temperature.

```{math}
  \begin{equation}
    p = \rho R_d T_v
  \end{equation}
```

where $R_d$ is the dry gas constant, and,

```{math}
  \begin{equation}
    T_v = \frac{T}{1-\frac{e}{p}\Big( 1-\frac{R_d}{R_v}\Big)}
  \end{equation}
```

The virtual temperature is the temperature that a dry air parcel needs to be in order to have the same density as a moist air parcel. It is in effect a correction factor for the increased buoyancy of moist air, and it is always higher than the real temperature, usually a few degrees more. The more humid the air, i.e. the greater amount of water vapour in the air parcel, the greater the correction factor, virtual temperature will be. 

Saturated Vapour Pressure is given by,

```{math}
  \begin{equation}
    SVP = \frac{1}{e_s}\frac{de_s}{dT} = \frac{L}{RT^2}
  \end{equation}
```


## 2022 Mar 29

### Introduction to Dynamic Meteorology {cite}`holton_intro_`

#### Elementary Applications of Basic Equations

##### Equations in Isobaric Coordinates

Using the isobaric coordinate system has a number of advantages, but significiantly the dependency of equations of motion on density is removed. The horizontal momentum equation becomes,

```{math}
  \begin{equation}
    \frac{D\vec{V}}{Dt} + f\hat{k} \times \vec{V} = -\nabla_p \phi
  \end{equation}
```

where the gradient of horizontal coordinates are taken at constant pressure.

The geostrophic relation becomes,

```{math}
  \begin{equation}
    f\vec{V}_g = \vec{V} \times \nabla_p \phi
  \end{equation}
```

If constant coriolis parameter, i.e. no meridional flow, there is no divergence in the geostrophic flow. 

A similar method can be adopted for the continuity equation, in isobaric coordinates,

```{math}
  \begin{equation}
    \bigg( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \bigg)_p + \frac{\partial \omega}{\partial p} = 0
  \end{equation}
```

where $\omega$ is the pressure change following the motion of the air parcel, the "omega" vertical motion. Once again, the horizontal coordinates are held at constant pressure.

The thermodynamic energy equation becomes,

```{math}
  \begin{equation}
    \bigg( \frac{\partial T}{\partial t} u\frac{\partial T}{\partial x} + v\frac{\partial T}{\partial y} \bigg) - S_p\omega = \frac{J}{c_p}
  \end{equation}
```

where $S_p$ is the static stability parameter, given by,

```{math}
  \begin{equation}
    S_p = - \frac{T}{\theta}\frac{\partial \theta}{\partial p} = (\Gamma_d - \Gamma)/\rho g 
  \end{equation}
```


##### Natural Coordinates

A natural set of coordinates are used to describe flows, $\hat{t}, \hat{n}, \hat{k}$, where $\hat{t}$ is orientated parallel to the horizontal velocity at each point, $\hat{n}$ is normal to the same horizontal velocity, and $\hat{k}$ is the usual vertical coordinate. This greatly simplifies the equations of motion. The horizontal momentum equation in the natural coordinate system, in $\hat{t}$ and $\hat{n}$ components,

```{math}
  \begin{align}
    \frac{DV}{Dt} &= -\frac{\partial \Phi}{\partial s} \\
    \frac{V^2}{R} + fV = -\frac{\partial \Phi}{\partial n}
  \end{align}
```

where, $R$ is the radius of curvature of the air parcel path, $s(x, y, t)$ is the distance along that path, and $\Phi$ is the geopotential height field as usual. These equations detail the fluid motions in the natural coordinate system.


###### Flow Types in the Natural Coordinates

In this system, the _geostrophic flow_ equation simplifies to $fV_g = -\partial \Phi / \partial n$. Any component of wind that is not in geostrophic balance is referred to as ageostrophic wind.

_Inertial flow_ is a type of flow that occurs when there is no horizontal pressure gradient, such that the equations reduce to a balance between the coriolis and centrifugal forces -- two inertial forces. This results in,

```{math}
  \begin{equation}
    \frac{V^2}{R} + fV = 0
  \end{equation}
```

which can be solved for the radius of curvature,

```{math}
  \begin{equation}
    R = \frac{-V}{f}
  \end{equation}
```

Neglecting the latitudinal dependence of $f$, this is a constant $R$, hence the flow follows a circular path in the anticyclonic direction (since \hat{n} is defined as positive to the left of the flow direction).

_Cyclostrophic flow_ occurs when the coriolis force may be neglected, which, solving the equation of motion for $V$, gives,

```{math}
  \begin{equation}
    V = \bigg( -R\frac{\partial \Phi}{\partial n} \bigg)^{1/2}
  \end{equation}
```

This flow may be both cyclonic or anticyclonic. The pressure gradient is always directed toward the centre of curvature, the centrifugal force away. This motion is important for tornado-scale motions. They tend to rotate in a cyclonic direction, however this is due to the fact ehy are embedded in environments that favour this motion, and no preference is inherent in the mechanics of the flow itself.


##### Thermal Wind

By considering the premise of hydrostatic balance, it can be inferred that there must be vertical wind shear when there is a horizontal temperature gradient. This is because air columns with higher average temperatures will be taller, hence there will be a geopotential gradient (due to the difference in density). Since geostrophic wind speed is proportional to geopotential gradient along an isobaric surface, higher altitudes in the troposphere will have a higher the geopotential gradient, hence a higher wind speed.

The Thermal Wind relation is expressed fully by,

```{math}
  \begin{equation}
    \frac{\partial\vec{V}_g}{\partial\ln{z}} = -\frac{R}{f}\hat{k} \times \nabla_p T
  \end{equation}
```

This equation is valid for predicting _geostrophic wind_ at a given height, provided geostrophic wind at a reference height, and the horizontal temperature gradent are known.

##### Formation of a Cyclone - in brief

Suppose a heat source is located in the midtroposphere, resulting in a local warm anomaly. This will raise the depth of the column above the warm anomaly, in accordance with the hypsometric equation. This results in a horizontal pressure gradient, creating upper-level divergence. This will initially cause the surface pressure to decrease, causing a surface low. The surface low will draw in air creating lower-level convergence and driving vertical circulation. The degree to which this vertical circulation compensates for the upper-level divergence will determine whether the surface low deepens, remains steady, or returns to normal. This is an example of high distrubances at any level in the atmosphere can propagate up- or downward.


#### Circulation, Vorticity & Potential Vorticity

Circulation and vorticity are two primary measures of rotation in a fluid. Circulation, a scalar integral quantity, is a macroscopic measure; vorticity is a vector field measuring microscopic rotation.


##### Circulation

Kelvin's Circulation Theorem is given by,

```{math}
  \begin{equation}
    \frac{DC_a}{Dt} = -\oint \rho^{-1} dp
  \end{equation}
```

which says that the absolute change in Circulation of a fluid is equal to the total change in pressure, including density, which is a function of pressure. This is further complicated under baroclinic conditions, when density is dependent on temperature as well as pressure. This equation can be applied to calculate the change in wind speed over a density discontinuity, such as a land-sea boundary.

##### Vorticity

Vorticity is related to the macroscopic Circulation by Stokes' theorem, which states,

```{math}
  \begin{equation}
    -\oint \vec{U} \cdot d\vec{l} = \iint_A (\nabla \times \vec{U})\cdot \hat{n} dA
  \end{equation}
```

meaning that the line integral of the tangential velocity of a closed loop is equal to the vorticity over the surface enclosed by that loop.

Vorticity is mostly considered in the vertical component, as other contributions are small. This component is vertical because of the vector nature of vorticity, however the vertical component is made up of contributions from the horizontal flow,

```{math}
  \begin{equation}
    \zeta = \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y}
  \end{equation}
```

Using the horizontal momentum equations, the vorticity equation becomes,

```{math}
  \begin{equation}
    \frac{D}{Dt}(\zeta + f) = -(\zeta + f)\bigg( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\bigg) - \bigg( \frac{\partial w}{\partial x}\frac{\partial v}{\partial z} - \frac{\partial w}{\partial y}\frac{\partial u}{\partial z}\bigg) + \frac{1}{\rho^2} \bigg(\frac{\partial \rho}{\partial x}\frac{\partial p}{\partial y} - \frac{\partial \rho}{\partial y}\frac{\partial p}{\partial x}\bigg)
  \end{equation}
```

where $\frac{Df}{Dt} = v\frac{df}{dy}$ since the coriolis parameter depends only on y. This equation states that the rate of change of vorticity with the flow depends on the three terms on the right, the divergence (or vorticity stertching), the tilting or twisting term (deformation of the flow), and the solenoidal term.

The concentration or dilution of the vorticity field (convergent or divergent flow) is very important for synoptic-scale distrubances. If the flow is divergent, the area enclosed by a loop, or air parcel, ncreases, meaning that for circulation to be conserved, the average vorticity in the loop must decrease. Conversely for convergent flow, if the area of the air parcel decreases, the absolute average vorticity will increase.

The tilting term is a measure of vertical vorticity generated by the tilting of horizontal components of the flow, e.g. if the y-component increases with height, there is a horizontal gradient in the y-direction creating a shear effect in the x-direction. If there is also a decrease in vertical velocity with increasing x, this will tilt the vorticity vector such that there is a component in the vertical direction. Hence, if $\partial v/\partial z > 0$ and $\partial w/\partial x < 0$, there is a positive vertical vorticity. The same will be true for the inverse of the negative part of the term. 

```{note}
Read up on classical mechanics again to interpret the third term, specifically Hamiltonian mechanics and Poisson brackets.
```

In the isobaric coordinate system, the solenoidal term is missing since the horizontal components are evaluated at constant pressure. This difference is genreally unimportant as the solenoidal term is usually so small as to be considered negligible. 

Using scale analysis for mid-latitude synoptic systems, the $\zeta$ relative vorticity may be neglected, as the coriolis parameter dominates the flow. Thus the vorticity equation simplifies to,

```{math}
  \begin{equation}
    \frac{D_h(\zeta + f)}{Dt} = -(\zeta + f)\bigg( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\bigg)
  \end{equation}
```

where, $D_h/Dt$ includes the horizontal components only. This equation states that the absolute vorticity of horizontal synoptic scale motions are approximately the divergence/convergence of planetary vorticity. This equation also indicates why cyclonic systems are stronger on average than anti-cyclonic systems. In a convergent flow, the relative vorticity will increase, strengthening the $(\zeta + f)$ term. However for a divergent flow, the opposite is true, such that relative the term shrinks. 

```{note}
This approximation does not remain valid nearly frontal systems.
```


##### Potential Vorticity

On an isentropic surface (a surface of constant potential temperature), it can be proven that Kelvin's circulation still holds, even for baroclinic systems. This is possible because isentropic surfaces mean that the density is dependent on pressure alone. Uzing Stokes' theorem, we can apply the same logic to vorticity component normal to the surface. This gives the very important __Ertel potential vorticity theorem__,

```{math}
  \begin{equation}
    \frac{D}{Dt}\bigg[ \frac{\omega_a \cdot \nabla\theta}{\rho}\bigg] = \frac{D}{Dt} \Pi = 0
  \end{equation}
```

This states that the quantity known as potential vorticity, PV, is conserved following the motion of an air parcel. This is very important, since it relates all the conservation laws into one simple equation, placing a constraint on the types of motions developing.

On synoptic and larger scales, the Rossby number is small, such that the dominant contribution to PV is from the vertical direction. 

```{admonition}
This explains why the focus on vertical vorticity!
```

Further simplifications can be made to the Ertel PV theorem by assuming shallow water equations -- an approximation of a shallow incompressible fluid whose vertical scale is negligible to its horizontal scale, a useful approximation for large-scale dynamic motions. Another simplification is to assuming isentropic coordinates, or potential temperature. This assumes that the atmosphere is stably stratified, such that $\theta$ increases monotonically with height.

```{note}
Weather disturbances that have sharp gradients in dynamical fields, such as jets and fronts, are associated with anomalies in the Ertel PV. Such anomalis tend to be rapidly advected under nearly adiabatic conditions in the upper troposphere, hence PV anomalies are useful for identifying meteorological disturbances.
```


## 2022 Mar 30

### Intro to Dynamic Meteorology, {cite}`holton_intro_`

#### Atmospheric Oscillations: Linear Perturbation Theory

This chapter focuses on an analytical method of idealised representations of the atmosphere. These idealised atmospheres are useful in isolating featues of the general flow and building up a comprehensive picture piece-by-piece.


##### Perturbation Method

All field variables are split into two parts, the field average (or basic state) and the deviation from that average. For example, $u(x,t) = \bar{u} + u'(x,t)$. The basic assumptions are that the field averages must satisfy the solutions to the governing equations, and that the deviations are small enough such that only the linear terms need be considered. This means that any perturbations may be considered to be wave-like, hence take on wave properties and are solutions to the linear harmonic oscillator equation, composed of any linear combination of sine and cosine waves. 


````{admonition} Dispersion and Group Velocity
For some waves whose phase speed varies with wavenumber $k$, the sinusoidal components making up the waves will later be found in different locations -- the wave envelope has dispersed. For this type of wave, the actual rate of energy transfer is better described by the group velocity, given by,
```{math}
  \begin{equation}
    c_{gx} = \partial \mu /\partial k
  \end{equation}
```
````


##### Waves in 2D and 3D

Waves of higher dimensions are more easily evaluated in space and time separately, characterised by a phase angle $\phi$. Lines of constant phase capture the propagation in higher dimensions. For spatial dimensions, the wave vector is defined by,

```{math}
  \begin{equation}
    \vec{K} = \nabla \phi
  \end{equation}
```

where $\phi = kx + ly + C$, $l$ and $k$ are the wane numbers in the y- and x-directions, and $C$ is some arbitrary constant. For the time dimension, 

```{math}
  \begin{equation}
    \mu = -\partial \phi /\partial t
  \end{equation}
```

where $\phi = C - \mu t$. The phase speed is then,

```{math}
  \begin{equation}
    c = \frac{\mu}{\mathcal{K}} = -\frac{1}{|\nabla\phi |} \frac{\partial \phi}{\partial t}
  \end{equation}
```

where $\mathcal{K} = |\vec{K} |$. Group velocity is then $\vec{C}_g = \nabla_k \mu = \Big(\frac{\partial \mu}{\partial k},\ \frac{\partial \mu}{\partial l}\Big)$. 

Importantly, in a frame of reference moving with the group velocity, the wave vector is conserved, as given by,

```{math}
  \begin{equation}
    \frac{\partial \vec{K}}{\partial t} + (\vec{C}_g \cdot \nabla )\vec{K} = 0
  \end{equation}
```


##### Shallow Water Waves

Shallow water waves are used as a good approximation of atmospheric waves of minimal vertical extent, shallow depth. Using linearised momentum & continuity equations, information about the characteristics of the waves can be uncovered. Solving for $\mu$,

```{math}
  \begin{equation}
    \mu^3 - \mu\Big[ f^2 +g\bar{h} \big( k^2 + l^2\big) \Big] = 0
  \end{equation}
```

Clearly, $\mu = 0$ is a solution. Provided $f$ is constant, this gives the stationary Rossby waves solution, dependent on rotation alone i.e. zero wave speed.

Where $\mu \ne 0$, this gives inertia-gravity wave solutions, explored in detail later. Another important result stems from this, which is htat linearised PV for shallow water waves are shown to be conserved at all local points,

```{math}
  \begin{equation}
    \frac{\partial Q'}{\partial t} = \zeta ' - \frac{f}{\bar{h}}h' = 0
  \end{equation}
```

Key characteristics and differences between Rossby Waves and Inertia-Gravity waves:

| Rossby | Inertia-Gravity |
| :-- | :-- |
| Stationary waves | Move very fast |
| Geostrophic winds with zero divergence & large relative vorticity | High divergence and low relative vorticity |
| Non-zero PV | Zero PV |


##### Internal Gravity Waves

Exist in a stably stratified atmosphere where buoyancy is the restoring force for any displacements. In a fluid with no upper boundary, such as the atmosphere, gravity waves can propagate in the vertical direction -- referred to as internal gravity waves.

One form of internal gravity waves are known as "pure" internal gravity waves. These are a wave form derived whilst assuming constant density with height and only small perturbations (as per linear perturbation theory). This means that the vertical scale of the morions must be less than $H$, the isothermal scale height, approximately 8km. They are generated by tropospheric cumulus convection, flow over topography and other processes. They propagate into the middle atmosphere, many times the iosthermal scale height -- _why?_ They have the remarkable property of the group velocity being perpendicular to the direction of phase propagation, such that energy propagates parallel to the wave crests and troughs -- the opposite to sound waves and other shallow water gravity waves.

##### Rossby Waves

Waves of great importance to large-scale circulation process, Rossby waves, also known as _planetary waves_, are generated by the meridional variation in the Coriolis parameter. In a baroclinic atmosphere, it is a potential vorticity-conserving wave that propagates through the atmosphere in an westward direction realtive to the mean flow (although still travels eastward due to the mean flow being faster). If an air parcel is displaced by small meridional distance, $\delta y$, the coriolis force will act to restore the air parcel to equilibrium, setting up an oscillatory motion in the vorticity field (as $f$ is a component of the absolute vorticity field, $\eta$, hence a hcnage in the coriolis parameter causes a change in the absolute vorticity), propagating in a westwards direction. In other words, the meridional absolute vorticity gradient resists meridonal displacement, providing a restoring force.

The variation of the coriolis parameter is often approximated using the _midlatitude $\beta$-plane_ approximation, given by,

```{math}
  \begin{eqaution}
    f = f_0 + \beta y
  \end{equation}
```

where $\beta = (df/dy)_{\phi_0} = 2\Omega \cos{\phi_0 /a}$ and $y=0$ at $\phi_0$. By assuming $\delta y$ has a wavelike signal, such that $\delta y = a\sin{[k(x-ct)]}, the phase speed is found to be,

```{math}
  \begin{equation}
    c=-\beta /k^2
  \end{equation}
```

Hence the wave speed is inversely proportional to the zonal wave number (_important for predicted changes to ZW3_). This shows that Rossby waves are dispersive. In 2D, including the zonal mean wind speed, the relative phase speed becomes,

```{math}
  \begin{equation}
    c - \bar{u} = -\beta /K^2
  \end{equation}
```

If the square of the wave number, $K^2=\beta /\bar{u}$, then the wave solution becomes stationary, i.e. zero phase speed.

Westward propoagating Rossby waves, along with eastward- and westward-propagating gravity waves, are normal modes of a hydrostatic, gravitationally stable atmosphere. As such, these free oscillations are frequently excited by perturbations in the atmosphere. Although, free-moving Rossby waves ahve relatively small amplitudes hence do not have a significant impact of the transfer of energy, momentum, mass etc.

Stationary Rossby waves are of great importance for understanding global circulation patterns. Flow over topographic featueres generate significant quasi-stationary variations in the geopotential height field. 


## 2022 Mar 31

### Intro to Dynamic Meteorology, {cite}`holton_intro_`

#### Quasi-Geostrophic (QG) Analysis

This analysis method simplifies some of the complexities of atmospheric dynamics by assuming near hydrostatic and geostrophic behaviour. It is assumed that the Rossby number is small i.e. for systems in the mid-latitudes where the coriolis force is significant. A full set of simplified equations stemming from this analysis are derived. 


##### Derivation of QG Equations 

For motions that are nearly hydrostatic and geostrophic, the 3-dimensional flow field is approximately determined by the pressure field. This operates under the assumption of constant density (Boussinesq approximation), and the $f$-field approximation -- the coriolis parameter is constant. The following equations are defined for a small Rossby number and an atmosphere with strong stratification.

###### Thermodynamic Energy Equation

In the absense of diabatic heating and for a small Rossby number, the QG thermodynamic energy equation can be written as,

```{math}
  \begin{equation}
    \frac{D\theta}{Dt_g} = -w\frac{d\hat{\theta}}{dz}
  \end{equation}
```

This says that the perturbation in potential temperature following a geostrophic flow changes due to vertical advection of a "basic state" potential temperature.

Interactions between the jet stream and extratropical weather systems are captured in the advection terms of the PV equation.

Following Geostrophic motion, geostrophic vorticity changes to stretching of ambient planetary rotation.


##### Qusai-Geostrophic Potential Vorticity

The QGPV equation is essentially a linearisation of the Ertel PV. This means separating it into the base state and perturbations, substituting inot the governing equations i.e. equation of motion, continuity equation, conservation of energy etc., and removing non-linear terms. This gives the equation,

```{math}
  \begin{equation}
    \frac{D}{Dt_g}\frac{1}{\rho_0}\frac{d\hat{\theta}}{dz} q = 0
  \end{equation}
```

where $t_g$ is the geostrophic component, $\hat{\theta}$ is the base state potential temperature, and $q$, the QG potential vorticity, is,

```{math}
  \begin{equation}
    q =\zeta_g + f + f\frac{\partial}{\partial z}\bigg( \frac{d\hat{\theta}}{dz}^{-1} \theta \bigg)
  \end{equation}
```

hence, QGPV is a conserved quantity. This is a very important concept for midlatitude weather systems, e.g. storm tracks! One way to view this, is that QGPV is made up of the contributions from the vertical component of vorticity and the disturbance static stability. _QGPV represents all of the fundamental conservation laws in a single equation._ It also states that QGPV is completely determined by the three-dimensional pressure field.

```{note}
All governing equations have a QG equivalents, see the Holton & Hakim chapter for full set.
```


##### "PV Thinking"

Using PV to describe atmospheric dynamics is very powerful as it encases the three conservation laws in a very simple form. "PV Thinking" has two aspects, inversion and conservation. Inversion is a kinematic diagnostic technique that allows any field variable to be recovered from the PV equation. Variables include the geostrophic wind and potential temperature field. This process is done by inverting the QGPV and solving with boundary conditions.


