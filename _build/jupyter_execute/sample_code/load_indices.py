#!/usr/bin/env python
# coding: utf-8

# # Load Indices
# 
# This notebook contains code that opens indices datasets and sorts them into a nested dictionary, a structure that is consistent with how the data is handled by the CorrCovMaps class.

# In[1]:


import xarray as xr
import numpy as np

from pathlib import Path

class Indices():
    def __init__(self, filenames, variable_names, period='seasonal'):
        """
        This function opens the NetCDF files containing indices, reformats the 
        contents into a usable format and stores them in a consistent data structure.

        Parameters
        ----------
        filenames: list
            List of file path locations for all indices to be correlated.
        variable_names: str
            List of names that identify the variable in the index NetCDF file.
        seasonal: boolean
            Indicates whether the input data should be processed seasonally.

        Returns
        -------
        index_dict: dict
            Dictionary used to store indices' time series.
        std_dict: dict
            Dictionary used to store standard deviations of indices' time series.
        """
        
        self._filenames = filenames
        self._variable_names = variable_names
        self._period = period
        
        self._index_dict = {}

        self.load_indices()


    def load_indices(self):
        """
        Returns
        -------
        normalised_index_dict: dict
            Dictionary containing arrays of all normalised indices' time series.
        std_dict: dict
            Dictionary containing standard deviation of all normalised indices' time 
            series.
        """

        for filename in self._filenames:
            raw_index = xr.open_dataset(filename)
            for variable_name in list(raw_index.keys()):
                if variable_name not in self._variable_names:
                    assert variable_name + "not in variable_names, skipping."
                    continue
                if variable_name == 'zw3index_magnitude':
                    self._zw3_lon_filtered_groups = self.get_lon_groups(raw_index)
                    for lon_range, times in self._zw3_lon_filtered_groups.groups.items():
                        raw_index = self._zw3_lon_filtered_groups[lon_range]
                        key_name = "zw3_" + lon_range
                        self.organise_indices_dict(raw_index, variable_name, key_name, times)
                else:
                    self.organise_indices_dict(raw_index, variable_name, variable_name)
            raw_index.close()


    def organise_indices_dict(self, index, variable_name, key_name, lon_times=None):
        """
        Checks whether the data is to be handled seasonally or not, and calls the 
        appropriate method to create the correct data structure.
        """
        
        if self._period == 'seasonal':
            index_groups = self.group_seasonal_data(index[variable_name])
            self.organise_seasonal_dict(index_groups, key_name)
        elif self._period == 'rolling_seasonal':
            index_groups = self.group_rolling_seasonal_data(index[variable_name])
            self.organise_seasonal_dict(index_groups, key_name)
        elif self._period == 'yearly':
            self.organise_yearly_dict(index[variable_name], key_name, lon_times) 
    
    
    def organise_yearly_dict(self, index, key_name, lon_times=None):
        """
        This function creates the necessary dictionary structure when using the full 
        time series i.e. yearly aggregate where seasonal differences are smeared over.
        Ensures self._index_dict and self._std_dict are stored and accessed correctly when
        calculating correlations and writing NetCDF files.

        Parameters
        ----------
        index: xarray.Dataset
            Dataset containing index data with time dimension.
        key_name: str
            Name of key to store data under, in this case usually the index name.
        lon_times: numpy.ndarray
            Array of indices of timestamps that feature for a given ZW3 longitude 
            phase.
        """

        index_time_series = self.format_index(index)
        if len(index_time_series) < 10:
            print(f"{key_name} has fewer than 10 data. "\
                "Sample size too small: it won't be correlated.")
        else:
            if 'zw3' in key_name:
                self._index_dict[key_name] = (index_time_series, lon_times)
            else:
                self._index_dict[key_name] = index_time_series


    def organise_seasonal_dict(self, index_groups, key_name):
        """
        For data to be handled seasonally, this function creates the necessary dictionary
        structure for the self._index_dict and self._std_dict to be stored and accessed 
        correctly when calculating correlations and writing NetCDF files.

        Parameters
        ----------
        index: xarray.Dataset
            Dataset containing index data with time dimension.
        key_name: str
            Name of key to store data under, in this case usually the index name.
        """
        for season, times in index_groups.groups.items():
            index_time_series= self.format_index(index_groups[season])
            if len(index_time_series) < 10:
                print(f"{key_name} in {season} has fewer than 10 data. "\
                    "Sample size too small: it won't be correlated.")
                continue
            else:
            # if self._period == 'rolling_seasonal':
            #     season_names = [
            #         'NDJ', 'DJF', 'JFM', 'FMA', 'MAM', 'AMJ', 
            #         'MJJ', 'JJA', 'JAS', 'ASO', 'SON', 'OND',   
            #     ]
            #     season = season_names[season - 1]
                if season not in self._index_dict:
                    self._index_dict[season] = {}
                self._index_dict[season][key_name] = (index_time_series, times)


    def format_index(self, index):
        """
        Reformats given index into a flattened numpy.ndarray and normalises that array.
        Returns the normalised index and its standard deviation for use in covariance
        calculation.

        Parameters
        ----------
        index: xarray.DataArray
            DataArray containing index data with time dimension.
        
        Returns
        -------
        normalised_index: numpy.ndarray
            Normalised index with no NaNs.
        """
        index_array = np.array(index).flatten()
        # Drop nans
        index_array = index_array[~np.isnan(index_array)]

        return index_array
        
    
    @staticmethod
    def group_seasonal_data(ds):
        return ds.groupby('time.season')


    @staticmethod
    def group_rolling_seasonal_data(ds):
        rolling_season_average = ds.rolling(time=3, min_periods=3).mean().dropna('time')
        return rolling_season_average.groupby('time.month')


    @staticmethod
    def get_lon_groups(zw3):
        """
        Groups Goyal's ZW3 index into longitude bins.

        Parameters
        ----------
        zw3: xarray.Dataset
            Dataset containing a time series for Goyal's ZW3 index, must contain both 
            magnitude and phase.
        
        Returns
        -------
        groups_zw3: xarray.Dataset.groupby
            Dataset grouped by longitude bins.
        """

        bins = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
        labels = ['-180_-150', '-150_-120', '-120_-90', '-90_-60', '-60_-30', '-30_0', '0_30', '30_60', '60_90', '90_120', '120_150', '150_180']

        groups_zw3 = zw3.groupby_bins(group=zw3.zw3index_phase, bins=bins, labels=labels, right=False, include_lowest=True)

        return groups_zw3

