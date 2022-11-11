# To Do List

- Introductory Motivation section:
    - James -- "An introductory/motivational chapter could be useful before you get into the guts of the work. Why do we care about storm tracks etc? Perhaps just an expanded version of your section 1.1."

- Abstract
    - Remove some of the detail.
    - James -- "This is nice, but quite long. You could start with an opening sentence along the lines of "We have studied SH storms tracks and their interactions with the background circulation both in reanalyses and in CMIP6 models."

- Chapter 1
    - Redo figures:
        - Use shared cmap.
        - Mask low variance and remove colour scales.
        - Redo ZW3 annual composite without lower composites.
        - Add phase bins to ZW3 annual covariance and composite figure.
        - Add season labels and remove autolabel feature from pygmt generated figures.
        - Get intervals and masking limits for all ERA-5 figures.
    - Make corrections.
        - Redo composites with seasonal sample size of 10.
    - Read up on MCA method again, make sure you understand the implications of it.

- Chapter 2
    - Back-up/Compare Results with References e.g. Bracegirdle et al. 2020.
    - Base State
        - Add figure with all meridional profiles.
        - Add symbols to legend of Taylor diagram.
        - Redo spatial biases figure with mask.
    - Composites
        - Redo figures with shared cmap.
    - CBF analysis 
        - Add in reference to seasonal performance.
        - Effect of difference in methodology from Lee et al.?
     
- Chapter 3
    - Introduction
        - Finish intro write-up.
        - Include outline of methods in the summary part.
    - Methods
        - Identify statistically significant changes to the mean field.
            - Apply either Tebaldi et al. 2011 or Knutti & Sedlacek 2013 method for robustness.
        - Calculate change in meridional peak position.
        - Covariance maps
            - SAM annual & seasonal
            - SOI annual & seasonal
            - ZW3 annual only
            - Take the difference between historical and scenario experiments.
        - CBF analysis, as above.
    - Analysis
        - Mean field projections.
            - Calculate statistical significance at each grid point using Welch's t-test and FDR method.
            - Calculate MME mean.
            - Identify model consensus/robustness of projections for MME mean plotting.
        - Meridional peaks and spatial biases.
        - Pearson covariance and correlations, seasonal and annual, and take the difference.
            - Create summary plots and calculate MME mean annually & seasonally.
        - CBF analysis.
    - Results 
        - Analyse results.
        - Write-up.

- Bibliography
    - Clean up references.
