# Techniques for Model Analysis

## Evaluation of Climate Models, AR5, Flato et al. 2013 {cite}`flato_evaluation_2013`

Clouds:

"The simulation of clouds in climate models remains challenging. There is very high confidence that uncertainties in cloud processes explain much of the spread in modelled climate sensitivity. However, the simulation of clouds in climate models has shown modest improvement relative to models available at the time of the AR4, and this has been aided by new evaluation techniques and new observations for clouds. Nevertheless, biases in cloud simulation lead to regional errors on cloud radiative effect of several tens of watts per square meter. {9.2.1, 9.4.1, 9.7.2, Figures 9.5, 9.43}" SEE ALSO ch.7 for advances in cloud processes.

Storm Tracks:

"Models are able to capture the general characteristics of storm tracks and extratropical cyclones, and there is some evidence of improvement since the AR4. Storm track biases in the North Atlantic have improved slightly, but models still produce a storm track that is too zonal and underestimate cyclone intensity. {9.4.1}"

ENSO teleconnection:

"ENSO teleconnections outside the tropical Pacific, of relevance to Chapter 14"


### Multi-Model Ensembles

Components are often shared between modelling centres, which has led different models to inherit the same biases {cite}`masson_climate_2011`. This undercuts the notion of independent contributions to the model or parameter space -- a notion of encompassing all possible outcomes from model parameterisation and tuning, analogous to what phase space is to entropy -- and reduces the number of effective independent contributions {cite}`knutti_challenges_2010`. Pennell and Reichler (2011) was a number of methods to evaluate effective sample size and found it to be significantly lower than the true sample size of 24 -- between 3 and 15 {cite}`pennell_effective_2011`. This is a pertinent consideration when investigating model projections, and establishing statistical likelihood of such eventualities. 


It is often a good idea that extreme events simulations be assessed as well as time-mean averages. Knutti et al. 2010 -- possibly, but needs checking.

## Performance Metrics for Climate Models, Gleckler et al. 2008 {cite}`gleckler_performance_2008`

This paper investigates climate models using proposed objective metrics that quantify model performance. One of note is the RMS difference, E, between a model output field, F, and a reference field, R. They do this by summing the weighted square of the differences over longitude, latitude and time and dividing by the sum of the weights -- _Need to incorporate this method into our methodology_.


## Quantifying the agreement between observed and simulated extratropical modes of interannual variability {cite}`lee_quantifying_2019`

The authors investigate an array of large-scale modes of variability, SAM being the only relevant one for us. They use a method known as Common Basis Function (CBF) and compare the relative merits with the conventional EOF approach. The EOF approach requires comparisons between the EOFs of observations and models, swapping simulated EOFs to most closely match the leading EOF if they are disordered. 

Whereas, the CBF approach projects model anomalies onto the EOF derived from the observations, forming a "CBF-PC". They then linearly regress gridpoint the CBF-PC and simulated temporal anomalies to calculate the slope (the y-intercept is zero since they use temporal anomalies), then reconstruct a 3D space-time representation by multiplying the simulated anomalies by the slope at each timestep, from this can calculate explained variance. Finally, they calculate the spatial pattern by multiplying the slope at each gridpoint by the standard deviation of the CBF-PC.

They establish that CBF performs better by comparing the spatial correlations between models and obseravtions and find that models consistently perform better using the CBF method. _Taking the spatial correlations between the observations and models also provides us with a quantitative measure of model fidelity_.

_The CBF approach is quite lovely._ 

Arguably, it relies on the mode of variability being fully captured by the EOF analysis of the observational dataset. This may not be totally the case, as the sample period of obsersvations may not adequately sample all the physically possible patterns, i.e. fully explore the realm of possibility within physical limits, for example, if it were possible, the Pacific arm stretching to 20S. However, the CBF method still constrains some of the uncertainty stemming from the EOF analysis, making it much easier to compare the two datasets knowing that both spatial patterns have been derived from the same EOF. 

Important to Note: they find that internal variability plays a less important role than that of inter-model variability, as errors between realisations of the same model were notably smaller than that between models. They conclude that faily robust conclusions can be drawn from CMIP comparisons.