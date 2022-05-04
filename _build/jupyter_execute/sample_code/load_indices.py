#!/usr/bin/env python
# coding: utf-8

# # Load Indices
# 
# Creates nested dictionary containing time series of each index passed to it.
# 
# See docstrings below for more details.

# In[1]:


import xarray as xr
import numpy as np


class Indices():
    """
    Creates dictionary containing time series of each index passed to it.

    Loads index NetCDF files contained within filenames list. Reads the data as
    xarray.Datasets before reformatting them into numpy.ndarrays. 
    Creates a data structure, a nested dictionary, that is consistent for easy 
    access to indices time series. This dictionary is assigned as an attribute 
    under self._index_dict.

    If period is "seasonal", the data is grouped according to season. Also, if
    the index for ZW3 is passed, the tindex is grouped according to phase bins,
    controlled by the argument "zw3_bins". This grouping effeectively reduces the
    length of the time series, and the exact times under each group must be paired
    with the same timestamps in the anomalies Dataset when calculating correlation
    and covariance matrices (see corr_cov_maps.py). To this end, the index of each 
    time contained within the grouped data is returned in a tuple with the index 
    value at this timestamp.

    Attributes
    ----------
    self._index_dict: dict
        Nested dictionary containing time series for each grouped index. If period
        is "seasonal", the data structure will be the following:
            self._index_dict = {
                season:{
                    index_name: (index_values, timestamp_indices)
                }
            }
        Otherwise, the structure will be:
            self._index_dict = {
                index_name:(index_values, timestamp_indices)
            }
        If the whole time series is to be used, {timestamp_indices} is assigned
        None.
    """
    
    def __init__(self, filenames, index_names, period='seasonal', zw3_bins='30_deg'):
        """
        Creates and organises index dictionary attribute.

        This function opens the NetCDF files containing indices, reformats the 
        contents into a usable format and stores them in a consistent data structure.

        Arguments
        ---------
        filenames: list
            List of file path locations for all indices to be correlated.
        index_names: list
            List of names that identify the variable in the index NetCDF file.
        period: str
            Indicates whether the input data should be processed seasonally or
            yearly.
        zw3_bins: str
            Indicates whether 30 degree or 60 degree longitude bins should be used.
        """
        
        self._filenames = filenames
        self._index_names = index_names
        self._period = period
        self._zw3_bins = zw3_bins
        
        self._index_dict = {}

        self.load_indices()


    def load_indices(self):
        """
        Loads index files and calls method depending on "period" value.

        Loops through each file and opens that file. Ensures that the
        index within that file is required, i.e. is contained within the
        self._index_names list. Handles ZW3 index different as it first
        groups the data according to phase bins/longitude groups. The
        bounds of the phase bins are used to name the dictionary key.
        """

        for filename in self._filenames:
            raw_index = xr.open_dataset(filename)
            for index_name in list(raw_index.keys()):
                if index_name not in self._index_names:
                    assert index_name + "not in variable_names, skipping."
                    continue
                if index_name == 'zw3index_magnitude':
                    self._zw3_lon_filtered_groups = self.get_lon_groups(raw_index)
                    for lon_range, times in self._zw3_lon_filtered_groups.groups.items():
                        raw_index = self._zw3_lon_filtered_groups[lon_range]
                        key_name = "zw3_" + lon_range
                        self.organise_indices_dict(raw_index, index_name, key_name, times)
                else:
                    self.organise_indices_dict(raw_index, index_name, index_name)
            raw_index.close()


    def organise_indices_dict(self, index, index_name, key_name, lon_times=None):
        """
        Calls appropriate method for handling seasonally grouped data.

        Checks whether the data is to be handled seasonally or not. If so,
        that data is grouped and a call is made to the appropriate method 
        to create the correct data structure.
        """
        
        if self._period == 'seasonal':
            index_groups = self.group_seasonal_data(index[index_name])
            self.organise_seasonal_dict(index_groups, key_name)
        elif self._period == 'yearly':
            self.organise_yearly_dict(index[index_name], key_name, lon_times) 
    
    
    def organise_yearly_dict(self, index, key_name, lon_times=None):
        """
        Creates dictionary for indices full time series.

        This function creates the necessary dictionary structure when using the
        full time series i.e. yearly aggregate where seasonal differences are 
        smeared over. Ensures self._index_dict is stored and accessed correctly 
        when calculating correlations and writing NetCDF files.

        Arguments
        ---------
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
                self._index_dict[key_name] = (index_time_series, None)


    def organise_seasonal_dict(self, index_groups, key_name):
        """
        Creates dictionary for indices to be analysed according to season.

        For data to be handled seasonally, this function creates the necessary 
        dictionary structure for the self._index_dict to be stored and accessed 
        correctly when calculating correlations and writing NetCDF files.

        Arguments
        ---------
        index: xarray.Dataset
            Dataset containing index data with time dimension.
        key_name: str
            Name of key to store data under, usually the index name.
        """
        for season, times in index_groups.groups.items():
            index_time_series= self.format_index(index_groups[season])
            if len(index_time_series) < 10:
                print(f"{key_name} in {season} has fewer than 10 data. "\
                    "Sample size too small: it won't be correlated.")
                continue
            else:
                if season not in self._index_dict:
                    self._index_dict[season] = {}
                self._index_dict[season][key_name] = (index_time_series, times)


    def format_index(self, index):
        """Returns flattened index array with no NaN values."""
        index_array = np.array(index).flatten()
        index_array = index_array[~np.isnan(index_array)]
        return index_array
        
    
    @staticmethod
    def group_seasonal_data(ds):
        """Groups xarray.Dataset seasonally."""
        return ds.groupby('time.season')


    def get_lon_groups(self, zw3):
        """
        Groups Goyal's ZW3 index into longitude bins.

        Arguments
        ---------
        zw3: xarray.Dataset
            Dataset containing a time series for Goyal's ZW3 index, must contain both 
            magnitude and phase.
        
        Returns
        -------
        groups_zw3: xarray.Dataset.groupby
            Dataset grouped by longitude bins.
        """
        if self._zw3_bins == "30_deg":
            bins = [-180, -150, -120, -90, -60, -30, 0, 30, 60, 90, 120, 150, 180]
            labels = [
                '-180_-150', '-150_-120', '-120_-90', '-90_-60', '-60_-30', 
                '-30_0', '0_30', '30_60', '60_90', '90_120', '120_150', '150_180'
            ]
        elif self._zw3_bins == "60_deg":
            bins = [-180, -120, -60, 0, 60, 120, 180]
            labels = [
            '-180_-120', '-120_-60', '-60_0', '0_60', '60_120', '120_180'
            ]

        groups_zw3 = zw3.groupby_bins(
            group=zw3.zw3index_phase, bins=bins, 
            labels=labels, right=False, include_lowest=True
            )

        return groups_zw3

