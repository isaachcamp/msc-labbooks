"""
Conducts False Discovery Rate significance testing on correlation maps and
plots boolean True/False on contour map.
"""

import xarray as xr
import numpy as np
from scipy import stats
from pathlib import Path

import cartopy.crs as ccrs
import matplotlib.pyplot as plt


def ttest_corr(r, dof):
    """Calculates t-score for correlation coefficients."""
    return r * np.sqrt(dof / (1 - r**2))


def fdr_test(ds):
    n = ds.attrs['sample_size']
    dof = n-2
    alpha = 0.1
    N = ds.lat.size * ds.lon.size
    i = 1

    tscores = ds.map(ttest_corr, args=[dof])
    abs_tscores = tscores.map(np.abs)
    pvals = abs_tscores.map(stats.t.sf, args=[dof]) * 2

    sorted_pvals = pvals.to_dataframe().reset_index().sort_values('corr', axis=0, ascending=True)
    sorted_pvals.rename(columns={'corr':'pval'}, inplace=True)
    sorted_pvals['significant'] = np.zeros((sorted_pvals['pval'].size, 1), dtype=bool)

    for idx, row in sorted_pvals.iterrows():
        if row['pval'] < i * (alpha/N):
            sorted_pvals['significant'].at[idx] = True
        elif row['pval'] > i * (alpha/N):
            break
        i += 1

    sorted_pvals.set_index(['lat', 'lon'], inplace=True)
    sorted_pvals.sort_index(inplace=True)
    corr_sig = xr.Dataset.from_dataframe(sorted_pvals)
    
    return corr_sig


def plot_FDR(corr_sig):
    # Set map projection for consistency with data.
    map_projection = ccrs.Orthographic(central_longitude=0.0, central_latitude=-90.0)
    extent = [-180, 180, -90, -20]

    fig = plt.figure(figsize=(12,9))
    ax = plt.subplot(1, 1, 1, projection=map_projection)
    ax.set_extent(extent, ccrs.PlateCarree())
    ax.contour(
        corr_sig.lon, corr_sig.lat,
        corr_sig['significant'], 
        transform=ccrs.PlateCarree(),
        colors='grey',
        linewidths=0.8,
        linestyles='dashed'
        )
    ax.coastlines()

    fig.show()

    output_path = Path("/Users/home/campbeis/Documents/msc-research/data/corr/yearly/")
    output_fname = "mean_sam_rank_corr_significant.png"

    out_dest = output_path / output_fname
    plt.savefig(out_dest, format='png')


if __name__ == "__main__":
    path = Path("/Users/home/campbeis/Documents/msc-research/data/corr/yearly/")
    file = "mean_sam_rank_corr.nc"
    corr_ds = xr.open_dataset(path / file)

    corr_sig = fdr_test(corr_ds)
    plot_FDR(corr_sig)
