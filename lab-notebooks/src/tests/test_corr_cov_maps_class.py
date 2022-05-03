import pytest
import numpy as np
import pandas as pd
import xarray as xr

from pathlib import Path

from src.corr_cov_maps.corr_cov_maps import CorrCovMaps
from src.corr_cov_maps.load_indices import Indices
from tests.create_fake_data import create_fake_anoms, create_fake_index


def create_fake_data(path, period, dims):
    # Number of repeated time series for lon/lat grid.
    lon = dims[0]
    lat = dims[1]
    time = dims[2]
    n = lon * lat

    data = np.arange(time)
    
    index_data_dict = {"fake_index": ("time", data)}
    fake_index_fname = create_fake_index(index_data_dict, time, path)
    indices = Indices([fake_index_fname], ["fake_index"], period)

    anoms_flattened = np.repeat(data[None, :], n, axis=0)
    anoms_data = anoms_flattened.reshape((lon, lat, time))
    
    anoms_data_dict = {"z": (["lon", "lat", "time"], anoms_data)}
    fake_anoms_fname = create_fake_anoms(anoms_data_dict, dims, path)
    anoms = xr.open_dataset(fake_anoms_fname)

    return anoms, indices


def normalise_sample(arr):
    """
    Normalises an array/sample and returns the standard deviation of sample anomalies.

    Parameters
    ----------
    arr: numpy.ndarray
        Sample to be normalised.
    
    Returns
    -------
    arr_norm: numpy.ndarray
        Normalised time series.
    np.std(arr_anoms): np.float64
        Standard deviation of the time series, later used to calculate covariance.
    """
    arr_anoms = arr - np.mean(arr)
    if np.std(arr_anoms) != 0:
        arr_norm = np.divide(arr_anoms, np.std(arr_anoms))
        return arr_norm, np.std(arr_anoms)
    
    assert np.std(arr_anoms) != 0, "Std is zero, anoms either uniform or zeroes."

    return arr_anoms, np.std(arr_anoms)


def test_attributes():
    
    path = Path("./tests")
    period = 'yearly'

    lon = 2 # no. of lon points, monotonically increasing
    lat = 2 # no. of lat points, monotonically increasing
    sample_size = 12 #no. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    assert inst._path == None
    assert inst._method == 'pearson'
    assert inst._stat == 'mean'
    assert inst._period == period


def test_normalised_yearly_index_and_anoms():

    path = Path("./tests")
    period = 'yearly'

    lon = 2 # no. of lon points, monotonically increasing
    lat = 2 # no. of lat points, monotonically increasing
    sample_size = 36 #no. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    norm_index, index_std = normalise_sample(inst._index_dict['fake_index'])
    anoms_array = np.array(inst._anoms.isel(lat=0, lon=0).to_array())
    norm_anoms_array, anoms_std = normalise_sample(anoms_array)

    assert np.mean(norm_index) == pytest.approx(0.0)
    assert np.std(norm_index) == pytest.approx(1.0)
    assert np.mean(norm_anoms_array) == pytest.approx(0.0)
    assert np.std(norm_anoms_array) == pytest.approx(1.0)


def test_normalised_seasonal_index_and_anoms():

    path = Path("./tests")
    period = 'seasonal'

    lon = 2 # no. of lon points, monotonically increasing
    lat = 2 # no. of lat points, monotonically increasing
    sample_size = 36 #no. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    for season in inst._index_dict.keys():
        time_indices = inst._index_dict[season]['fake_index'][1]
        norm_index, index_std = normalise_sample(
            inst._index_dict[season]['fake_index'][0]
            )
        anoms_array = np.array(
            inst._anoms.isel(lat=0, lon=0, time=time_indices).to_array()
            )
        norm_anoms_array, anoms_std = normalise_sample(anoms_array)

        assert np.mean(norm_index) == pytest.approx(0.0)
        assert np.std(norm_index) == pytest.approx(1.0)
        assert np.mean(norm_anoms_array) == pytest.approx(0.0)
        assert np.std(norm_anoms_array) == pytest.approx(1.0)


def test_yearly_create_corr_cov_dict():
    
    path = Path("./tests")
    period = 'yearly'

    lon = 2 # no. of lon points, monotonically increasing
    lat = 2 # no. of lat points, monotonically increasing
    sample_size = 36 #no. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    arrays_keys = [key for key in inst._correlation_arrays.keys()]

    assert arrays_keys[0] == "fake_index"
    assert len(arrays_keys) == 1
    assert inst._correlation_arrays["fake_index"].shape == (lon, lat)


