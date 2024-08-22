import streamlit as st
import folium
from streamlit_folium import st_folium
import requests

# Create a map
m = folium.Map(location=[45.5236, -122.6750], zoom_start=13)

# Create a function to get the current location
def get_current_location():
    response = requests.get('https://api.opencagedata.com/geocode/v1/json',
                             params={'q': 'my current location', 'key': 'YOUR_OPEN_CAGE_GEOCODER_API_KEY'})
    data = response.json()
    return data['results'][0]['geometry']['lat'], data['results'][0]['geometry']['lng']

# Create a function to add a marker to the map
def add_marker_to_map(lat, lng):
    folium.Marker([lat, lng], popup='My Current Place').add_to(m)

# Create a button to show the current location
if st.button('My Current Place'):
    lat, lng = get_current_location()
    add_marker_to_map(lat, lng)

# Display the map
st_folium(m, width=800, height=600)
