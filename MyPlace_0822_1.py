import streamlit as st
import folium
from streamlit_folium import st_folium

# Streamlit App
st.title("My Current Place on Map")

# JavaScript to get user's current location
st.markdown(
    """
    <script>
    function getLocation() {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const latitude = position.coords.latitude;
                const longitude = position.coords.longitude;
                document.getElementById("lat").value = latitude;
                document.getElementById("lon").value = longitude;
                document.getElementById("location-form").submit();
            }
        );
    }
    </script>
    """,
    unsafe_allow_html=True,
)

# Form to trigger the location function and hold the latitude and longitude
st.markdown(
    """
    <form id="location-form" action="" method="POST">
        <input type="hidden" id="lat" name="lat">
        <input type="hidden" id="lon" name="lon">
        <input type="button" value="My Current Place" onclick="getLocation()">
    </form>
    """,
    unsafe_allow_html=True,
)

# Get the latitude and longitude from the form submission
lat = st.experimental_get_query_params().get("lat", [None])[0]
lon = st.experimental_get_query_params().get("lon", [None])[0]

if lat and lon:
    lat = float(lat)
    lon = float(lon)
    st.success(f"Found your location: Latitude: {lat}, Longitude: {lon}")

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
    st.write("Click the button to show your current place on the map.")
