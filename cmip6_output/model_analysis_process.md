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

