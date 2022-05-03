import numpy as np
import pandas as pd
import xarray as xr

from pathlib import Path


def create_fake_index(data: dict, months=12, path=Path(".")):
    """
    Creates an index dataset from data input with dimensions 'time'.
    """
    assert isinstance(data, dict), "Data must be a dictionary."

    start_date = np.datetime64('2000-01-01')
    time = pd.date_range(start_date, periods=months, freq="M")

    ds = xr.Dataset(
        data_vars=data,
        coords=dict(
            time=time,
        ),
        attrs=dict(description="Fake index data."),
    )

    ds.to_netcdf(path / "fake_index.nc")
    ds.close()

    return path / "fake_index.nc"


def create_fake_anoms(data: dict, dims, path=Path(".")):
    """
    Creates a anomalies dataset from data input with coordinates 'time', 
    'lat' and 'lon'.
    """
    assert isinstance(data, dict), "Data must be a dictionary."

    start_date = np.datetime64('2000-01-01')
    time = pd.date_range(start_date, periods=dims[2], freq="M")
    lon = np.arange(dims[0])
    lat = -np.arange(dims[1])

    ds = xr.Dataset(
        data_vars=data,
        coords=dict(
            time=time,
            lon=(["lon"], lon),
            lat=(["lat"], lat),
        ),
        attrs=dict(description="Fake anoms data."),
    )

    ds.to_netcdf(path / "fake_anoms.nc")
    ds.close()

    return path / "fake_anoms.nc"
