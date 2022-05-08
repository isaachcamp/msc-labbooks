# Week 4

This lab notebook belongs to a set of [preliminary research](preliminary_research.md).

## 2022 Mar 21

### A new zonal wave 3 index for the Southern Hemisphere {cite}`goyal_new_2022`

A pair of indices are introduced to characterise ZW3 more effectively. These new indices are based on the first two EOFs of meridional wind anomalies (and raw data) and successfully capture both magnitude and phase of the quasi-stationary zonal wave. This is a marked improvement on the Raphael 2004 index, increasing the amount of variance contained within the indices from 16% to 40%. The introduction of two indices over just a single index is justified due to the phase being of great importance in explaining some climatological patterns seen, in this case study the Antarctic sea-ice extent is used, in which a strong relationship between the two is established, with sea-ice extent exhibiting a clear ZW3-like pattern. 

The main flaw in the Raphael index was the station data used cannot capture the phase change of ZW3, leading to false positives and false negatives. It also couldn't be applied to CMIP6 or CMIP5 model output given that the station doesn't exist in those models, and a nearby datum would need to be used. The new indices suffer from neither problem.


#### Major Findings

- Indices explain 40% of the variance observed in meridional wind anomalies.
- Better differentiation between strong and weak ZW3 events is achieved.
- Seasonal cycle in phase and magnitude, exhibiting a phase shift of 20-40 degrees and stronger mean magnitude in austral winter.
- Strong relationship between sea-ice extent and ZW3 magnitude and phase.
- Significant relationship between meridional heat transport and ZW3 magnitude.


#### Data

- ERA5 500hPa meridional wind & geopotential height anomalies.
- Uses CESM2 historical model for the last 1200 preindustrial years in order to find more robust results for connections between ZW3 and sea-ice and heaat transport - _justified? What impacts does this have?_

Meridional wind field was used as it can be directly associated with momentum and heat transport. 


#### New Index

PCA analysis of meridional wind field indicates that the first two EOFs encapsulate the variability of ZW3, 40% of the total variance. As the two are orthogonal, both are required to fully describe ZW3, and the phase can be found by finding the angle between the magnitude of both. The two indices are defined as: 

```{math}
    \begin{align}
      \lvert ZW3\rvert = \sqrt{PC1^2 + PC2^2}\\
      ZW3\ phase = \arctan{\frac{PC1}{PC2}}
    \end{align}
```

First anomalies of the meridional wind field were used with the new indices, then the raw data was used to try to identify a seasonal cycle in the phase - _what does this mean? Wilkes suggests PCA on anything other than anomalies is non-sensical, as do the CDO docs._

The indices were also applied to CMIP6 model output, however some possess EOFs that were either not connected to ZW3, instead ZW4, and others had the third EOF connected to ZW3. Therefore it is important to inspect the results of the PCA before applying the indices - _very relevant_.


#### Seasonality

Austral winter possesses the strongest ZW3 events on average, summer the weakest. However there is strong variability in all months, corroborated by Renwick 2005. Also identified is where the strongest signal is located, the South Pacific - _why? Look in Renwick 2005_. There was no clear phase seasonal cycle using the deseasonalised data, however there was a clear cycle with the raw data of a  20-30 degree shift.


#### Atmospheric Meridional Heat Transport (AMHT)

Significant relationship, up to a 99% confidence level, identified between ZW3 magnitude and AMHT, suggesting that ZW3 has an important role to play in heat transport poleward. Strong ZW3 events means stronger AMHT poleward.


#### Antarctic Sea-ice Extent

Sea ice is more expansive during August-September-October months, hence only this season is used in analysis. Phase and magnitude assumed to be important, hence the strongest 50% of ZW3 events (greater than the median) were split into phase groups of 20 degrees. Findings:
- Clear ZW3-like pattern in sea-ice anomalies.
- Stronger anomalies in South Pacific and Atlantic around Ross sea, Amundsen-Bellingshausen and Weddell seas, consistent with strongest ZW3 nodes.
- Positive sea-ice anomalies align with northward wind anomalies, and netive sea-ice anomalies with southward wind anomalies, where wind anomalies are suggestive of heat transport, hence greater northward winds are linked with stronger equatorward heat transport and more sea ice.
- Sea-ice anomalies phase shift with ZW3.


