"""

    Extract the forecast data from the ECCC data mart
    use file_funcs to set up wget commands
    run in define_vars based on user input details

    Liam.Buchart@nrcan-rncan.gc.ca
    July 30, 2025

"""

from pathlib import Path
import os
import geopandas as gpd
import xarray as xr

# use wget to download the file
link = "https://dd.weather.gc.ca/"

# function to interpolate grib2 file data to a point
def interpolate_grib2_to_point(grib2_file, variables, point):
    """
    Interpolates grib2 file data to a specific point.   
    """

    # open file with xarray
    ds = xr.open_dataset(grib2_file, engine='cfgrib')

    # dictionary to hold the interpolated data
    interpolated_data = {}
    for var in variables:
        if var in ds:
            # interpolate the variable to the point
            interpolated_data = ds[var].interp(lat=point[0], lon=point[1], method='linear')
            print(f"Interpolated {var} at {point}: {interpolated_data.values}")

            # add value to the dictionary
            interpolated_data[var] = interpolated_data.values.item()
        else:
            print(f"Variable {var} not found in the dataset.")

    return interpolated_data

