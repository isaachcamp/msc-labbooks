# Week 12

## 2022 May 24

### Persistent Positive Anomalies in the Southern Hemisphere Circulation {cite}`renwick_persistent_2005`

- What is the importance of linear detrending?

#### Summary

Clustering analysis of the 500hPa geopotential height field reveals two commonly occurring patterns: a ZW1 pattern; and a ZW3 pattern. There is a clear maximum anomaly in the south Pacific. A persistant positive anomaly (PPA) is defined as an anomaly in the 500hPa geopotential height field of at least 100m and lasting at lest 5 days. Blocking events are described as associated with a PPA in the higher latitudes, that is associated with a region of negative anomalies on the equatorward side, resulting in a 'split' or 'blocked' westerly flow.

Previous studies have either identified ZW3 pattern with limited data for the south Pacific -- using Australian observations, or, where data has been available, identified the south Pacific as the major blocking event in the SH, and downplayed the impact of ZW3. This paper argues that there are both ZW3 and ZW1 related PPAs, with the former having a weak connection to ENSO forcing, and the latter being strongly connected.

#### Major Findings

- Number of PPAs varies seasonally and zonally, reachin a maximum in the southb Pacific during austral winter.
- Notes an upward trend in the number of PPA events, consistent with the SAM trneding positive, however this could be an artefact of the uptake in satellite observations.
- 

#### Cluster Analysis

Three clusters are identified, with cluster 1 and 2 likely be linked to the changeover during the satellite era, with cluster 1 being the low resolution version of cluster 2. This is apparent from the drop-off in cluster 1 occurrence found around 1979, whilst there was a significant uptick in cluster 2 at around the same time. Clusters 1 and 2 have a ZW3-like signal, whilst cluster 3 is more ZW1-like, with a signal strong maximum located over the South Pacific. Cluster 3 has little seasonal cycle, though it does reach a maximum over austral winter.


#### Possible Forcings 

Cluster 3 (ZW1) has a clear linkage with the SOI, as documented in Kiladis & Mo 1998, Renwick 1998, Kidson 1999, Renwick & Revell 2001, Renwick 2002. _Check out these papers_. This refers to the blocking over the South Pacific that is closely-tied to ENSO, which is apparent in a lot of the correlation and composite maps. More frequent blocking events during El Nino events. 

ZW3 patterns have less certain forcing by ENSO, but indications of PPAs favoured during winter La Nina and spring El Nino. Notes the forcing of Rossby waves by ENSO and it's potential involvement in stimulating ZW3.

## 2022 May 25

### Assessment of zonally symmetric and asymmetric components of the Southern Annular Mode using a novel approach {cite}`campitelli_assessment_2021`

#### Summary

Campitelli et al. separate the SAM into three indices, one for the SAM as a whole, and two separate indices for the symmetric and asymmetric components. The indices are defined by regressing the geopotential height each of 37 atmospheric layers, 1000hPa to 1hPa, onto the asymmetric and symmetric components. Here they document temporal and spatial variability of both components, and look at linkages through the depth of the atmosphere, focussing on the manifestation of each component in the troposphere (700hPa) and stratosphere (50hPa).

They found that each component has distinct regimes of variability, and that the asymmetric component is the sole connection between the SAM and ENSO. The well-documented positive trend appears only to be present in the symmetric SAM index.

```{note}
The connection between A-SAM and ENSO is important for us as the ZW3 pattern of A-SAM has a strong maximum in the south Pacific, around the location of the Amundsen sea low. This is present in many of the figures produced so far, and is a key component in the variability of SAM. This means that the leading mode of variance are in fact the combination of ENSO and SAM.
```

_If the asymmetrical component is the only part of SAM that is connected to ENSO, why do we see a ring-like structure in variance and height corr/cov and composites for DJF, when ENSO pattern looks most like SAM?_

#### Indices

To define the symmetric SAM (S-SAM) and asymmetric SAM (A-SAM), they compute the zonal mean and anomalies of the geopotential height field, before calculating the leading EOF for these fields.

The A-SAM assumes linearity of response i.e. the positive phase is a mirror image of the negative. They suggest this is valid as there is a strong negative spatial correlation between composites of events with +/- 1 standard deviation.

#### Results

##### Temporal Evolution

The stratospheric imprint of SAM shows a significant oscillatory nature on the order of 20 months, and is therefore linked to the Quasi-Biennial Oscillation (QBO) (Baldwin et al. 2001, Vasconcellos et al. 2020). The most significant variability is found for ZW3 in the troposphere on the order of 3.6 months.

Correlations between A-SAM and S-SAM were found to differ between the stratosphere and troposphere, with consistent values of ~0.4 with zero-lag in the troposphere, before dropping to below 0.25 in the stratosphere. Whereas, with -1 lag (A-SAM keads S-SAM by one month), the reverse relationship is found, with there being a much lower (although consistent) correlation in the troposphere, before reaching a peak of 0.58 in the stratosphere.

