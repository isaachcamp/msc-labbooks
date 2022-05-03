#!/usr/bin/env python
# coding: utf-8

# # ZW3 Correlations
# 
# Initially correlations were done between variance anomalies and both ZW3 magnitude and phase, however this was deemed insufficient since ZW3 is quite mobile. This means that ZW3 events with high magnitudes could occur and affect the storm track strongly locally, but not on the other side of the globe. Therefore, due to the inconsistency of event locations, correlations would be weaker and local influences could go undetected. For this reason, ZW3 events of sufficient magnitude were separated into longitude bins and correlated those ZW3 magnitude time series with variance anomalies found in corresponding longitude bins.

# In[1]:


import xarray as xr
import pandas as pd
import numpy as np

import correlation_spatial_patterns as csp


# In[2]:


from scipy.stats import spearmanr


# In[3]:


path_zw3 = "G:\\Isaac\\Documents\\msc-research\\data\\indices\\"
filename_zw3 = "zw3index_Goyaletal2022.nc"
zw3 = xr.open_dataset(path_zw3 + filename_zw3)

path_anoms = "G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\"
filename_mean_anoms = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass_20S_mon_anoms.nc"
filename_var_anoms = "era5_h500_daily_1979_2021_1deg_20S_deseasonalised_bandpass_mon_var_anoms.nc"
mean_anoms = xr.open_dataset(path_anoms + filename_mean_anoms)
var_anoms = xr.open_dataset(path_anoms + filename_var_anoms)


# In[4]:


bins = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
labels = ['-180:-150', '-150:-120', '-120:-90', '-90:-60', '-60:-30', '-30:0', '0:30', '30:60', '60:90', '90:120', '120:150', '150:180']


# In[5]:


zw3_upper_half = zw3.where(zw3.zw3index_magnitude > zw3.zw3index_magnitude.median(), drop=True)
groups_zw3 = zw3_upper_half.groupby_bins(group=zw3_upper_half.zw3index_phase, bins=bins, labels=labels, right=False, include_lowest=True)


# In[6]:


groups_anoms = mean_anoms.groupby_bins(group=var_anoms.lon, bins=bins, labels=labels, right=False, include_lowest=True)
present_times = {}


# In[7]:


for lon_group in groups_zw3.groups.keys():
    time_list = groups_anoms[lon_group].indexes['time'].strftime("%Y-%m")
    present_times[lon_group] = []
    for i, time in enumerate(time_list):
        if time in groups_zw3[lon_group].indexes['time']:
            present_times[lon_group].append(i)


# In[8]:


shape = (var_anoms.lat.size, var_anoms.lon.size)
correlations_array = {"zw3": np.zeros(shape)}

errors = 0

for lon_group in groups_zw3.groups.keys():
    zw3_time_series_lon_filtered = zw3['zw3index_magnitude'].isel(time=present_times[lon_group])
    zw3_time_series_lon_filtered = np.array(zw3_time_series_lon_filtered)
    zw3_time_series_lon_filtered_normalised = csp.normalise_sample(zw3_time_series_lon_filtered)

    anoms_lon_filtered = groups_anoms[lon_group].isel(time=present_times[lon_group])
    coords_array = csp.get_coord_pairs(anoms_lon_filtered)

    for coord in coords_array:
        anoms_time_series_lon_filtered = np.array(anoms_lon_filtered.sel(lon=coord[0], lat=coord[1])['z'])
        anoms_time_series_lon_filtered_normalised = csp.normalise_sample(anoms_time_series_lon_filtered)

        #correlation = csp.correlation_two_normalised_samples(
        #    zw3_time_series_lon_filtered_normalised,
        #    anoms_time_series_lon_filtered_normalised
        #    )
        
        correlation, pval = spearmanr(
            zw3_time_series_lon_filtered_normalised,
            anoms_time_series_lon_filtered_normalised
        )
        
        i = (np.abs(coord[1]) - 20) * var_anoms.lon.size + (coord[0] + 180)
        coord = np.unravel_index(i, correlations_array["zw3"].shape)
        if correlations_array["zw3"][coord] == 0:
            correlations_array["zw3"][coord] = correlation
        else:
            errors += 1


# In[111]:


errors


# In[112]:


csp.write_correlations_netcdf(correlations_array, var_anoms, path_anoms)

