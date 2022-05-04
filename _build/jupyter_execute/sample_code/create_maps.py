#!/usr/bin/env python
# coding: utf-8

# # Create Maps
# 
# Creates figures of variance & mean height anomalies and saves them as PNG files.
# 
# See docstrings below for more details.

# In[1]:


import xarray as xr
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cartopy.crs as ccrs

from pathlib import Path

class CreateMaps():
    """
    Creates figures of variance & mean height anomalies and saves as PNG files.

    Takes inputs detailing file path. All files with suffix ".nc" located 
    under the file path are globbed into a list. Input files must be variance 
    and mean height field anomalies, and must be in NetCDF4 format. Pairs of
    variance and mean height anomaly data are collated and creates a figures 
    of each pair. 
    
    Every outputted figure is saved to a separate file under a filename 
    derived from the filenames inputted. For example, two files, with names 
    "DJF_mean_sam_rank_corr.nc" and "DJF_variance_sam_rank_corr.nc", will be 
    saved under the name "DJF_sam_rank_corr.png".

    Attributes
    ----------
    self._path: str
        Path to directory containing variance and mean height anomalies 
        files.
    self._mean_files: list
        List of paths to mean height anomalies file locations.
    self._var_files: list
        List of paths to variance anomalies file locations.
    self.labels: dict
        Dictionary of plot labels derived from the file names. Specific
        to each file so repreatedly changed. The final label attribute 
        will correspond to the final files processed.
    """

    def __init__(self, path=Path("."), var='corr', period='yearly'):
        """
        Sets attributes and loops through paired files.
        
        Arguments
        ---------
        path: str
            Path to base directory. 
        var: str
            Name of sub-directory containing the variable.
        period: str
            Name of sub-directory containing files to be plotted.
        """
        if path == None or path == "":
            raise Exception("No path provided, no figures were created, "\
                "skipping process.")
        
        self._path = path / var / period
        
        self.get_files()
        
        for i, mean_file in enumerate(self._mean_files):
            filename = mean_file.parts[-1]
            self.get_plot_labels(filename)
            output_fname = self.get_output_filename(filename) + ".png"

            mean_ds = xr.open_dataset(mean_file)
            var_ds = xr.open_dataset(self._var_files[i])
            
            self.plot_corr_cov_maps(mean_ds, var_ds, output_fname)


    def get_files(self):
        """Creates lists of variance and mean anomalies files as attributes."""
        self._var_files = list(self._path.glob('*variance_*.nc'))
        self._mean_files = list(self._path.glob('*mean_*.nc'))


    def get_plot_labels(self, filename):
        """"
        Returns plot labels as an attribute, derived from file name.
        
        File naming convention is assumed to be the following:
        If seasonal:
            {season}_{variance or mean}_{index name}_{correlation method}_{statistic}.nc
        If not seasonal:
            {variance or mean}_{index name}_{correlation method}_{statistic}.nc

        If index is ZW3, the index naming convention is assumed to be:
            zw3_{phase bin}, e.g. zw3_-120_-90
        """
        self.labels = {}
        parts = filename.split('_')
        
        if parts[0] != 'variance' and parts[0] != 'mean':
            self.labels['season'] = parts[0]
            parts.remove(parts[0])
        
        self.labels['method'] = parts[-2].capitalize()
        if not parts[-3].isalpha():
            self.labels['index'] = parts[1].upper() \
                + " (with Phase between " + parts[2] \
                + " and " + parts[3] + ")"
        else:
            self.labels['index'] = parts[-3].upper()

        corr_cov = parts[-1].split('.')[0]
        self.labels['variable_name'] = corr_cov
        if corr_cov == 'corr':
            self.labels['stat'] = 'Correlation'
        elif corr_cov == 'cov':
            self.labels['stat'] = 'Covariance'


    def get_output_filename(self, filename):
        """Returns output file name derived from the input file name."""
        parts = filename.split('_')
        parts[-1] = parts[-1].split('.')[0]
        parts.remove('mean')
        return '_'.join(parts)


    @staticmethod
    def calibrate_colour_scale(ds, variable_name):
        """Return max and min values for figure colour scale."""
        abs_max_value = np.abs(ds[variable_name]).max()
        return abs_max_value, -abs_max_value


    def plot_corr_cov_maps(self, mean_ds, var_ds, output_fname):
        """
        Create figures and save as PNG files.
        
        Takes input Datasets and plots mean and variance datasets 
        side-by-side. The two share the same projection, but possess 
        independent colour bars. xarray's PlateCarree native projection
        is transformed into Orthographic projection for more digestable 
        figures.

        Arguments
        ---------
        mean_ds: xarray.Dataset
            Dataset containing data of mean height field anomalies.
        var_ds: xarray.Dataset
            Dataset containing data of bandpassed variance anomalies.
        output_fname: str
            Name of PNG output file.
        """
        # Check path exists
        output_path = self._path / 'figures'
        output_path.mkdir(parents=True, exist_ok=True)

        # Fetch plot labels from self.labels attribute
        index = self.labels['index']
        variable_name = self.labels['variable_name']
        stat = self.labels['stat']
        method = self.labels['method']
        
        # Set figure super title.
        figure_title = method + " " + stat + " between " \
            + index \
            + " and 500hPa Geopotential Height Field"
            
        if 'season' in self.labels:
            figure_title = self.labels['season'] + " " + figure_title

        # Set max and min values for colour bar.
        mean_max, mean_min = self.calibrate_colour_scale(mean_ds, variable_name)
        var_max, var_min = self.calibrate_colour_scale(var_ds, variable_name)

        # Set map projection for consistency with data.
        map_projection = ccrs.Orthographic(central_longitude=0.0, central_latitude=-90.0)
        extent = [-180, 180, -90, -20]

        # Create figure with two subplot axes.
        fig = plt.figure(figsize=(15,6))
        
        ax1 = plt.subplot(1, 2, 1, projection=map_projection)
        ax1.set_extent(extent, ccrs.PlateCarree())
        mean_ds[variable_name].plot(
            ax=ax1, 
            transform=ccrs.PlateCarree(),
            vmin=mean_min, vmax=mean_max, 
            cbar_kwargs={'shrink': 0.7},
            cmap=cm.seismic)
        ax1.coastlines()
        ax1.set_title("Mean Height Anomalies")

        ax2 = plt.subplot(1, 2, 2, projection=map_projection)
        ax2.set_extent(extent, ccrs.PlateCarree())
        var_ds[variable_name].plot(
            ax=ax2, 
            transform=ccrs.PlateCarree(),
            vmin=var_min, vmax=var_max, 
            cbar_kwargs={'shrink': 0.7},
            cmap=cm.seismic)
        ax2.coastlines()
        ax2.set_title("2-8 Day Bandpassed Variance Anomalies")

        fig.suptitle(figure_title, fontsize=16)

        out_dest = output_path / output_fname
        plt.savefig(out_dest, format='png')

        plt.close()


if __name__ == "__main__":
    path = Path("G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\")
    corr_maps = CreateMaps(None, "corr", "seasonal")
    cov_maps = CreateMaps(None, "cov", "seasonal")

