# Setup

## Install

It is highly recommended that you have Visual Studio Code installed on your machine before running this. Jupyter Notebook does not like the required javascript to produce an interactive map. Please go to `https://code.visualstudio.com/download` to download and follow the intstruction. Is you do not have python on your machine, that will be the next step. 

Go to 
`<https://www.anaconda.com/download>`
then follow the instruction to download Anaconda on your machine.

## Using VSCode

Once you have VSCode installed on your machine simply oopen it and configure the settings they suggest. Once completed, at the top of the window, select `Terminal` from the bar. Then click `New Terminal`. This will open a Powershell of similar terminal at the bottom of the window. You can navigate as you typically would. 

In this terminal, navigate to the directory where you want to download the folder. This is also where all of the lines of code shown below will be run.

## Fork the repository 

Pick one of the following:

    git clone https://github.com/LiamBuchart/prometheus_interp.git
    git fork https://github.com/LiamBuchart/prometheus_interp.git

If you have already installed this once before, you can instead run:

    git pull https://github.com/LiamBuchart/prometheus_interp.git

Now navigate to the `docs/source` directory. The jupyter notebook which contains all that you need is named `define_vars.ipynb`. This notebook calls all other python scripts that are used. The directory structure is dictated by the use of sphinx and how I want to host it. Sorry that its messy, its who I am. 

## Make Sure to condigure overall python environment

Before seting up our conda enviornment we need to install a module in your python environment so the jupyternotebook can 'see' your conda environments.

    conda install -c conda-forge nb_conda_kernels 

## Create a conda environment

    conda create --name <my-env>

The `<my-env>` can be whatever name that you want for the conda environment. Follow the prompts and accept any terms and click `y` to install the environment. Finally, activate the environment with: 

    conda activate <my-env>

### Install the necessary packages

Use the `conda install -c conda-forge` extension to install the following required packages:

    ipykernel
    numpy pandas 
    geopandas 
    scipy 
    ipyleaflet 
    ipywidgets 
    xarray dask netcdf4 bottleneck 
    cfgrib 
    jupyter

In general, the order that you install these packages does not matter execpt for two cases. Ensure that both `numpy` and `pandas` are installed before `xarray`. Ensure that `xarray` is installed before `cfgrib`.

## Get the python environment active in your window

Once you havew these downloaded we can open the notebook. On the left side of the window there are several symbols, the top of which is a file navigator. Click on this and open the newly downloaded folder (i.e. the folder name `prometheus_interp`). This will give a visual way to navigate the folder structure. Open the `define_vars,ipynb` file from the `docs/source` directory.

Once open, the python environment will be shown at the top right of the .ipynb window. If this is not your newly created conda environment, click on it and then select the name of your new conda environment. VSCode is smart enough to have all the conda environments already listed for you. In the unlikely event that it is not immediately listed hit `select another Kernel` is should then be shown.

## Running

The `define_vars` script is designed to be run cell by cell. In a Jupyter Notebook there are two main way to run each cell.

1. Click in the desired cell, then hit the `run` (play) button at the top. 

2. Click in the desired cell then hit `Shift` + `Enter`. This will activate the cell.

Each cell is numbered. When the cell is running the cell number will change to the `*` sign. Once it return to the previous number, it has been completed. 

There are some written instructions to help with running each cell. Modify the widgets for your run and make sure to click on the interactive map to select the location for interpolation. 

## Completion

When finished make sure you deactivate the conda environment

    conda deactivate <my-env>

The final .csv file will be in the `output` folder. The naming convention is `dd/mm/yyyy_prometheus_slider_<forecast_length (in hours)>`. 