#### Papers Referenced

- Campitelli et al. 2021, associated asymmetrical component of SAM with ZW3 variability.
- Renwick 2005, strong variabilty in ZW3 all year round, also that the strongest ZW3 signal lies in the South Pacific.
- Goyal et al. 2021, ZW3 generated by tropical SST anomalies, not SH orography as previously suggested.


### Meeting with James

- Need to match the temporal and spatial resolution of models to ERA5 as much as possible. Will have to think about whether we can apply Goyal indices to model output.
- Can use data from 20S, ignoring northward of this latitude.
- When finding the EOF, it is essentially finding a set of basis vectors, and the PC quantifies how well a given vector x maps to that basis vector. This could be interesting in exploring patterns correlations, or mapping patterns of two circulation phenomena, e.g. SAM and ENSO.


#### To Do

- Look for statistical technique for correlating/significance testing patterns.


### Zonal wave 3 pattern in the Southern Hemisphere generated by tropical convection {cite}`goyal_zonal_2021`

Goyal et al. uses a series of experiments with an AGCM to establish that tropical convection forced by the presence of land in the tropics generates ZW3. The essential idea is that deep tropical convection sets up a local Hadley cell, with tropical upper-level divergence and sub-tropical upper-level convergence. The convergence in the sub-tropics acts as a Rossby wave source, exciting a poleward and eastward Rossby wave train that is deflected equatorward by wave guides at high latitudes and decays in the tropics. This forms a quasi-stationary wave in the form of ZW3.

ZW3 is prominent in the geopotential height and meridional wind fields, and dominates zonally asymmetric extratropical circulation at submonthly, seasonal and interannual timescales. It is at its strongest at 55S. ZW3 plays a key role in poleward heat and momentum transport.

```{note}
CMIP5 underestimates ZW3 amplitude - is this still true of CMIP6?
```


#### Major Findings

- ZW3 generated by tropical convection events, driven by asymmetry in SSTs.
- Phase of ZW3 is related to the longitudinal location of the Rossby wave source in the sub-tropics.


#### Data & Experimental Set-up

Uses data from the NCEP CESM2 model, using 1200 years pre-industrial. CESM2 is forced by prescribed SSTs and sea-ice and uses realistic land mass & orography. On the model run-through, the model is forced by geographically and climatologically varying SSTs. A series of experiments were run with differing land-ocean and SST configurations, building model complexity from a basic aquaplanet, to realistic land mass & orography.

#### Response to Land Mass

Found that a single flat tropical land mass can trigger a phase-locked ZW3, a quasi-stationary wave. Whereas an aquaplanet and a model with sub-tropical land mass only does not create ZW3-like waves, no "phase-locking" or stationary waves. It is suggested that the presence of sub-tropical land has little to no effect on generating ZW3, in contrast to explanations given in previous literature. Introducing realistic orography had little significant effect either.

They conclude that land mass in the tropics causes low-level convergence resulting in deep adiabatic convection events resulting in a Rossby wave train.


#### Mechanism

Tropical land presence provides a pertrubation to the mean flow causing low-level/surface convergence. This results in convective heating and increased vertical motion, creating upper-level tropospheric divergence. This creates a local Hadley cell, causing upper-level convergence and sinking in the sub-tropics. This set up acts as a Rossby wave source, creating a Rossby wave train that propagates poleward and eastward. Wave guides in the high latitudes, where absolute vorticity is zero, reflect the wave train equatorward where it eventually decays in the tropics, where zonal wind tends to zero (Rossby wave trains require westerlies to propagate). This sets up a ZW3-like signal - a quasi-stationary wave with three highs and three lows.

