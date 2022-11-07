# Methodology

## Field Projections

Do I remove the bias of each model for each set of projections?

For both the mean height field and its associated HF variance field, perform Welch's t-test (https://www.geeksforgeeks.org/welchs-t-test-in-python/, two independent samples of unequal size and variance) on each gridpoint to determine whether a statistically significant change has occured. Then apply the method of Knutti & Sedlácek (2013) -- _ask James if he knows how to do this_.


## Covariance Maps

Ideas:

- Repeat a similar procedure but for Covariance maps, using covariance as the means and variance as the ??
- Use the projections of the two fields and covariance maps as normal to compare, and interpret changes to SAM, ENSO and ZW3 without statistical certainty.