#!/usr/bin/env python
# coding: utf-8

# # Correlation Spatial Patterns
# 
# This notebook calculates the correlation between indices time series and anomaly time series, variance and mean height, at each longitude/latitude grid point. Methods used are both Pearson and Spearman rank correlations.

# In[1]:


import xarray as xr
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

import glob

import pytest


# In[2]:


def get_coords(variance_anoms):
    # Creates 2D array of coordinate pairs
    lon_min = np.int32(np.array(variance_anoms.lon)[0])
    lon_max = np.int32(np.array(variance_anoms.lon)[-1])
    lat_min = np.int32(np.array(variance_anoms.lat)[0])
    lat_max = np.int32(np.array(variance_anoms.lat)[-1])

    lon = [*range(lon_min, lon_max+1)]
    lat = [*range(lat_min, lat_max-1, -1)]

    coords_array = np.array(np.meshgrid(lon, lat)).T.reshape(-1,2)

    return coords_array


# In[3]:


def create_correlation_dict(variance_anoms, index_dict):   
    correlation_arrays = {}
    
    shape = (variance_anoms.lon.size, variance_anoms.lat.size)
    corr_array = np.zeros(shape)

    for key in index_dict.keys():
        correlation_arrays[key] = np.copy(corr_array)

    return correlation_arrays


# In[4]:


def normalise_sample(arr):
    if np.round(np.mean(arr),6) != pytest.approx(0.0):
        arr_anoms = arr - np.mean(arr)
    else:
        arr_anoms = arr
    if np.std(arr_anoms) != pytest.approx(1.0):
        arr_norm = np.divide(arr_anoms, np.std(arr_anoms))
    else:
        arr_norm = arr_anoms
    
    return arr_norm


# In[5]:


def correlation_two_normalised_time_series(arr1, arr2):
    return np.sum(np.multiply(arr1, arr2)) / (arr1.size - 1)


# In[6]:


def reformat_time_series(variance_anoms, coords):
    variance_anoms_dbl_array = np.array(variance_anoms.sel(lon=coords[0], lat=coords[1]).to_array()[1])
    variance_anoms_array = np.hsplit(variance_anoms_dbl_array, 2)[0]
    variance_time_series = variance_anoms_array.flatten()

    return variance_time_series


# In[7]:


def load_indices(filenames, variable_names):
    index_dict = {}
    for filename in filenames:
        raw_index = xr.open_dataset(filename)
        for variable_name in list(raw_index.keys()):
            if variable_name in variable_names:
                index_dict[variable_name] = np.array(raw_index[variable_name]).flatten()
                # Drop nans
                index_dict[variable_name] = index_dict[variable_name][~np.isnan(index_dict[variable_name])]
                index_dict[variable_name] = normalise_sample(index_dict[variable_name])

    return index_dict


# In[8]:


def calculate_correlation_matrices(anoms, index_dict, coords_array, correlation_arrays, method='pearson'):
    for i,coord in enumerate(coords_array):
        time_series = reformat_time_series(anoms, coords=coord)
        time_series_normalised = normalise_sample(time_series)
        for key,index in index_dict.items():
            resized_time_series_normalised = time_series_normalised[:index.size]
            if method == 'pearson':
                correlation = correlation_two_normalised_time_series(index, resized_time_series_normalised)
            elif method == 'rank':
                correlation, pval = spearmanr(resized_time_series_normalised, index)
            coord = np.unravel_index(i,correlation_arrays[key].shape)
            correlation_arrays[key][coord] = correlation

    return correlation_arrays


# In[9]:


def write_correlations_netcdf(correlation_arrays, anoms, var='variance', method='pearson'):
    corr_path = path + "correlations//"
    for key in correlation_arrays.keys():
        correlations_ds = xr.Dataset(
            data_vars={key:(('lat', 'lon'), correlation_arrays[key])},
            coords={'lat':anoms.lat, 'lon':anoms.lon}
        )
        filename = var + '_' + key + '_' + method + '_correlations.nc'
        correlations_ds.to_netcdf(corr_path + filename)


# In[10]:


path = "G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\"
var_file = "era5_h500_daily_1979_2021_1deg_20S_deseasonalised_bandpass_mon_var_anoms.nc"
mean_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass_20S_mon_anoms.nc"

index_path = "G:\\Isaac\\Documents\\msc-research\\data\\indices\\"
index_files = glob.glob(index_path + "*.nc")


# In[11]:


variance_anoms = xr.open_dataset(path + var_file)
mean_anoms = xr.open_dataset(path + mean_file)


# In[12]:


variable_names = ['z', 'DMI', 'SOI']
index_dict = load_indices(index_files, variable_names)


# In[13]:


coords_array = get_coords(variance_anoms)
correlation_arrays = create_correlation_dict(variance_anoms, index_dict)


# In[14]:


variance_pearson_correlation_arrays = calculate_correlation_matrices(variance_anoms, index_dict, coords_array, correlation_arrays, 'pearson')
variance_rank_correlation_arrays = calculate_correlation_matrices(variance_anoms, index_dict, coords_array, correlation_arrays, 'rank')


# In[19]:


mean_pearson_correlation_arrays = calculate_correlation_matrices(mean_anoms, index_dict, coords_array, correlation_arrays, 'pearson')
mean_rank_correlation_arrays = calculate_correlation_matrices(mean_anoms, index_dict, coords_array, correlation_arrays, 'rank')


# In[ ]:


write_correlations_netcdf(variance_pearson_correlation_arrays, mean_anoms, 'variance', method='pearson')
write_correlations_netcdf(variance_rank_correlation_arrays, mean_anoms, 'variance', method='rank')


# In[39]:


write_correlations_netcdf(mean_pearson_correlation_arrays, mean_anoms, 'mean', method='pearson')
write_correlations_netcdf(mean_rank_correlation_arrays, mean_anoms, 'mean', method='rank')