def test_seasonal_create_corr_cov_dict():
    
    path = Path("./tests")
    period = 'seasonal'

    lon = 2 # no. of lon points, monotonically increasing
    lat = 2 # no. of lat points, monotonically increasing
    sample_size = 36 #no. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    seasons = [key for key in inst._correlation_arrays.keys()]

    assert len(seasons) == 4 # No. of seasons
    for season in seasons:
        assert season in ["DJF", "MAM", "JJA", "SON"]
        assert inst._correlation_arrays[season]["fake_index"].shape == (lon, lat)


def test_yearly_pearson_corr_cov_matrices():
    
    path = Path("./tests")
    period = 'yearly'

    lon = 2 # No. of lon points, monotonically increasing
    lat = 2 # No. of lat points, monotonically increasing
    sample_size = 24 # No. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    index = inst._index_dict["fake_index"]
    variable_name = 'fake_index'

    # Arrays are the same hence should be perfectly correlated.
    # Note: xarray covariance method divides by n-1.
    norm_anoms, anoms_std = normalise_sample(index)
    norm_index, index_std = normalise_sample(index)

    sample_correction = sample_size / (sample_size-1) # Factor to adjust for finite sample.
    true_corr = 1.0
    true_cov = 1.0 * anoms_std * index_std * sample_correction

    index_ds = inst.create_indices_dataset(anoms, index, variable_name)
    corr_matrix, cov_matrix = inst.calculate_corr_cov_matrices(
        anoms, 
        index_ds, 
        "fake_index"
        )

    assert np.all(corr_matrix == pytest.approx(true_corr))
    assert corr_matrix.shape == (lon, lat)
    assert np.all(cov_matrix == pytest.approx(true_cov))
    assert cov_matrix.shape == (lon, lat)


def test_seasonal_pearson_corr_cov_matrices():
    
    path = Path("./tests")
    period = 'seasonal'

    lon = 2 # No. of lon points, monotonically increasing
    lat = 2 # No. of lat points, monotonically increasing
    sample_size = 24 # No. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    for season in inst._index_dict.keys():
        # Remove incomplete seasons as per processing in populate_corr_cov_matrices.
        if season == "DJF":
            index = indices._index_dict[season]["fake_index"][0][2:-1]
            time_indices = indices._index_dict[season]["fake_index"][1][2:-1]
        else:
            index = indices._index_dict[season]["fake_index"][0]
            time_indices = indices._index_dict[season]["fake_index"][1]

        season_anoms = anoms.isel(lat=0, lon=0, time=time_indices).to_array()
        season_anoms_arr = np.array(season_anoms)
        sample_size = len(index)

        index_norm_arr, index_std = normalise_sample(index)
        anoms_norm_arr, anoms_std = normalise_sample(season_anoms_arr)

        # Arrays are the same hence should be perfectly correlated.
        # Note: pearson method divides by n-1, rank divides by n.
        sample_correction = sample_size / (sample_size-1) # Factor to adjust for finite sample.
        true_corr = 1.0
        true_cov = 1.0 * anoms_std * index_std * sample_correction
        
        corr_matrix = inst._correlation_arrays[season]["fake_index"]
        cov_matrix = inst._covariance_arrays[season]["fake_index"]

        assert corr_matrix.shape == (lat, lon)
        assert cov_matrix.shape == (lat, lon)
        assert np.all(corr_matrix == pytest.approx(true_corr))
        assert np.all(cov_matrix == pytest.approx(true_cov))


def test_yearly_rank_corr_cov_matrices():

    path = Path("./tests")
    period = 'yearly'

    lon = 2 # No. of lon points, monotonically increasing
    lat = 2 # No. of lat points, monotonically increasing
    sample_size = 24 # No. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='rank',
        period=period, 
        path=None
    )

    index = inst._index_dict["fake_index"]
    variable_name = 'fake_index'

    # Arrays are the same hence should be perfectly correlated.
    # Note: xarray covariance method divides by n-1.
    norm_anoms, anoms_std = normalise_sample(index)
    norm_index, index_std = normalise_sample(index)

    sample_correction = sample_size / (sample_size-1) # Factor to adjust for finite sample.
    true_corr = 1.0
    true_cov = 1.0 * anoms_std * index_std * sample_correction

    index_ds = inst.create_indices_dataset(anoms, index, variable_name)
    corr_matrix, cov_matrix = inst.calculate_corr_cov_matrices(
        anoms, 
        index_ds, 
        "fake_index"
        )

    assert np.all(corr_matrix == pytest.approx(true_corr))
    assert corr_matrix.shape == (lon, lat)
    assert np.all(cov_matrix == pytest.approx(true_cov))
    assert cov_matrix.shape == (lon, lat)