Rossby wave trains can be forced by a number of tropical convection events, relating to Madden-Julian Oscillation, monsoons, IOD and ENSO positive events. 


#### Trends

Changes to ZW3 depend on tropical SST warming as well as changes to SH circulation patterns like ENSO and IOD. Warming is expected to weaken teleconnections through to mechanisms:
- weakening convective circulation.
- Amplified upper tropospheric warming causing static stability, decreasing the amount of vertical motion.

Westerly winds are projected to increase with warming. Stationary wave theory states that wave number inversely proportional to zonal flow strength, suggesting that the wavenumber of the stationary wave created by tropical convection events may decrease in the future.


## 2022 Mar 22

(index-processing)=
### Calculating SAM Index

A time series for the SAM Index is calculated using PCA analysis of the monthly mean variance field of the deseasonalised 500hPa geopotential height.

Script used by Raapoi, calc_sam_pc1.sh:

```
#!/bin/bash
#SBATCH --cpus-per-task=20
#SBATCH --mem=5G
#SBATCH --partition=parallel
#SBATCH --time=16:00:00
#SBATCH -o /nfs/home/campbeisaa/pca_analysis.out
#SBATCH -e /nfs/home/campbeisaa/pca_analysis.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=isaac.campbell6@googlemail.com

# Load required modules
module use /home/software/tools/eb_modulefiles/all/Core
module load foss/2021a
module load CDO/1.9.10

# Calculate monthly mean variance field
cdo monmean era5_h500_daily_1979_2021_1deg_deseasonalized_20S.nc era5_h500_daily_1979_2021_1deg_deseasonalized_20S_mon_anoms.nc

# Calculate all EOFs of the monthly mean variance field and output file for first EOF (and a separate file of all EOFs by default)
cdo eof,1 era5_h500_daily_1979_2021_1deg_deseasonalized_20S_mon_anoms.nc era5_h500_daily_1979_2021_1deg_deseasonalized_20S_eofs.nc era5_h500_daily_1979_2021_1deg_deseasonalized_20S_eof1.nc

# Calculate the first principal coefficient
cdo eofcoeff era5_h500_daily_1979_2021_1deg_deseasonalized_20S_eof1.nc era5_h500_daily_1979_2021_1deg_deseasonalized_20S_mon_anoms.nc obase

# Invert time series and divide by g for units in metres
cdo divc,-9.81 obase00000.nc obase00000_PC1.nc

# Normalise PC1 by subtracting long term mean and dividing by the standard deviation of the time series.
# Calculate mean and subtract from PC1 time series
cdo timmean obase00000_PC1.nc obase00000_PC1_mean.nc
cdo sub obase00000_PC1_mean.nc obase00000_PC1.nc PC1_anoms.nc
cdo timstd obase00000_PC1.nc PC1_std.nc
cdo div PC1_anoms.nc PC1_std.nc sam_pc1_normalised.nc
```

### Obtaining SOI and DMI time series

Both time series were collected from NOAA website ([see Week 3 Notebook for details](week3.md)).

Raw data was copied and saved as a .txt file. After which a python script was created to convert the data into a netCDF time series file with accompanying metadata. 

Example script for creating SOI .nc file:

```{code}
import numpy as np
import pandas as pd
import xarray as xr

path = 'G:\\Isaac\\Documents\\msc-research\\data\\indices\\raw_data\\'
filename = 'soi_noaa.txt'
    
with open(path + filename, 'r') as f:
    lines = f.readlines()

time_series_list = []

for line in lines:
    line = line.strip(' \n').split(' ')[1:]
    data_line = [x for x in line if x != '']
    time_series_list.append(data_line)
    
data_series = np.array(time_series_list)
data_series = np.reshape(data_series, (np.size(data_series),1))
data_series = data_series.astype(float)

idx = pd.date_range('1979-01-31', periods=np.size(data_series), freq='M')
time_series = pd.DataFrame(data_series, index=idx)
time_series.rename(columns={0:'SOI'}, inplace=True) 
time_series.index.rename('time', inplace=True)

ts = time_series.to_xarray()
ts.attrs = {'frequency':'monthly', 
            'source':'https://www.cpc.ncep.noaa.gov/data/indices/soi', 
            'history':'created using "read_txt_datafile.py"',
            'data range':'Jan 1979 - Dec 2021'
            }

ts.SOI.attrs = {
    'standard_name':'SOI', 
    'long_name':'Southern Oscillation Index', 
    'units':'dimensionless',
    '_FillValue':-9999.00
    }
print(ts.var)

ts.to_netcdf("soi_noaa.nc")
```

