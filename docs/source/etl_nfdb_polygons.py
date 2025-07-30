"""

    Download the shapefile for NFDB fire polygons from the CWFIS website
    and save it in the current working directory.

    Liam.Buchart@nrcan-rncan.gc.ca
    July 30, 2025

"""

from pathlib import Path
import wget
import os
import geopandas as gpd

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
    ff = wget.download(f"{link}{ext}", out=str(cwd))

# convert the shapefile to a GeoJson file
gdf = gpd.read_file(f"./perimeters.shp") 
gdf.to_file(json_file, driver='GeoJSON')
#with open(json_file, 'w') as f:
#    f.write(gdf.to_json())