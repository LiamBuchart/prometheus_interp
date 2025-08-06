# some nice mapping functions to call as needed
import streamlit_folium as st_folium
import streamlit as st


# return the lat lon coordinates of the clicked point
def get_pos(lat, lng):
    """
    Return the lat lon coords
    Call is from the last click value in map
    """
    print("Current position:", lat, lng)
    return lat, lng
