#!/usr/bin/env python
# coding: utf-8

# # Sample Calculations
# 
# Five random points at two different pre-selected timestamps are used to test whether the CDO software accurately calculated pre-processing steps as well as anomalies, means and variances.
# 
# The bandpass calculation was not recreated as the process is computationally expensive -- CDO took over two days of CPU time, even with various optimisation procedures.
# 
# Deseasonlisation and long-term averages show no discrepancies between the sample calculations and CDO. Neither do the variance and mean height anomalies -- use of CDO module is considered valid.

# In[1]:


import xarray as xr
import pandas as pd
import numpy as np

import datetime

import pytest


# In[2]:


def choose_random_data(ds):
    arr_size = ds.lat.size * ds.lon.size

    rng = np.random.default_rng()
    points = rng.choice(arr_size, 5)

    points_indices = np.array(np.unravel_index(points, (ds.lon.size, ds.lat.size))).transpose()
    points_coords = points_indices - np.array([180, 90])

    # Ensure all surrounding points exist for smoothing operation.
    for coords in points_coords:
        if coords[0] == 180:
            coords[0] -= 1
        elif coords[0] == -180:
            coords[0] += 1
        if coords[1] == 90:
            coords[1] -= 1
        elif coords[1] == -90:
            coords[1] += 1

    return points_coords


# In[3]:


def long_term_average(ds, resample="D", group_by_time_format='%m-%d'):
    resampled_ds = ds.resample(time=resample).mean()
    index_array = xr.DataArray(resampled_ds.indexes['time'].strftime(group_by_time_format), coords=resampled_ds.coords, name='time')
    long_term_ave = resampled_ds.groupby(index_array).mean()
    
    return long_term_ave


# In[4]:


def long_term_variance(ds, group_by_time_format='%m'):
    index_array = xr.DataArray(ds.indexes['time'].strftime(group_by_time_format), coords=ds.coords, name='time')
    long_term_var = ds.groupby(index_array).var()
    
    return long_term_var


# In[5]:


def calculate_variance_anomalies(time_series, resample='M', group_by_time_format='%m'):
    period_variance = time_series.resample(time=resample).var()
    long_term_var = long_term_variance(time_series, group_by_time_format=group_by_time_format)
    index_array = xr.DataArray(period_variance.indexes['time'].strftime(group_by_time_format), coords=period_variance.coords, name='time')
    var_anoms = period_variance.groupby(index_array) - long_term_var

    return var_anoms


# In[6]:


def smooth9(datum, ds, grid_res=1.0, timestamp='1979-01-01-00', resample="D", group_by_time_format='%m-%d'):
    # Get correct format for selecting by time index for long-term average dataset.
    groupby_time = datetime.datetime.strptime(timestamp,"%Y-%m-%d-%H").strftime(group_by_time_format)

    # Create variables for data and surrounding points using longitude and latitude.
    lon = np.float64(datum[0])
    lat = np.float64(datum[1])
    lons = [lon - grid_res, lon, lon + grid_res]
    lats = [lat - grid_res, lat, lat + grid_res]
    
    surrounding_points = np.array(np.meshgrid(lons, lats)).T.reshape(-1, 2)
    surrounding_values = np.zeros((3,3))
    weights = np.array([
        [0.3, 0.5, 0.3],
        [0.5, 1.0, 0.5],
        [0.3, 0.5, 0.3]
    ])
    
    # Get long-term average values for all points.
    for i in range(len(surrounding_points)):
        time_series = ds.sel(lon=surrounding_points[i][0], lat=surrounding_points[i][1])
        long_term_ave = long_term_average(time_series, resample, group_by_time_format)
        index = np.unravel_index(i, (3,3))
        surrounding_values[index] = np.float64(long_term_ave.sel(time=groupby_time).to_array())
    
    # Calculate the smoothed value, sum of all weighted values divided by total weight.
    weighted_values = np.multiply(surrounding_values, weights)
    smoothed_value = np.sum(weighted_values)/np.sum(weights)
    
    return smoothed_value


# In[7]:


def deseasonalise(datum, ds, timestamp='1979-01-01-00', grid_res=1.0, resample="D", group_by_time_format='%m-%d'):
    smoothed_long_term_ave = smooth9(datum, ds, grid_res, timestamp=timestamp, resample=resample, group_by_time_format=group_by_time_format)
    datum_val = ds.sel(lon=datum[0], lat=datum[1], time=timestamp).to_array()
    deseasonalised = np.float64(datum_val) - smoothed_long_term_ave
    
    return deseasonalised


# In[8]:


def compare_vals(cdo_ds, calc_vals):
    errors = 0
    for key,calc_val in calc_vals.items():
        print(key)
        cdo_val = cdo_ds.sel(time=key[1], lon=key[0][0], lat=key[0][1])['z']
        cdo_val = np.float64(cdo_val)
        cdo_val_approx = np.round(cdo_val, 2)
        calc_val_approx = np.round(calc_val, 2)
        if pytest.approx(cdo_val_approx) != pytest.approx(calc_val_approx):
            print('Difference between CDO and calculated values for: ' + str(key) + 
                  '\n the two values are ' + str(cdo_val) + ' and ' + str(calc_val))
            errors += 1
    if errors == 0:
        print('No discrepancies found.')


# In[9]:


# Check pre-processing steps, up to deseasonalisation, but excluding bandpass filter.

path = "G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\"
raw_file = "era5_h500_daily_1979_2021_1deg.nc"
cdo_file = "era5_h500_daily_1979_2021_1deg_deseasonalised.nc"

ds = xr.open_dataset(path + raw_file)
cdo_ds = xr.open_dataset(path + cdo_file)

points_coords = choose_random_data(ds)
print(points_coords)

deseasonalised_data = {}
timestamps = ['1979-01-01-00', '2000-06-06-12']

for timestamp in timestamps:
    for i,datum in enumerate(points_coords):
        deseasonalised_datum = deseasonalise(datum, ds, timestamp=timestamp, grid_res=1.0)
        deseasonalised_data[tuple(datum), timestamp] = deseasonalised_datum
        print(str(i) + ': Done')

errors = compare_vals(cdo_ds, deseasonalised_data)


# In[9]:


# Check calculations of monthly variance anomalies.

path = "G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\"
raw_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass.nc"
cdo_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass_mon_var_anoms.nc"

ds = xr.open_dataset(path + raw_file)
cdo_ds = xr.open_dataset(path + cdo_file)

points_coords = choose_random_data(ds)
print(points_coords)

monthly_variance_anomalies = {}
timestamps = ['1979-01-31', '2000-06-30']

for timestamp in timestamps:
    for i,datum in enumerate(points_coords):
        time_series = ds.isel(lon=datum[0], lat=datum[1])
        var_anoms = calculate_variance_anomalies(time_series)
        var_anom = var_anoms.sel(time=timestamp).to_array()
        print(tuple(datum), timestamp)
        monthly_variance_anomalies[tuple(datum), timestamp] = np.float64(var_anom)

errors = compare_vals(cdo_ds, monthly_variance_anomalies)

