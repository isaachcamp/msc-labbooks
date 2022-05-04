#!/usr/bin/env python
# coding: utf-8

# # Correlation & Covariance Maps
# 
# This module calculates the correlation & covariance between indices time series and anomaly time series, variance and mean height, at each longitude/latitude grid point. Methods used are both Pearson and Spearman rank.
# 
# Call made to class that creates and saves figures based on correlation and covariance matrices.
# 

# In[1]:


import xarray as xr
import numpy as np

from pathlib import Path

from load_indices import Indices
from create_maps import CreateMaps


class CorrCovMaps(): 
    """ 
    Attributes
    ----------
    self._path: str
        Root directory.
    self._anoms: xarray.Dataset
        Dataset containing time series for all lat/lon grid points.
    self._index_dict: dict
        Dictionary containing arrays of all normalised indices' time series.
    self._corr_arrays: numpy.ndarray
        Array to store correlation values between index and all lat/lon 
        grid points.
    self._cov_arrays: numpy.ndarray
        Array to store covariance values between index and all lat/lon 
        grid points.   
    self._stat: str
        Specifies whether the anomalies are either mean height or bandpassed
        variance.
    self._method: str
        Specifies whether to use Pearson product-moment correlation or
        Spearman rank correlation.
    self._period: str
        Indicates whether the input data should be processed seasonally or 
        yearly.
    """

    def __init__(self, anoms, indices, stat, method, period, path=None):
        """
        Creates correlation and covariance arrays and saves to NetCDF4 files.

        Sets object attributes and creates correlation and covariance array 
        attributes as nested dictionaries. Calculates covariance and 
        correlation between all indices contained with indices argument and
        anomalies at every latitude/longitude grid point.
        
        Creates new directories for organising output files according to 
        correlation or covariance and period. Correlation and covariance 
        arrays are then saved as NetCDF4 files, to the appropriate directory. 

        Arguments
        ---------
        anoms: xarray.Dataset
            Dataset containing all anomalies, with dimensions "latitude", 
            "longitude" and "time.
        indices: Indices object
            Possess Indices._index_dict attribute required for calculating 
            correlations and covariance.
        stat: str
            Specifies whether the anomalies are either mean height or 
            bandpassed variance.
        method: str
            Specifies whether to use Pearson product-moment correlation or
            Spearman rank correlation.
        period: str
            Indicates whether the input data should be processed seasonally
            or yearly.
        path: str
            Root directory.
        """

        self._path = path
        self._anoms = anoms
        self._index_dict = indices._index_dict
        self._stat = stat
        self._method = method
        self._period = period

        if self._path == None or self._path == "":
            raise Exception("No path given, no figures created.")

        self._corr_arrays = self.create_corr_cov_dict()
        self._cov_arrays = self.create_corr_cov_dict()

        self.populate_corr_cov_matrices()
      

    def populate_corr_cov_matrices(self):
        """
        Populates covariance and correlation dictionaries.

        Handles seasonal and yearly time series. This function loops through each key
        and sub-key in the self._index_dict attribute. The anomalies are filtered 
        according to the times indexes -- the second item in the index tuple. The 
        index series is then reformatted into a dataset and aligned with the
        filtered anomalies dataset. These are passed to the method that calculates
        correlation/covariance matrices, which are then assigned to the 
        key/sub-key of self._corr_arrays/self._cov_arrays corresponding to the 
        equivalent key/sub-key of self._index_dict.

        For example, if self._period is "seasonal", the loop will go through the 
        "DJF" key of the self._index_dict, then "DMI" sub-key. Once calculated,
        the correlation array will be assigned to self._corr_arrays["DJF"]["DMI"].

        Finally, self._corr_arrays and self._cov_arrays are passed to the method
        that writes NetCDF files.
        """

        if self._period == 'seasonal':
            for season,indices in self._index_dict.items():
                for index_name,index_tuple in indices.items():
                    # Separate tuple of index values and time indices.
                    index_times = index_tuple[1]
                    index_values = index_tuple[0]
                    # Remove values for incomplete seasons, i.e. first month of first 
                    # summer and first two months of final summer in anomalies dataset.
                    if season == 'DJF' and self._period == 'seasonal':
                        index_times = index_times[2:-1]
                        index_values = index_values[2:-1]
                    anoms_filtered = self._anoms.isel(time=index_times)
                    
                    # Create index dataset object.                     
                    index_ds = self.create_indices_dataset(
                        anoms_filtered,
                        index_values, 
                        index_name
                    )
                    # Calculate corr & cov arrays for this season and index.
                    corr_arr, cov_arr = self.calculate_corr_cov_matrices(
                        anoms_filtered, index_ds, index_name
                    )
                    self._corr_arrays[season][index_name] = corr_arr
                    self._cov_arrays[season][index_name] = cov_arr
        else:
            for index_name, index_tuple in self._index_dict.items():
                # Separate tuple of index values and time indices.
                if "zw3" in index_name:
                    index_times = index_tuple[1]
                    index_values = index_tuple[0]
                    anoms_filtered = self._anoms.isel(time=index_times)
                else:
                    index_values = index_tuple[0]
                    anoms_filtered = self._anoms
                # Create index dataset object.
                index_ds = self.create_indices_dataset(
                        anoms_filtered,
                        index_values, 
                        index_name
                    )
                # Calculate corr & cov arrays for this index.
                corr_arr, cov_arr = self.calculate_corr_cov_matrices(
                    anoms_filtered, index_ds, index_name
                )
                self._corr_arrays[index_name] = corr_arr
                self._cov_arrays[index_name] = cov_arr

        self._anoms.close()
        if self._path != None:
            self.write_to_netcdf(self._corr_arrays, 'corr')
            self.write_to_netcdf(self._cov_arrays, 'cov')

    
    def create_corr_cov_dict(self):
        """
        Creates nested dictionary with same structure as self._index_dict.

        Creates a nested dictionary with keys corresponding to an index name. 
        If self._period is "seasonal", the first order keys will be named 
        according to the season, and a second order of sub keys will contain the
        index name, i.e. the same structure as self._index_dict. The returned 
        dictionary is used to store data for correlation and covariance values 
        for the entire lat/lon grid.
        
        Returns
        -------
        arrays: dict
            Dictionary with the same structure as index_dict. Each key is assigned
            a None type as a placeholder.
        """
        arrays = {}

        for key in self._index_dict.keys():
            if self._period == 'seasonal':
                for subkey in self._index_dict[key].keys():
                    if key not in arrays:
                        arrays[key] = {}
                    arrays[key][subkey] = None
            else:
                arrays[key] = None
        
        return arrays

    
    def create_indices_dataset(self, anoms, index_values, index_name):
        """
        Returns index as Dataset type with additional lat & lon dimensions.

        Inputted index as an array possesses only "time" dimension, however,
        in order to use xarray's native corr and cov methods, the index 
        must have the same dimensions as the anomalies dataset. This 
        function takes the index time series array and forms a numpy array 
        of equivalent dimensions i.e. 3D with latitude, longitude and time.
        The newly formed array contains a repeat of the time series at every
        longitude, latitude grid point.
        
        The numpy array is converted into an xarray.Dataset object using the 
        anoms coordinates for consistency between the two datasets.

        Arguments
        ---------
        anoms: xarray.Dataset
            Dataset containing the filtered anomalies. Used for consistency 
            of coordinate dimensions with the new index dataset.
        index_values: numpy.ndarray
            Array containing the index time series.
        index_name: str
            Name of the index, used to assign variable name for new index
            dataset.

        Returns
        -------
        ds: xarray.Dataset
            Index dataset with dimensions along latitude, longitude and time.
        """
        lon = anoms.lon
        lat = anoms.lat
        time = len(index_values)
        n = lon.size * lat.size

        # Create 3D array of repeated time series
        index_flattened = np.repeat(index_values[None, :], n, axis=0)
        index_data = index_flattened.reshape((lon.size, lat.size, time))

        # Create index dataset.
        ds = xr.Dataset(
                data_vars={
                    index_name:(('lon', 'lat', 'time'), index_data)
                    },
                coords={
                    'lon':lon,
                    'lat':lat, 
                    'time':anoms.time[:time]
                }
            )
        return ds

    
    def calculate_corr_cov_matrices(self, anoms, index_ds, index_name):
        """
        Returns covariance and correlation matrices of two input datasets.

        Filtered anomalies and index datasets are converted to DataArray 
        objects so as to use the xarray native methods corr and cov. The 
        method for calculating correlation and covariance is determined by
        the self._method attribute.

        Arguments
        ---------
        anoms: xarray.Dataset
            Dataset containing the filtered anomalies of mean or variance
            fields.
        index_ds: xarray.Dataset
            Dataset containg the 3D index with latitude and longitude 
            dimensions.
        index_name: str
            Name of index in the index_ds, used for converting the Dataset
            into a xarray.DataArray object.

        Returns
        -------
        corr_matrix: xarray.DataArray
            Matrix containing pearson or spearman correlation values 
            between index and anomalies time series at all lon/lat grid
            points.
        cov_matrix: xarray.DataArray
            Matrix containing pearson or spearman covariance values 
            between index and anomalies time series at all lon/lat grid
            points.
        """
        anoms_arr = anoms.z
        index_arr = index_ds[index_name]
        anoms_arr, index_arr = xr.align(anoms_arr, index_arr)

        if self._method == 'pearson':
            corr_matrix = xr.corr(anoms_arr, index_arr, dim='time')
            cov_matrix = xr.cov(anoms_arr, index_arr, dim='time')
        elif self._method == 'rank':
            # Rank DataArray objects before passing to corr and cov methods.
            ranked_anoms = anoms_arr.rank(dim='time')
            ranked_index = index_arr.rank(dim='time')
            corr_matrix = xr.corr(ranked_anoms, ranked_index, dim='time')
            cov_matrix = xr.cov(ranked_anoms, ranked_index, dim='time')

        return corr_matrix, cov_matrix


    def write_to_netcdf(self, arrays: dict, var='corr'):
        """
        Writes NetCDF file with dimensions at specified path location.

        Creates parent directories if required. Loops through every key
        & sub-key and writes each as a separate NetCDF file. Ensures
        that all output files having ordered dimensions: ("lat", "lon").
        This is for consistency in creating figures.
        """
        self._opath = self._path / var / self._period
        self._opath.mkdir(parents=True, exist_ok=True)

        # Handle seasonal data.
        if self._period == 'seasonal':
            for season_name,indices_dict in arrays.items():
                for index_name,index_da in indices_dict.items():
                    ds = index_da.to_dataset(name=var)
                    ds = ds.transpose("lat", "lon")
                    filename = season_name + '_' + self._stat + '_' \
                        + index_name + '_' + self._method + '_' \
                        + var +  '.nc'
                    ds.to_netcdf(self._opath / filename)
                    ds.close()
        else:
            for index_name,index_da in arrays.items():
                ds = index_da.to_dataset(name=var)
                ds = ds.transpose("lat", "lon")
                filename = self._stat + '_' \
                    + index_name + '_' + self._method + '_' \
                    + var +  '.nc'
                ds.to_netcdf(self._opath / filename)
                ds.close()


