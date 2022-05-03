#!/usr/bin/env python
# coding: utf-8

# In[1]:


import xarray as xr
import numpy as np
import geopandas as gpd

import plotly.graph_objects as go
import plotly.express as px


# In[2]:


import plotly.io as pio
pio.renderers.default = 'notebook'


# In[3]:


path = "G:\\Isaac\\Documents\\msc-research\\data\\ERA5\\daily_data\\"
file = "era5_h500_daily_1979_2021_1deg_20S_deseasonalised_bandpass_mon_var_anoms.nc"


# In[4]:


anoms_ds = xr.open_dataset(path + file)
anoms_df = anoms_ds.isel(time=0, bnds=0).to_dataframe()
anoms_df.reset_index(inplace=True)
anoms_df.drop(columns=['time_bnds'], inplace=True)


# In[6]:


gdf = gpd.GeoDataFrame(
    anoms_df, geometry=gpd.points_from_xy(anoms_df.lon, anoms_df.lat))


# In[90]:


fig1 = go.Contour(
    x=gdf.lon,
    y=gdf.lat,
    z=gdf.z,
    opacity=1.0
)


# In[91]:


fig = go.Figure(
    go.Densitymapbox(
        opacity=0.8
    ),
)
fig.add_traces(fig1)
fig.update_layout(
    mapbox_style='dark',
    mapbox_layers=[
        {
            "below":'traces',
            "sourcetype": "raster",
        }
    ]
)
fig.show()


# In[36]:


fig = px.density_mapbox(
    gdf,
    lat="lat",
    lon="lon",
    z="z",
    center=dict(lat=-90, lon=0),
    zoom=3,
    radius=30,
    opacity=0.5,
)
fig.update_layout(
    mapbox_style="white-bg",
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

