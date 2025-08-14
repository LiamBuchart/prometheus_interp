"""

    Extract the forecast data from the ECCC data mart
    use file_funcs to set up wget commands
    run in define_vars based on user input details

    Liam.Buchart@nrcan-rncan.gc.ca
    July 30, 2025

"""

import cfgrib
import os
import xarray as xr
import requests
import shutil
import numpy as np

from scipy.spatial import cKDTree
from scipy.interpolate import griddata


# function to download each file using requests
def download_data(full_path, file_name):
    try:
        # Send a GET request to download the file
        response = requests.get(full_path, stream=True)
        response.raise_for_status()  # Check for HTTP request errors

        # Write the content to a local file
        with open(file_name, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File downloaded successfully: {file_name}, moving to /temp/ ...")    

        dst_dir = "./temp"
        # clear .grib2 files from the temp directory 
        for file in os.listdir(dst_dir):
            if file.endswith(".grib2"):
                file_path = os.path.join(dst_dir, file)
                os.remove(file_path)

        # move the file to the temp directory 
        shutil.move(file_name, os.path.join(dst_dir, file_name))

        print("Commence interpolation")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# function to interpolate grib2 file data to a point using KDTree lookup
def KDTree_interpolate_grib2_to_point(grib2_file, var, point):
    """
    Interpolates grib2 file data to a specific point.   
    """

    # open file with xarray
    ds = xr.open_dataset(f"{grib2_file}", engine='cfgrib', backend_kwargs={'indexpath': ''})
    
    # get coordinate grids as numpy
    lats = ds.coords["latitude"].values.flatten()
    lons = ds.coords["longitude"].values.flatten()

    coords = np.column_stack( (lats, lons))

        # get required met values as numpy
    array = ds[str(var)].values.flatten()

    tree = cKDTree(coords)
    dist, idx = tree.query((point[0], point[1]))

    nearest_lat, nearest_lon = coords[idx]
    nearest_met = array[idx]
    
    return nearest_lat, nearest_lon, nearest_met


# interpolate to a point using linear interpolation
def GRID_interpolate_grib2_to_point(grib2_file, var, point):
    """
    Interpolates grib2 file data to a specific point.   
    """

    # open file with xarray
    ds = xr.open_dataset(f"{grib2_file}", engine='cfgrib', backend_kwargs={'indexpath': ''})
    
    # get coordinate grids as numpy
    lats = ds.coords["latitude"].values
    lons = ds.coords["longitude"].values

    # get required met values as numpy
    array = ds[str(var)].values
    
    # interpolate with scipy to the specified point
    points = np.array( (lons.flatten(), lats.flatten()) ).T
    values = array.flatten()

    val0 = griddata(points, values, (point[1], point[0]))

    return val0
