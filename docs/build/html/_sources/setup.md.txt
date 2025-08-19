# Setup

## Install

Go to 
`<https://www.anaconda.com/download>`
then follow the instruction to download Anaconda on your machine.

## Fork the repository 

    // from my personal github repo
    git fork https://github.com/LiamBuchart/prometheus_interp.git

Now navigate to the `docs/source` directory. The jupyter notebook which contains all that you need is named `define_vars.ipynb`. This notebook calls all other python scripts that are used. The directory structure is dictated by the use of sphinx and how I want to host it. Sorry that its messy, its who I am. 

## Create a conda environment

    `conda create --name <my-env>` 

The `<my-env>` can be whatever name that you want for the conda environment. Follow the prompts and accept any terms and click `y` to install the environment. Finally, activate the environment with: 

    `conda activate <my-env>`

### Install the necessary packages

Use the `conda install -c conda-forge` extension to install the following required packages:

> numpy pandas |
> geopandas |
> scipy |
> ipyleaflet |
> ipywidgets |
> xarray dask netcdf4 bottleneck |
> cfgrib |

In general, the order that you install these packages does not matter execpt for two cases. Ensure that both `numpy` and `pandas` are installed before `xarray`. Ensure that `xarray` is installed before `cfgrib`.

## Running

The `define_vars` script is designed to be run cell by cell. There are some written instructions to help with running each cell. Modify the widgets for your run and make sure to click on the interactive map to select the location for interpolation. 

## Completion

When finished make sure you deactivate the conda environment

    `conda deactivate <my-env>`