def test_seasonal_rank_corr_cov_matrices():
    
    path = Path("./tests")
    period = 'seasonal'

    lon = 2 # No. of lon points, monotonically increasing
    lat = 2 # No. of lat points, monotonically increasing
    sample_size = 24 # No. of months in fake anoms and index
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='rank',
        period=period, 
        path=None
    )

    for season in inst._index_dict.keys():
        # Remove incomplete seasons as per processing in populate_corr_cov_matrices.
        if season == "DJF":
            index = indices._index_dict[season]["fake_index"][0][2:-1]
            time_indices = indices._index_dict[season]["fake_index"][1][2:-1]
        else:
            index = indices._index_dict[season]["fake_index"][0]
            time_indices = indices._index_dict[season]["fake_index"][1]

        season_anoms = anoms.isel(lat=0, lon=0, time=time_indices).to_array()
        season_anoms_arr = np.array(season_anoms)
        sample_size = len(index)

        index_norm_arr, index_std = normalise_sample(index)
        anoms_norm_arr, anoms_std = normalise_sample(season_anoms_arr)

        # Arrays are the same hence should be perfectly correlated.
        # Note: pearson method divides by n-1, rank divides by n.
        sample_correction = sample_size / (sample_size-1) # Factor to adjust for finite sample.
        true_corr = 1.0
        true_cov = 1.0 * anoms_std * index_std * sample_correction
        
        corr_matrix = inst._correlation_arrays[season]["fake_index"]
        cov_matrix = inst._covariance_arrays[season]["fake_index"]

        assert corr_matrix.shape == (lat, lon)
        assert cov_matrix.shape == (lat, lon)
        assert np.all(corr_matrix == pytest.approx(true_corr))
        assert np.all(cov_matrix == pytest.approx(true_cov))


def test_create_index_dataset():

    path = Path("./tests")
    period = 'yearly'

    lon = 2 # No. of lon points, monotonically increasing.
    lat = 2 # No. of lat points, monotonically increasing.
    sample_size = 24 # No. of months in fake anoms and index.
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='rank',
        period=period, 
        path=None
    )

    index = inst._index_dict["fake_index"]
    variable_name = 'fake_index'

    index_ds = inst.create_indices_dataset(anoms, index, variable_name)
    index_array = np.array(index_ds.isel(lat=0, lon=0).to_array())

    assert isinstance(index_ds, xr.Dataset)
    assert np.all(index_array == index)


def test_large_dataset():

    path = Path("./tests")
    period = 'yearly'

    lon = 360 # No. of lon points, monotonically increasing.
    lat = 71 # No. of lat points, monotonically increasing.
    sample_size = 512 # No. of months in fake anoms and index.
    dims = [lon, lat, sample_size]

    # Create fake data
    anoms, indices = create_fake_data(path, period, dims)
    inst = CorrCovMaps(
        anoms,
        indices,
        stat='mean',
        method='pearson',
        period=period, 
        path=None
    )

    index = inst._index_dict["fake_index"]
    variable_name = 'fake_index'

    # Arrays are the same hence should be perfectly correlated.
    # Note: xarray covariance method divides by n-1.
    norm_anoms, anoms_std = normalise_sample(index)
    norm_index, index_std = normalise_sample(index)

    sample_correction = sample_size / (sample_size-1) # Factor to adjust for finite sample.
    true_corr = 1.0
    true_cov = 1.0 * anoms_std * index_std * sample_correction

    index_ds = inst.create_indices_dataset(anoms, index, variable_name)
    corr_matrix, cov_matrix = inst.calculate_corr_cov_matrices(
        anoms, 
        index_ds, 
        "fake_index"
        )

    assert np.all(corr_matrix == pytest.approx(true_corr))
    assert corr_matrix.shape == (lon, lat)
    assert np.all(cov_matrix == pytest.approx(true_cov))
    assert cov_matrix.shape == (lon, lat)
