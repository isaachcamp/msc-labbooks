# Reasons for CMIP6 & CMIP5

## An Overview of CMIP5 and the Experiment Design, Taylor et al. 2012 {cite}`taylor_overview_2012`

The Coupled Model Intercomparison Project phase 5 (CMIP5) is an initiative of the World Climate Research Programme (WCRP) Working Group on Coupled Modeling (WGCM). The goals of the CMIP projects are to coordinate the climate modeling community for greater accuracy in simulating past and predicting future climate; and to engage scientists outside the modeling community enabling more effective and impactful model analysis in a timely fashion. "WCRP-supported research provides the climate science that underpins the United Nations Framework Convention on Climate Change" (_https://www.wcrp-climate.org/about-wcrp/wcrp-overview_). The form the project took grew out of consultation with a number of groups with vested interests, such as climate impacts scientists. 

Direct Quotation:

> CMIP5 will notably provide a multimodel context for:
> 
> - 1) assessing the mechanisms responsible for model differences in poorly understood feedbacks associated with the carbon cycle and with clouds
> - 2) examining climate “predictability” and exploring the predictive capabilities of forecast systems on decadal time scales
> - 3) more generally, determining why similarly forced models produce a range of responses.

Scenario runs offer a way of evaluating/predicting the future climate. 

CMIP5 uses Atmosphere-Ocean Global Climate Models (AOGCMs), not ESMs, as they are more complex. ESMs are limited to long-term experiments, whereas AOGCMs are also used on decadal experminets (10-30 years).

Four fundamental considerations/limitations of using CMIP5 model output:

- Models (the historical experiment namely) simulate natural variability but are run independently of observations, therefore it is not expected that quasi-regular oscillations such as ENSO will occur concurrently with those observed.
- An experiment, once begun, shifts from pre-determined initial conditions into a state of equilibrium. This shift occurs over the course of a control run, however, most experiments are only run for a period of a few hundred years. A return to equilibrium cannot be expected over the short timescales that the control simulations occur, and it is unsafe to assume a state of equilibrium. There may remain a residual drift toward an equilibrium, therefore those analysing trends in model output from a particular forcing experiment must consider this. One suggestion is to subtract the piControl experiment results from the chosen experiment to remove this drift, leaving only the forced trends.
- Climate noise occurs as a result of natural variability, so that is not expected that the observations and model output will be the same. However, differences between them can be significance tested by the using the ensemble of model runs to characterise a sample. If the state being compared is well outside the ensemble average, it could be considered significant.
- Multi-model ensembles, assuming they are all somewhat independent, are a good way to examine how the future climate state will look. In our case, it will also be good for diagnosing biases. Some variation in how the mean state presents will be a result of climate noise, which must be diagnosed by using an ensemble of model runs, therefore you can conclusively say that one model is better than another as the model run that was selected may be outside of the ensemble average -- an average which could be highly representative of the observed mean state.


## Overview of the Coupled Model Intercomparison Project Phase 6 (CMIP6) experimental design and organization, Eyring et al. 2016 {cite}`eyring_overview_2016`

CMIP6 develops on the foundation laid by previous CMIPs.

Direct Quote:

> The CMIP6 newly-organised structure consists of three major elements:

> - (1) a handful of common experiments, the DECK (Diagnostic, Evaluation and Characterization of Klima) and CMIP historical simulations 1850–near present) that will maintain continuity and help document basic characteristics of models across different phases of CMIP; 
> - (2) common standards, coordination, infrastructure, and documentation that will facilitate the distribution of model outputs and the  characterization of the model ensemble;
> - (3) an ensemble of CMIP Endorsed Model Intercomparison Projects (MIPs) that will be specific to a particular phase of CMIP (now CMIP6) and
that will build on the DECK and CMIP historical simulations to address a large range of specific questions and fill the scientific gaps of the previous CMIP phases.

> CMIP6 will address three broad questions:

> - How does the Earth system respond to forcing?
> - What are the origins and consequences of systematic model biases?
> - How can we assess future climate changes given internal climate variability, predictability, and uncertainties in scenarios?

> This effort (to standardise model output and provide model descriptions) is now continuing under the banner of the
international ES-DOC activity, which establishes agreements
on common Controlled Vocabularies (CVs) to describe models and simulations. Modelling groups will be required to
provide documentation following a common template and
adhering to the CVs. With the documentation recorded uniformly across models, researchers will, for example, be able
to use web-based tools to determine differences in model versions and differences in forcing and other conditions that affect each simulation. Further details on the CMIP6 infrastructure can be found in the WIP contribution to this special
issue.

_Check out the above for model descriptions!_

Refer back to this reference as it has many tools for intermodel evaluation.
