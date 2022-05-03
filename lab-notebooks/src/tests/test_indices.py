import pytest
import numpy as np
import pandas as pd
import xarray as xr

from pathlib import Path

from src.corr_cov_maps.load_indices import Indices
from tests.create_fake_data import create_fake_index


def test_indices_attributes():

    # Create fake data
    path = Path("./tests")
    period = 'yearly'
    months = 12 #no. of months in fake index
    data = np.array([x for x in range(months)])
    data_dict = {"fake_index": ("time", data)}

    fake_index_fname = create_fake_index(data_dict, months, path)
    inst = Indices([fake_index_fname], ["fake_index"], period)

    assert inst._filenames == [path / "fake_index.nc"]
    assert inst._variable_names == ["fake_index"]


def test_yearly_index_dict():

    # Create fake data
    path = Path("./tests")
    period = 'yearly'
    months = 12 #no. of months in fake index
    data = np.array([x for x in range(months)])
    data_dict = {"fake_index": ("time", data)}

    fake_index_fname = create_fake_index(data_dict, months, path)
    inst = Indices([fake_index_fname], ["fake_index"], period)
    
    indices = [key for key in inst._index_dict.keys()]

    assert indices[0] == "fake_index"
    assert len(indices) == 1
    assert len(inst._index_dict["fake_index"]) == months


def test_seasonal_index_dict():

    # Create fake data
    path = Path("./tests")
    period = 'seasonal'
    months = 24 #no. of months in fake index
    months_per_year = 12
    years = months // months_per_year
    months_in_season = 3
    data = np.array([x for x in range(months)])
    data_dict = {"fake_index": ("time", data)}

    fake_index_fname = create_fake_index(data_dict, months, path)
    inst = Indices([fake_index_fname], ["fake_index"], period)
    
    seasons = [key for key in inst._index_dict.keys()]
    values = [values for key,values in inst._index_dict.items()]

    for season in ["DJF", "MAM", "JJA", "SON"]:
        assert season in seasons
    assert len(seasons) == 4 #seasons
    for array in values:
        # array should be tuple of time indices and data.
        assert np.all(len(array['fake_index']) == 2)

        assert len(array['fake_index'][0]) == months_in_season * years
        assert len(array['fake_index'][1]) == months_in_season * years

        # Test all indices are integer values
        time_indices_dtype = np.array([isinstance(x, int) for x in array['fake_index'][1]])
        assert np.all(time_indices_dtype == True)


def test_group_seasonal_data():
    
    # Create fake data
    path = Path("./tests")
    period = 'seasonal'
    months = 12 #no. of months in fake index
    data = np.array([x for x in range(months)])
    data_dict = {"fake_index": ("time", data)}

    fake_index_fname = create_fake_index(data_dict, months, path)
    ds = xr.open_dataset(fake_index_fname)
    seasons_ds = Indices.group_seasonal_data(ds)
    seasons = [season for season in seasons_ds.groups.keys()]
    da_list = [da for season,da in seasons_ds.groups.items()]

    for season in ["DJF", "MAM", "JJA", "SON"]:
        assert season in seasons
    
    assert da_list[0] == [0, 1, 11]
    assert da_list[2] == [2, 3, 4]
    assert da_list[1] == [5, 6, 7]
    assert da_list[3] == [8, 9, 10]


def test_get_lon_groups():

    # Create fake data
    path = Path("./tests")
    months = 12 #no. of months in fake index

    # One data point in each 30 degree longitude bin
    data = np.array([x * 30 - 180 for x in range(months)])
    data_dict = {
        "zw3index_magnitude": ("time", data),
        "zw3index_phase": ("time", data)
    }

    fake_index_fname = create_fake_index(data_dict, months, path)
    ds = xr.open_dataset(fake_index_fname)
    groups_zw3 = Indices.get_lon_groups(ds)

    assert "zw3index_magnitude" in ds
    assert len(groups_zw3.groups.keys()) == 12


def test_zw3_dicts():

    # Create fake data
    path = Path("./tests")
    period = 'yearly'
    months = 60 #no. of months in fake index
    months_per_year = 12
    years = months // months_per_year

    # One data point in each 30 degree longitude bin
    data = np.array([x * 30 - 180 for x in range(months_per_year)] * years)
    data_dict = {
        "zw3index_magnitude": ("time", data),
        "zw3index_phase": ("time", data)
    }
    
    fake_index_fname = create_fake_index(data_dict, months, path)
    inst = Indices([fake_index_fname], ["zw3index_magnitude"], period)

    assert len(inst._index_dict.keys()) == 12
    for key,value in inst._index_dict.items():
        # value should be tuple of time indices and data.
        assert len(value) == 2
        assert len(value[0]) == years
        assert len(value[1]) == years

        # Test all indices are integer values
        time_indices_dtype = np.array(
            [isinstance(x, int) for x in value[1]]
            )
        assert np.all(time_indices_dtype == True)
    
    # Test for the first time index equal to monotonically increasing
    # i value as per fake index data creation.
    for i,time_indices in enumerate(inst._index_dict.values()):
        assert time_indices[1][0] == i


def test_zw3_seasonal_dicts():
    
    # Create fake data
    path = Path("./tests")
    period = 'seasonal'
    months = 36 # no. of months in fake index.
    months_per_year = 12
    years = months // months_per_year
    lon_bins_per_season = 3 # Same as no. of months per season.

    # One data point in each 30 degree longitude bin
    data = np.array([x * 30 - 180 for x in range(months_per_year)] * years)
    print(data)
    data_dict = {
        "zw3index_magnitude": ("time", data),
        "zw3index_phase": ("time", data)
    }
    
    fake_index_fname = create_fake_index(data_dict, months, path)
    inst = Indices([fake_index_fname], ["zw3index_magnitude"], period)

    seasons_index = [key for key in inst._index_dict.keys()]

    assert len(seasons_index) == 4 # four seasons
    for season in ["DJF", "MAM", "JJA", "SON"]:
        assert season in seasons_index
        assert len(inst._index_dict[season].keys()) == lon_bins_per_season
