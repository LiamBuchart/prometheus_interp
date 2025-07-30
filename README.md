# prometheus_interp
Tool to interpolate hourly ECCC model output and places it in a Prometheus spreadsheet

This will all be run inside a Jupyter notebook

Goal is to select model from the dropdown (RDPS, HRDPS)
Then either write in coordinates or select them from a map
Enter date and time for Prometheus run

Script will grab the data and place them in a .csv file that prometheus can read.