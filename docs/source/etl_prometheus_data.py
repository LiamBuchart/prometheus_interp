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
extensions = [".shp", ".shx", ".dbf", ".prj"]
link = "https://cwfis.cfs.nrcan.gc.ca/downloads/hotspots/perimeters"
json_file = "Canada_perimeters.json"

cwd = Path.cwd()
parent = cwd.parent

# Download the NFDB fire polygons using wget
for ext in extensions:
    output, error = execute_command(f"wget {link}{ext}")

    if error:
        print(f"Error downloading NFDB fire polygons: {error}")
    else:
        print("NFDB fire polygons downloaded successfully.")
        print(f"Output: {output}")