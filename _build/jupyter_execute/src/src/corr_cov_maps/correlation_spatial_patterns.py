#!/usr/bin/env python
# coding: utf-8

# # Correlation Spatial Patterns
# 
# This notebook calculates the correlation between indices time series and anomaly time series, variance and mean height, at each longitude/latitude grid point. Methods used are both Pearson and Spearman rank correlations.

# In[1]:


import xarray as xr
import numpy as np

from pathlib import Path

from load_indices import Indices


# In[2]:


class CorrCovMaps():
    def __init__(self, anoms, indices, stat, method, period, path=Path(".")):
        """ 
        Attributes
        ----------
        self._anoms: xarray.Dataset
            Dataset containing time series for all lat/lon grid points.
        self._index_dict: dict
            Dictionary containing arrays of all normalised indices' time series.
        self._coords_array: numpy.ndarray
            2D array containing all lat/lon coordinate pairs.
        self._correlation_arrays: numpy.ndarray
            Array to store correlation values between all indices and all lat/lon 
            grid points.
        self._covariance_arrays: numpy.ndarray
            Array to store covariance values between all indices and all lat/lon 
            grid points.   
        self._stat: str
            Specifies whether the anomalies are either mean height or bandpassed
            variance.
        self._method: str
            Specifies whether to use Pearson product-moment correlation or
            Spearman rank correlation.
        self._period: boolean
            Indicates whether the input data should be processed seasonally, 
            rolling three month seasons or yearly.
        """
        
        self._path = path
        self._anoms = anoms
        self._index_dict = indices._index_dict
        self._stat = stat
        self._method = method
        self._period = period

        self._correlation_arrays = self.create_corr_cov_dict()
        self._covariance_arrays = self.create_corr_cov_dict()

        self.populate_corr_cov_matrices()
      

    def populate_corr_cov_matrices(self):
        """
        This function calls the correct function to calculate correlation/covariance
        depending on whether seasonal data is being used. 
        """

        if self._period == 'seasonal' or self._period == 'rolling_seasonal':
            for season,variables in self._index_dict.items():
                for variable_name,variable_values in variables.items():
                    # Separate tuple of index values and time indices.
                    times = variable_values[1]
                    index_values = variable_values[0]
                    # Remove values for incomplete seasons, i.e. first month of first 
                    # summer and first two months of final summer in anomalies dataset.
                    if season == 'DJF' and self._period == 'seasonal':
                        times = times[2:-1]
                        index_values = index_values[2:-1]
                    anoms_filtered = self._anoms.isel(time=times)
                    index_ds = self.create_indices_dataset(
                        anoms_filtered,
                        index_values, 
                        variable_name
                    )
                    correlation_array, covariance_array = self.calculate_corr_cov_matrices(
                        anoms_filtered, index_ds, variable_name
                    )
                    self._correlation_arrays[season][variable_name] = correlation_array
                    self._covariance_arrays[season][variable_name] = covariance_array
        else:
            for variable_name, variable_values in self._index_dict.items():
                if "zw3" in variable_name:
                    times = variable_values[1]
                    index_values = variable_values[0]
                    anoms_filtered = self._anoms.isel(time=times)
                else:
                    index_values = variable_values
                    anoms_filtered = self._anoms
                index_ds = self.create_indices_dataset(
                        anoms_filtered,
                        index_values, 
                        variable_name
                    )
                corr_arr, cov_arr = self.calculate_corr_cov_matrices(
                    anoms_filtered, index_ds, variable_name
                )
                self._correlation_arrays[variable_name] = corr_arr
                self._covariance_arrays[variable_name] = cov_arr

        self._anoms.close()
        if self._path != None:
            self.write_to_netcdf(self._correlation_arrays, 'corr')
            self.write_to_netcdf(self._covariance_arrays, 'cov')

    
    def create_corr_cov_dict(self):
        """
        Creates a dictionary of zero arrays with keys corresponding to index name and, 
        if seasonal is True, seasons. The dictionary will have the same structure as 
        index_dict. correlation_arrays will be used to store data for correlation
        values at each lon/lat point.
        
        Returns
        -------
        arrays: dict
            Dictionary with the same structure as index_dict. Each key has a 
            numpy.ndarray of zeroes with identical longitude/latitude dimensions
            to the input file grid.
        """

        arrays = {}

        for key in self._index_dict.keys():
            if self._period == 'seasonal' or self._period == 'rolling_seasonal':
                for subkey in self._index_dict[key].keys():
                    if key not in arrays:
                        arrays[key] = {}
                    arrays[key][subkey] = None
            else:
                arrays[key] = None

        return arrays

    
    def create_indices_dataset(self, anoms, index, variable_name):
        lon = anoms.lon
        lat = anoms.lat
        time = len(index)
        n = lon.size * lat.size

        index_flattened = np.repeat(index[None, :], n, axis=0)
        index_data = index_flattened.reshape((lon.size, lat.size, time))

        ds = xr.Dataset(
                data_vars={
                    variable_name:(('lon', 'lat', 'time'), index_data)
                    },
                coords={
                    'lat':lat, 
                    'lon':lon,
                    'time':anoms.time[:time]
                }
            )
        return ds

    
    def calculate_corr_cov_matrices(self, anoms, index_ds, variable_name):
        anoms_arr = anoms.z
        index_arr = index_ds[variable_name]
        anoms_arr, index_arr = xr.align(anoms_arr, index_arr)

        if self._method == 'pearson':
            corr_matrix = xr.corr(anoms_arr, index_arr, dim='time')
        elif self._method == 'rank':
            ranked_anoms = anoms_arr.rank(dim='time')
            ranked_index = index_arr.rank(dim='time')
            corr_matrix = xr.corr(ranked_anoms, ranked_index, dim='time')
        
        cov_matrix = xr.cov(anoms_arr, index_arr, dim='time')
        
        return corr_matrix, cov_matrix


    def write_to_netcdf(self, arrays: dict, var='corr'):
        """
        Writes NetCDF file with dimensions at specified path location, creates parent 
        directories if required. 
        """
        corr_path = self._path / var / self._period
        corr_path.mkdir(parents=True, exist_ok=True)
        
        # Handle seasonal data.
        if self._period == 'seasonal' or self._period == 'rolling_seasonal':
            for season_name,variables_dict in arrays.items():
                for variable_name,variable_values in variables_dict.items():
                    ds = variable_values.to_dataset(name=var)
                    filename = season_name + '_' + self._stat + '_' \
                        + variable_name + '_' + self._method + '_' \
                        + var +  '.nc'
                    ds.to_netcdf(corr_path / filename)
                    ds.close()
        else:
            for variable_name,variable_values in arrays.items():
                ds = variable_values.to_dataset(name=var)
                filename = season_name + '_' + self._stat + '_' \
                    + variable_name + '_' + self._method + '_' \
                    + var +  '.nc'
                ds.to_netcdf(corr_path / filename)
                ds.close()


# In[3]:


path = Path("G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\")
index_path = Path("G:\\Isaac\\Documents\\msc-research\\data\\indices\\")

var_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass_20S_mon_var_anoms.nc"
mean_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_20S_mon_anoms.nc"
index_files = list(index_path.glob("*.nc"))


# In[4]:


period = 'seasonal'

variance_anoms = xr.open_dataset(path / var_file)
mean_anoms = xr.open_dataset(path / mean_file)

variable_names = ['sam', 'DMI', 'SOI', 'zw3index_magnitude']
indices = Indices(index_files, variable_names, period)


# In[5]:


anoms = [(variance_anoms, 'variance'), (mean_anoms, 'mean')]
methods = ['pearson', 'rank']


# In[6]:


for anom in anoms:
    for method in methods:
        CorrCovMaps(
            anom[0], indices, stat=anom[1],
            method=method, period=period,
            path=path
            )

