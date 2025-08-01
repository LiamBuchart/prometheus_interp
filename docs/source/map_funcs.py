# some nice mapping functions to call as needed
import streamlit_folium as st_folium
import streamlit as st

# return the lat lon coordinates of the clicked point
def get_coordinates():
    """
    Function to get the coordinates of a clicked point on the map.
    """
    coords = st_folium(m, width=700, height=500)
    if coords:
        lat = coords['last_active_drawing']['lat']
        lon = coords['last_active_drawing']['lng']
        st.write(f"Coordinates: {lat}, {lon}")
        return lat, lon
    else:
        st.write("Click on the map to get coordinates.")
        return None, None
    

# get the coordinates of the clicked point
lat, lon = get_coordinates()
print(f"Clicked coordinates: Latitude = {lat}, Longitude = {lon}")