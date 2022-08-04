# To Do List

## Things to Do

- Write paper.
    - Create publication-quality figures.
- Write abstract for NZ Met Conference -- deadline: 22nd August. (https://www.hydrometsoc22.co.nz/presenter-guidelines)
- Cannot interpolate HadGEM3 calendar as expected. What effect will this have? It doesn't appear to have any major effect on MCA results, however, there may be some small errors that could lead to unfair model performance analysis.
- Calculate ZW3 index for models.
    - Calculate Magnitude and Phase time series.
- Check spread of indices for models. Do they simulate frequency of extreme values?
    - Violin/box plots for all models adjacent to ERA-5.
    - Map for areas of high standard deviations/variances? -- for all models and ERA-5.
- Are there linear trends in some quantities? Perhaps location of maximum variance, or magnitude.
- Think about how to quantify the bias in annual cycle.
    - James' suggestion:
        - Calculate the mean height & variance of height through time for each grid point during each season.
        - Calculate Root Mean Square (RMS) value over the spatial field, i.e., sum of difference between model mean and ERA-5 mean at each grid point.
        - Add up the RMS values for each season and compare between models. The best should have the smallest RMS.
- Quantify the base state bias.
    - Find the zonally-averaged mean height and plot vs. latitude.
        - Does the peak in mean height gradient occur at the same spot as ERA-5?
    - Repeat the same analysis for the variance field -- where is the meridional gradient peak?
- Look into Taylor Diagrams


## Questions to Answer

- What is the Eliasson-Palm flux and what does it represent? Trenberth 1991 seems to use E-P flux as a proxy for representing eddy fluxes of several characteristics of storms.
- The jet axis tends to be located above a narrow sloping zone of strong potential temperature gradients, called the _polar-frontal zone_, which separates the cold polar air from the warm tropical air. This is a result of the thermal wind balance. Why is this?


## Research Areas

- Rossby Waves
    - Rossby Wave Trains
    - Rossby Wave Breaking
- Atmospheric Dynamics
    - Potential Temperature
    - Potential Vorticity


## Papers to Read

- Fogt and Marshall, 2020
- Fogt, Jones et al. 2012
- Priestley et al. 2020


## Books/Chapters to Read

- Holton & Hakim - Introduction to Dynamic Meteorology


## Misc to Read

- On the Trend, Detrending and variability of nonlinear and nonstationary time series, PNAS online https://www.pnas.org/doi/10.1073/pnas.0701020104
- Old Notes
