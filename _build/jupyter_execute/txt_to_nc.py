#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import xarray as xr


# In[2]:


path = 'G:\\Isaac\\Documents\\msc-research\\data\\indices\\raw_data\\'
filename = 'soi_noaa.txt'


# In[3]:


with open(path + filename, 'r') as f:
    lines = f.readlines()

time_series_list = []

for line in lines:
    line = line.strip(' \n').split(' ')[1:]
    data_line = [x for x in line if x != '']
    time_series_list.append(data_line)


# In[4]:


data_series = np.array(time_series_list)
data_series = np.reshape(data_series, (np.size(data_series),1))
data_series = data_series.astype(float)

idx = pd.date_range('1979-01-31', periods=np.size(data_series), freq='M')
time_series = pd.DataFrame(data_series, index=idx)
time_series.rename(columns={0:'SOI'}, inplace=True) 
time_series.index.rename('time', inplace=True)

ts = time_series.to_xarray()


# In[5]:


ts.attrs = {'frequency':'monthly', 
            'source':'https://www.cpc.ncep.noaa.gov/data/indices/soi', 
            'history':'created using "read_txt_datafile.py"',
            'data range':'Jan 1979 - Dec 2021'
            }

ts.SOI.attrs = {
    'standard_name':'SOI', 
    'long_name':'Southern Oscillation Index', 
    'units':'dimensionless',
    '_FillValue':-9999.00
    }


# In[6]:


print(ts.var)


# In[7]:


ts.to_netcdf("soi_noaa.nc")

