#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from pathlib import Path


# In[2]:


path = Path("G://Isaac//Documents//msc-research//data//ERA5//daily_data//maxcov_analysis")
fname = "pcs_soi_correlations.csv"


# In[3]:


df = pd.read_csv(path / fname, index_col='filename')


# In[4]:


df.loc[(df.data=='daily') * (df.window_length==15) * (df.field=='mean height')]
#(df.data=='daily') * (df.time_series_type=='seasonal') * (df.window_length==15)


# In[ ]:




