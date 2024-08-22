import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import st_folium

# Initialize Nominatim API
geolocator = Nominatim(user_agent="geoapiExercises")

# Streamlit App
st.title("My Current Place on Map")

# Button to get the current location
if st.button('My Current Place'):
    # Get current place (dummy coordinates, replace with actual method to get user's location)
    # In real scenario, you would get this from user's browser or device GPS
    location = geolocator.geocode("Your Current Address or City")
    
    if location:
        lat, lon = location.latitude, location.longitude
        st.success(f"Found your location: {location.address}")
        
        # Create a folium map centered at the location
        m = folium.Map(location=[lat, lon], zoom_start=15)
        
        # Add a circle marker to the map
        folium.CircleMarker(
            location=[lat, lon],
            radius=10,
            popup="Your Current Place",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc"
        ).add_to(m)
        
        # Display the map in Streamlit
        st_folium(m, width=700, height=500)
    else:
        st.error("Could not determine your location.")
else:
    st.write("Click the button to show your current place on the map.")

# To deploy this on Streamlit, save this code in a file named `app.py` and run:
# streamlit run app.py
