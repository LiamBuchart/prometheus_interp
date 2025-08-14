"""

    Download the shapefile for NFDB fire polygons from the CWFIS website
    and save it in the current working directory.

    Liam.Buchart@nrcan-rncan.gc.ca
    July 30, 2025

"""

from pathlib import Path
import os
import geopandas as gpd
import requests
import shutil

# use wget to download the file
extensions = [".shp", ".shx", ".dbf", ".prj"]
link = "https://cwfis.cfs.nrcan.gc.ca/downloads/hotspots/perimeters"
json_file = "Canada_perimeters.geojson"

cwd = Path.cwd()

# check to see if the shapefile already exists
if os.path.exists("perimeters.shp"):
    # delete the shapefile if it exists
    print("Shapefile already exists. Downloading the latest data...")
    for ext in extensions:
        os.remove(f"perimeters{ext}")  

## Download the NFDB fire polygons using wget
for ext in extensions:

    with requests.get(f"{link}{ext}", stream=True) as r:
        r.raise_for_status()
        with open(f"perimeters{ext}", 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded perimeters{ext}")

# convert the shapefile to a GeoJson file
gdf = gpd.read_file(f"./perimeters.shp") 
gdf.to_file(json_file, driver='GeoJSON')
