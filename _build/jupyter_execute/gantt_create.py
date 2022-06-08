#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.figure_factory as ff


# In[2]:


task1 = "Finish ERA5 Analysis."
task2 = "Write paper on ERA5 Analysis."
task3 = "Model Analysis."
task4 = "Model Projections."
task5 = "Write paper on Model Analysis."
task6 = "Thesis write-up."

df = [dict(Task=task1, Start='2022-05-26', Finish='2022-06-18'),
      dict(Task=task2, Start='2022-06-14', Finish='2022-07-08'),
      dict(Task=task3, Start='2022-06-21', Finish='2022-09-30'),
      dict(Task=task4, Start='2022-09-26', Finish='2022-10-21'),
      dict(Task=task5, Start='2022-10-07', Finish='2022-12-02'),
      dict(Task=task6, Start='2022-11-28', Finish='2023-02-28')]

fig = ff.create_gantt(df,)
fig.show()


# | Task | Details | Period |
# | --: | :-- | :-- |
# | Finish ERA5 Analysis. | Finish MCA analysis, seasonally and yearly, with lagged data and rotated EOFs, and calculate correlations between variance and height PCs. | 30th May - 11th June |
# |  | Change presentation of corr/cov maps and MCA EOFs figures. | 6 - 11th June |
# |  | FDR Significance testing | 6 - 17th June |
# | Write paper on ERA5 Analysis. | Describe figures & results. | 13 - 17th June |
# |  | Discussion of seasonal variability and influence of phenomena. | 20th June - 1st July |
# |  | Introduction, Conclusion & Abstract | 27th June - 8th July |
# |  | Literature Review & Back-up/Compare Results with References | 13th June - 8th July |
# | Model Analysis | Gather set of 20 models and research model background. | 11 - 29th July |
# |  | Write procedure that can be executed in Raapoi & run procedure. | 25th July - 5th August |
# |  | Analyse results & Diagnose Biases | 8th August - 30th Sept |
# | Model Projections | Develop analysis procedure to identify whether any consensus holds. | 26th Sept - 7th Oct |
# |  | Apply procedures & analyse results. | 10 - 21st Oct |
# | Write paper on Model Analysis | Describe figures & results. | 10 - 28th Oct |
# |  | Discussion of comparisons with ERA5 and biases. | 24th Oct - 18th Nov |
# |  | Introduction, Conclusion & Abstract | 14th Nov - 2nd Dec |
# |  | Literature Review & Back-up/Compare Results with References | 10th Oct - 2nd Dec |
