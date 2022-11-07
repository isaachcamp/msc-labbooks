# Ensemble Consensus on Projections

## Robustness and uncertainties in the new CMIP5 climate model projections {cite}`knutti_robustness_2013`

There are only modest improvements from CMIP3 to CMIP5 in narrowing uncertainties in projections of key quantities, in this case, temperature and precipitation. The authors argue that although convergence to a more certain value will remain slow, the considerable improvement in representation of physical processes provides greater confidence in the projections.

They use a measure of Robustness to quantify model agreement which uses the signal-to-variability ratio and considers magnitude of change, sign, natural variability and inter-model spread. They find internal variability within a model is large enough to obscure a signal in the near-term, but robustness is better as emerging signals become more pronounced. They also find though there is consistency between CMIP generations, there is little improvement in model agreement.

Robustness is defined in Weigel, A., Liniger, M. & Appenzeller, C. The discrete Brier and ranked probability skill scores. Mon. Weath. Rev. 135, 118-124 (2007).

They provide hypotheses for these findings:

"_There are several hypotheses that potentially explain the lack of convergence and associated reduction of uncertainty. There could be (1) inherent limitations in the way models are built given limited computational resources and spatial resolution, (2) lack of process understanding, (3) lack of accurate long term observations to constrain models, (4) lack of consensus on metrics of present-day model performance that clearly separate better from worse models in terms of projection quality, (5) inherent limitation of climate change not being predictable owing to internal variability, (6) addition of dissimilar models from institutions new in CMIP5 and (7) addition of new processes, components, or forcings in CMIP5 that are not well understood, not well represented in the model, or not well constrained by observations._"


## Mapping model agreement on future climate projections {cite}`tebaldi_mapping_2011`

The authors argue that not considering internal variability leads to misinterpretation of results, and unreliable conclusions about the degree of consensus, or lack thereof, between models. They highlight how studies of trends of some variables with low signal-to-noise ratios conflate a lack of information with a lack of consensus; this is particularly pertinent to short-term predictions on small-scales where internal noise is prominent. They propose a method for distinguishing between the two cases, when low signal-to-noise ratios or model disagreement are concerned.

The method is as such:

"_1) Test for significant change in each of the models individually with a t-test comparing the mean of the reference and the future period, 2a) if less than X = 50% of the models show a significant change then show the multimodel mean change in color, 2b) if more than 50% of the models show significant change then test for agreement in sign by the following criteria, 3a) if less than Y = 80% of the significant models agree on the sign then show the grid point as white, 3b) if more than 80% agree on the sign show it in color with stippling._"

Only one realisation from each model is required for this simple method. Could I combine this with the FDR method to ensure t-tests aren't considered completely independent? They say there was no appreciable difference using it, but it would be consistent with the rest of the study...


## The use of the multi-model ensemble in probabilistic climate projections {cite}`tebaldi_use_2007`

Identify the relative merits of a number of methods used to create probability density functions (PDFs) to quantify the uncertainty in projections from a MME. They also relate the challenges faced when implementing such an approach.


## Challenges in Combining Projections from Multiple Climate Models {cite}`knutti_challenges_2010`

The authors outline various problems with constraining uncertainty in projections made from MMEs. 

First they mention errors in estimating the Prior Distribution, which, in a Bayesian framework, is the initial best guess of the true distribution. If the uncertainty in the variance of the prior distribution is underestimated this could mean that extremes of the distribution are missed, leading to severe impacts being underestimated too. It seems likely that the prior distribution does not capture the full range of feasible models.

Another issue is the presence of systematic biases, which are shared across all models. They show that the RMS error of a MME converges to a value greater than zero as the ensemble size increases, indicating the MME bias is correlated across models. They also show that choosing a few good models has a lower RMS, therefore weaker systemic bias, and converges upwards, also their distribution of bias values at grid points in space is much smaller and centred around the zero value.

They also indicate the interrelation of models, inherited biases through sharing code and shared understanding/knowledge of processes. However, many studies on projections assume model independence, and that each model realisation is a valid random observation, hence statistics using the assumption of random independence are used to qunatify uncertainty. This is a false assumption, and a true measure of independence between models drastically reduces the number of models that can be assumed independent.

They suggest that identifying a meaningful metric for quantifying model performance is difficult, and results from a subset of "best performing" models are often indistinguishable from that of a unweighted ensemble.

One final problem stated is the potential for loss of signal in MME means. This can result from spatial variability in the location where individual models project changes will occur; if there is a difference in the sign of a change, the signal can be lost entirely. This is particularly important for quantities with high spatial variability, such as precipitation.

They conclude that metrics able to evaluate models effectively by linking representational accuracy to probabilistic projections are needed. They also consider the use of process-focussed approaches to be important.