## 2022 Mar 23

### Emergence of Climate Change in the Tropical Pacific {cite}`ying_emergence_2022`

This paper uses a multi-model ensemble to detect projected changes of ENSO, as well as establishing a timescale on which the signals of these trends may occur. They find that ENSO-related SSTs are expected to rise and become a "detectable" signal by 2070, and the trend of increasing ENSO-related rainfall will become apparent by 2040 - higher precipitation from warmer temperatures follows the basic analysis that "warmer is wetter". On this, all models agree around precipitation, however there is much inconsistency between models regarding rising SSTs, some predicting no change, others the complete opposite (see paper for references). These ENSO-related signals, established by Ying et al., are exaggerated in comparison to the global average i.e. rising at a faster rate.

The SSTs in the Eastern Pacific are projected to be some of the fastest changing (increasing) temperatures in the world, likely producing a weaker east-west Pacific SST gradient - an event strongly linked to El Nino warm events. _This may result in higher frequency and amplitude El Nino warm events._


### IPCC AR6 WG1 Chapter 2 - ENSO Trends {cite}``

Main conclusions are that there are no significant trends that can be surmised from observations in the instrumental period. 

#### ENSO Behaviour over Instrumental Period

- No indication of systematic trend, but there is evidence from recent observations (1979-2009) that amplitude is higher during this period than before 1979.
- Some studies find a weakened Pacific SST gradient, however one study suggests that studies using proxies for pre-instrumental period may be based on false assumptions, as proxies underweight weakening in Central Pacific (CP) region, hence there may instead have been a shift of ENSO towards the central Pacific rather than weakening.
- Some studies find possibly higher variability in recent decades than previous, others do not.
- No concerted shift in teleconnections.

#### Summary

Medium confidence that amplitude and frequency of high-magnitude events are higher since 1950 than between 1850-1950. However there is low confidence that this constitutes from prior to 1400. There is no indication of a sustained shift in ENSO behaviour or associated phenomena from using proxies (pre-1850) and instrumental data. However there appears to be (low confidence) a shift in CP events over Eastern Pacific (EP) - _read Timmerman et al. 2018 for description of these to ENSO event types._


## 2022 Mar 24

### Time Series Chapter in Wilks {cite}`wilks_statistical_2006`

#### Summary

This chapter focuses on the ability to fit models to time series data. For my purposes, I am working with continuous data, meaning that autoregression methods are most useful in the time domain. By fitting higher order autoregression models to time series, this could result in accurately representing non-linear components of atmospheric variables. However, the exact application remains unclear to me. Do I need to have a single-valued metric first, or can I apply the regression model to the whole field independently? 


#### Stationarity

Stationarity is the assumption that the distribution of values observed for a time series is not dependent on time, i.e. a time fragment at one end of the series will be statistically similar to a time fragment taken from the other end. This assumption is important, as a number of other statistical assumptions are valid if this is true. For example, a point in time is loosely correlated with points only a few time steps away, but whose correlation depends only on the time separation, or lag, k. This is important for accounting for the correlation in time series.

Most atmospheric variables are not stationary, but exhibit annual and diurnal cycles. To transform into a stationary function, the variable must be transformed into standardised anomalies, meaning subtracting the mean monthly value and dividing by the monthly standard deviation -- otherwise known as deseasonalisation. This has the effect of making the mean value of the time series zero, as well as normalising the amount of variance for each time step. This is necessary because, for example, not only do temperatures in the high latitudes vary between seasons, they also exhibit a much higher degree of variability in winter than in summer.