Cross-correlations indicate that there is greater vertical coherence in SAM and S-SAM, whilst A-SAM is more incoherent.

##### Spatial Patterns

In the stratosphere, SAM has a symmetrical monopole structure, off-centre from the pole, reflected by the structure seen in the S-SAM. Interestingly, the A-SAM has a ZW1 pattern, with a high over South America, and low in the south Indian ocean. 

In the troposphere, S-SAM possesses the ring-like structure surrounding the oppositely-signed polar disc (with faint traces of ZW3 highs and lows), whereas A-SAM has the familiar ZW3 signal, and SAM is a combination of both. Notably, the ZW3 pattern of A-SAM is displaced by half a wavelength from the climatological mean phase as described by Raphael 2004 (_is this the case with Goyal's too?_).

Partial correlations between A-SAM & S-SAM and the Oceanic Nino Index (ONI), which quantifies the correlation between ENSO and SAM, show there is a statistically significant (moderated by False Discovery Rate (FDR)) relationship between A-SAM and ONI, but no such relationship exists between S-SAM and ONI. These results were repeated for the SOI and Multivariate ENSO Index (Wolter and Timlin 2011).

```{note}
Look at regression patterns with temperature anomalies (p11) and compare with generated figures, some of the A-SAM patterns look similar to ones that emerged from corr/cov and composite analysis.
```

#### Useful Citations

- "the main mode of variability in the Southern Hemisphere extratropical circulation (Rogers and van Loon 1982)"
- On the trends observed in SAM, "find large positive trends in summer, smaller in autumn and no trends in the other seasons (e.g., Fogt and Marshall 2020, and references therein)"
- "Fogt et al. (2011) showed that there is a significant relationship between the SAM and the ENSO", the Oceanic Nino Index quantifies the correlation between ENSO and SAM.


### “The Stippling Shows Statistically Significant Grid Points" How Research Results are Routinely Overstated and Overinterpreted, and What to Do about It {cite}`wilks_stippling_2016`

#### Summary 

This paper lays out a technique for interdependent multiple hypothesis tests and how significance can be established. This technique, known as the control of False Discovery Rate (FDR), is computationally simple and statistically principled. 

#### History of Significance Testing for Multiple Hypotheses

The paper outlines a couple of methods that have been used historically to try to solve this problem: Walker's Test; and Field Significance. Both assume that the hypothesis tests are independent, which is highly unlikely for a global field, what is much more likely is strong autocorrelation between grid points. The success of Walker's test is in how it accounts for the increasing likelihood of a vanishingly small p-value with increasing number of hypothesis tests. He proposed a modification to the chosen significance level:

```{math}
  \begin{equation}
    \alpha_{walker} = 1 - (1 - \alpha)^{\frac{1}{N_0}}
  \end{equation}
```

This however, is a very strict criterion for establishing significance, and can often fail to reject false null hypotheses. The second method mentioned is the field significance approach. This is a 'metatest', which defines a global null hypothesis which must be rejected in order for any local tests to be considered significant. This is done by assuming that a certain proportion of local tests, equivalent to the significance level, e.g. $\alpha = 0.05$, must be rejected before the global null hypothesis can be rejected. Two prominent issues arise from this approach, aside from the assumption of statistical independence:
   
- No account is taken of the magnitude of the p-value, and so not all the information is used to establish significance.
- If a global null hypothesis is rejected, this merely establishes the field in its entirety as significant, which could lead to an overinterpretation of seemingly coherent features present that did not in fact contribute to the rejection of the global null hypothesis. These features may not have any physical significance, but as they are present in a 'statistically-significant field', they may be subjected to overinterpretation.

#### False Discovery Rate Technique

This technique works by limiting the number of falsely rejected null hypotheses by using the statistically expected fraction of such rejections. p-values are sorted into ascending order and compared to the expected fraction, which is progressively more lenient with p-values. This takes account of both the magnitude of the p-values, as well as their distribution. This method can capture regional/feature significance allowing for interpretation of these results. The FDR is defined as:

```{math}
  \begin{equation}
    p^*_{FDR} = \big[p_{(i)}: p_{(i)} <= (i/N)\alpha_{FDR} \big]
  \end{equation}
```

Choosing $\alpha_{FDR} = 0.1$ is a reasonable estimate, as strong spatial autocorrelation tends to effectively double the usual significance level. Use this paper as a reference. _Find others_.

Even though this test assumes statistical independence, it is shown that the results are not too affected by highly correlated tests, as such it is appropriate for testing fields with spatial autocorrelation.

## 2022 May 26

### Eddy–Zonal Flow Feedback in the Southern Hemisphere {cite}`lorenz_eddy_2002`

#### Summary


