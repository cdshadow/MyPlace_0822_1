import streamlit as st
import folium
from streamlit_folium import st_folium

# Initialize the map centered at a default location (you can change it later)
m = folium.Map(location=[37.3382, 126.5924], zoom_start=12)

# Define the Streamlit app
def app():
    st.title("My Current Place on Map")

    # Create a button
    if st.button("My Current Place"):
        # Simulate getting user's location (replace with actual geolocation logic)
        user_lat, user_lon = 37.3382, 126.5924  # Replace with actual geolocation

        # Add a circle marker at the user's location
        folium.CircleMarker(
            location=[user_lat, user_lon],
            radius=50,  # Adjust the radius as needed
            color="blue",
            fill=True,
            fill_color="blue",
        ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)

# Run the app
if __name__ == "__main__":
    app()