Stationarity can be understood as the sample have a zero-mean, hence linear detrending can create a stationary dataset if a lingering trend is observed, e.g. is rising mean global temperature.


#### Time Series Models - Time Domain

Fitting time series models to observed data allows you to use the statistical properties of the data to forecast future observations. This is particularly so if the assumption of stationarity is true, allowing you to assume that future observations will possess the same statistical properties as the dataset at hand.


##### Markov Chains - Discrete Data

Markov chains are a way of representing the correlation between successive time steps of discrete data i.e. the possible states are discretised. It does this by assuming different probabilities of moving into any other given state, based solely on the current state that the system is in. Given a state i, the probability of moving into another given state j is dependent only on state i, which would be much more probable if closer to i in the phase space which they both occupy. The mathematical function used to define probabilities is most frequently an exponential term.

The probability parameter for Markov chains is defined as the "conditional relative frequency":

```{math}
  \begin{equation}
    p_{ij} = \frac{number\ of\ times\ state\ j\ succeeded\ current\ state\ i}{number\ of\ times\ state\ i\ occurred}
  \end{equation}
```
These are transition probabilities, which, for a two-state system, are related to "stationary probabilities by:

```{math}
  \begin{equation}
    \pi_i = \frac{p_{ji}}{1 + p_{ji} - p_{ii}}
  \end{equation}
```

where the number of $p_{ji}$ is governed by the number of possible states, i.e. for s-states, $j = 1,..., s$. Transition probabilities imply a serial correlation, defined by the a "persistence parameter", $r_i$, where:

```{math}
  \begin{equation}
    r_i = p_{ii} - p_{ji}
  \end{equation}
```

where again j can take on the values $j = 1,..., s$, describing the autocorrelation between states i and j. This implies that state i is more likely to follow the current state i than another state j, resulting in a clustering effect. This defines the autocorrelation between successive time steps, and can be extended to an interval of multiple time steps by:

```{math}
  \begin{equation}
    r_k = (r_{i})^k
  \end{equation}
```

Implying that although the current state of the system is the only information used to determine the following state, that does not mean that states multiple time steps away are independent, but remain correlated to the current state, if only loosely.


###### Testing for Serial Correlation

It is possible to test for independence/serial correlation using a form of $\chi ^2$-test. Taking the null hypothesis to be that the time series is serially independent:

```{math}
  \begin{equation}
    \chi ^2 = \sum_{i} \sum_{j} \frac{(n_{ij} - e_{ij})^2}{e_{ij}}
  \end{equation}
```

where $n_{ij}$ is the number of counts for transitions between states i and j, $e_{ij}$ is the expected count of transitions between states i and j, defined as: 

```{math}
  \begin{equation}
    e_{ij} = \frac{(number\ of\ times\ state\ i\ occurred)(number\ of\ times\ state\ j\ occurred)}{total\ number\ of\ events\ in\ time\ series}
  \end{equation}
```

The value obtained from evaluating this test can be directly compared to a comparison table, found in the appendix.


###### Higher Order Markov Chains

It is possible to develop Markov chains that depend on the state of the preceding m time steps -- these are called $m^{th}$-order chains. Here, the transition probabilities become:

```{math}
  \begin{equation}
    p_{hij} = \frac{n_{hij}}{n_{hi\bullet}}
  \end{equation}
```

where $n_{hi\bullet}$ represents the number of times event h was succeeded by i occurred, disregarding the following state.


##### Autoregression - Continuous Data

A continuous analogue of the Markov Chain. 


###### First Order Autoregression AR(1)

Can be viewed as a simple linear regression model:

```{math}
  \begin{equation}
    x_{t+1} - \mu = \phi(x_t - \mu) + \epsilon{t+1}
  \end{equation}
```

