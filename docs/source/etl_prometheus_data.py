"""

    Extract the forecast data from the ECCC data mart
    use file_funcs to set up wget commands
    run in define_vars based on user input details

    Liam.Buchart@nrcan-rncan.gc.ca
    July 30, 2025

"""

import subprocess
import pathlib
from pathlib import Path
import os
import geopandas as gpd

from file_funcs import execute_command

# use wget to download the file
link = "https://dd.weather.gc.ca/"


cwd = Path.cwd()
parent = cwd.parent

def get_MSc(filename):
    """
    Get the file name for the MSc data based on user input
    uses wget, might need to switch to sarrcenia if using it alot
    """
    output, error = execute_command(f"wget -P ./temp/ {filename}")

    if error: 
        print(f"Error downloading MSc data: {error}")
        print(f"Isses with the file: {filename}")
    else:
        print(f"Sucessfully downloaded {filename}")
        print(f"Output: {output}")