if __name__ == "__main__":
    path = Path("G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\")
    index_path = Path("G:\\Isaac\\Documents\\msc-research\\data\\indices\\")

    var_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_bandpass_20S_mon_var_anoms.nc"
    mean_file = "era5_h500_daily_1979_2021_1deg_deseasonalised_20S_mon_anoms.nc"

    variance_anoms = xr.open_dataset(path / var_file)
    mean_anoms = xr.open_dataset(path / mean_file)
    index_files = list(index_path.glob("*.nc"))

    # Default options, control outputs here.
    period = 'seasonal'
    zw3_bins="60_deg"
    variable_names = ['zw3index_magnitude',]#'sam', 'SOI', 'DMI', ]

    indices = Indices(index_files, variable_names, period, zw3_bins)

    anoms = [(variance_anoms, 'variance'), (mean_anoms, 'mean')]
    methods = ['rank', 'pearson',]

    for anom in anoms:
        for method in methods:
            inst = CorrCovMaps(
                    anom[0], 
                    indices, 
                    stat=anom[1],
                    method=method, 
                    period=period,
                    path=None
                    )
    
    # Currently loops through every file found in the directory,
    # not just the ones created in the current iteration.
    corr_maps = CreateMaps(inst._path, 'corr', inst._period)
    cov_maps = CreateMaps(inst._path, 'cov', inst._period)