where $\mu$ is the time series mean, $\phi$ is the autoregression parameter and $\varepsilon_{t+1}$ is a random quantity corresponding to the residual in ordinary regression. The random quantity provides a "shock" to the regression. $x_{t+1}$ represents the predictand, the quantity to be predicted in the next time step, and $x_{t}$ is the predictor, the value of the current time step.

This essentially works by subtracting the mean $\mu$ from an initial value $x_0$, multiplying by the autoregressive parameter $\phi$ and adding a random variable $\varepsilon$, where $\varepsilon$ is drawn from a Gaussian distribution with zero mean and variance $\sigma_{\varepsilon}^{2}$. Finally, the mean is added again to give a value for the next time step, $x_1$. This process is repeated for succeeding time steps to create a time series for $x$.

As with the Markov chain, only the preceding state contributes information for the calculation of the following state, hence AR(1) is often called the Markov process.

Importantly, the autoregressive parameter $\phi$ is equivalent to the autocorrelation coefficient defined for Markov chains.

```{math}
  \begin{equation}
    \hat{\phi} = r_1
  \end{equation}
```

and similarly, for k time steps ahead, the two states are correlated according to:

```{math}
  \begin{equation}
    \rho_k = \phi^k
  \end{equation}
```

For a sufficiently long time series, $\hat{\phi}$ can be assumed to be Gaussian, with $\mu_{\phi} = \hat{\phi}$ and $\sigma_{\phi}^2 = (1 - \phi^2)/n$, therefore a test can be carried out, with a null hypothesis of $\phi = 0$ i.e. no correlation:

```{math}
  \begin{equation}
    z = \frac{\hat{\phi} - 0}{[Var(\hat{\phi})]^{1/2}} = \frac{\hat{\phi}}{[1/n]^{1/2}}
  \end{equation}
```

essentially a t-test.

The final variable, the "white noise" signal $\varepsilon$, is also assumed Gaussian, with a zero-mean and a variance that can be estimated by:

```{math}
  \begin{equation}
    \sigma_{\varepsilon}^2 = (1 - \phi^2)\sigma_{x}^2 
  \end{equation}
```

where $\sigma_{x}^2$ is the variance of the observations.


###### Higher Order Regressions AR(K)

Where the succeeding state is dependent on the state of the previous K states:

```{math}
  \begin{equation}
    x_{t+1} - \mu = \sum_{k=1}^{K}\phi_{k}(x_{t -k + 1} - \mu) + \varepsilon_{t+1}
  \end{equation}
```

where there are now K lots of autoregression parameters, $\phi_{k}$. These can be determined using the Yule-Walker equations, which relate the autoregressive pareameters to the autocorrealtion function.

Particularly important is the AR(2) model that can describe a variety of different time series behaviours. The regression equation here, and Yule-Walker equations are:

```{math}
  \begin{align}
    x_{t+1} - \mu = \phi_{1}(x_{t} - \mu) + \phi_{2}(x_{t - 1} - \mu)+ \varepsilon_{t+1}\\
    r_1 = \hat{\phi}_1 + \hat{\phi}_2 r_1\\
    r_2 = \hat{\phi}_1 r_1 + \hat{\phi}_2
  \end{align}
```

and the two auroregressive parameters can be estimated by (by solving the above Yule-Walker equations): 

```{math}
  \begin{align*}
    \hat{\phi}_1 = \frac{r_1(1-r_2)}{1-r_1^2}\\
    \hat{\phi}_2 = \frac{r_2-r_1^2}{1-r_1^2}
  \end{align*}
```

For AR(2) to be stationary, it must satisfy the constraints:

```{math}
  \begin{align}
    \phi_1 + \phi_2 < 1\\
    \phi_2 - \phi_1 < 1\\
    -1 < \phi_2 < 1
  \end{align}
```

AR(2) models can represent barometric pressure variations from the movement of midlatitude synoptic systems, as they are able to create damped periodic oscillatory functions.


