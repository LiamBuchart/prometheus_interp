# Setup

## Install

Go to 
`<https://www.anaconda.com/download>`
then follow the instruction to download Anaconda on your machine.

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

Jupyter notebooks can now find your conda environment. 

## Create a conda environment

    conda create --name <my-env>

The `<my-env>` can be whatever name that you want for the conda environment. Follow the prompts and accept any terms and click `y` to install the environment. Finally, activate the environment with: 

    conda activate <my-env>

### Install the necessary packages

Use the `conda install -c conda-forge` extension to install the following required packages:

    numpy pandas 
    geopandas 
    scipy 
    ipyleaflet 
    ipywidgets 
    xarray dask netcdf4 bottleneck 
    cfgrib 
    jupyter-leaflet
    jupyter
    ipykernel
    jupyterlab

In general, the order that you install these packages does not matter execpt for two cases. Ensure that both `numpy` and `pandas` are installed before `xarray`. Ensure that `xarray` is installed before `cfgrib`.

## Getting the jupyter notebook going

There is one more step to make sure this can be run easily. Run:

    python -m ipykernel install --user --name=<my-env>

Make sure that `<my-env>` is the same name as the conda environment that you created. This will ensure that the jupyter notebook can find the kernel and use all of the packages that you have installed. 

Once everything is installed run:

    jupyter notebook

make sure that you are in the `source` directory. This will open the source firectory in your default browser. Now select the `define_variables.ipynb` file to run. At the top right of the python script you should see the name of your kernel. Assuming you had previously activated the kernel all should be well. If the name is different, select `Kernel` from the top menu bar, then navigate down to `Change Kernel...`. You will then be able to select your created Kernel with the necessary packages. Once this is complete, you are ready to step through the notebook.

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