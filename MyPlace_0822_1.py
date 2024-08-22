import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# Create a map
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Create a function to get the current location
def get_current_location():
    if st.button('My Current Place'):
        try:
            response = requests.get('https://ipapi.co/json/')
            data = response.json()
            return data['latitude'], data['longitude']
        except:
            return None, None

# Create a function to add a marker to the map
def add_marker_to_map(lat, lng):
    folium.Marker([lat, lng], popup='My Current Place').add_to(m)

# Get the current location
lat, lng = get_current_location()

# Add a marker to the map
if lat is not None and lng is not None:
    add_marker_to_map(lat, lng)

# Display the map
st_folium(m, width=800, height=600)