###### Variance of a Time Average

Atmospheric data is often correlated, reducing the amount of variance observed as the succeeding data is constrained by the preceding. Therefore, when conducting hypothesis testing, a null hypothesis can often be rejected incorrectly due to the variance being minimised. To account for this, a vairance inflation factor, V, can be applied. If the data is uncorrelated, $V = 1$. 

```{math}
  \begin{equation}
    \frac{1 - \sum_{k=1}^{K}\phi_k \rho_k}{[1 - \sum_{k=1}^{K}\phi_k]^2}
  \end{equation}
```

where $\rho_k$ is the autocorrelation function of the $k^{th}$ order, defined in Wilks chapter.


## 2022 Mar 25

### Time Series Chapter in Wilks {cite}`wilks_statistical_2006`

#### Frequency Series Models - Frequency Domain

##### Spectral Analysis

Represents time series as a series of sines and cosines and Fourier coefficients:

```{math}
  \begin{equation}
    y = \bar{y} + \sum_{k=1}^{n/2}\bigg\{ A_k\cos{\bigg[ \frac{2\pi kt}{n}\bigg] } + B_k\cos{\bigg[ \frac{2\pi kt}{n}\bigg] }\bigg\}
  \end{equation}
```

where the Fourier coefficients $A_k$ and $B_k$ are,

```{math}
  \begin{align*}
    A_k &= \frac{2}{n} \sum_{t=1}^{n} y_t\cos{\bigg(\frac{2\pi kt}{n}\bigg)} \\
    B_k &= \frac{2}{n} \sum_{t=1}^{n} y_t\sin{\bigg(\frac{2\pi kt}{n}\bigg)}
  \end{align*}
```

A Fourier power spectrum can be used to plot the amplitudes for each harmonic in the series. The amplitude or magnitude squared is plotted only, therefore the times at which these signals are at their peak (phase) are not indicated. Each harmonic may represent a different process happening on varying timescales/frequencies, e.g decadal or seasonal, or diurnal.

The Nyquist frequency is the highest possible frequency, $\omega_{n/2} = \pi$, which executes a whole cycle over just two timesteps, and $n/2$ cycles over the full data record. It imposes an important limitation on the amount of information that can be extracted from the data. This is because at a minimum two points are required for plotting a cosine graph, one peak and one trough. Thus discrete data can only represent explicitly variations that occur no faster than the Nyquist frequency. 


###### Aliasing

Importantly, variations that occur at higher frequencies than the Nyquist are attributed to lower frequencies, a phenomenon known as aliasing. This will cause the amplitude and phase of the lower frequencies to be biased, e.g. the amplitude of the higher frequency will be added to the amplitude of the lower frequency graphically represented by a Fourier spectrum. Due to the squaring of the Fourier coefficients when calculating the magnitude, this causes a folding pattern in the assignation of variation to lower frequencies i.e. frequencies just higher than the Nyquist frequency will be attributed to those just lower, whereas variations of very high frequencies will be attributed to very low frequencies. For this reason the Nyquist frequency is commonly referred to as the "folding" frequency. 

```{note}
Aliasing could be important when considering the diurnal cycle. What does this do to very low frequency signals?

Madden and Jones 2001 suggest that badly aliased spectra are expected unless averaging time is larger than the sampling interval.
```

It is useful to have knowledge of physical phenomena that cause variations as these can be accounted for, whereas exploratory analysis is more difficult. It is impossible to de-alias data once it's been taken, however for exploratory purposes, confidence can be taken if the signals toward the Nyquist frequency tend to zero.


###### Sampling Properties

Because data is subject to sampling fluctuations, i.e. fluctuations due to finite discrete data points not following an exact distribution, this can lead to power spectra being wildly inaccurate. The way to get around this might be to split the data into several samples to find an average power spectrum by adding the amplitudes together. This might however, smooth out some of the contributions by particular frequencies -- there is always a compromise between robustness and frequency resolution.