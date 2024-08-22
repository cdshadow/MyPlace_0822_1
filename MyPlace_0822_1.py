import streamlit as st
import folium
from streamlit_folium import st_folium

# Initialize the map centered at a default location
m = folium.Map(location=[37.3382, 126.5924], zoom_start=12)

def app():
    st.title("My Current Place on Map")

    # Create a button
    if st.button("My Current Place"):
        # Get user's location using browser's geolocation API
        js_code = """
        navigator.geolocation.getCurrentPosition(
            (location) => {
                document.dispatchEvent(new CustomEvent("geolocation", {
                    detail: { lat: location.coords.latitude, lon: location.coords.longitude }
                }));
            },
            (error) => {
                console.error("Error getting location:", error);
                // Handle errors gracefully here (e.g., show a message to the user)
            }
        );
        """

        # Inject JavaScript code into the Streamlit app
        st.components.v1.html(f"<script>{js_code}</script>")

        # Wait for the "geolocation" event triggered by the JavaScript code
        data = st.experimental_get_query_params()
        if "geolocation" in data:
            lat, lon = map(float, data["geolocation"][0].split(","))

            # Add a circle marker at the user's location
            folium.CircleMarker(
                location=[lat, lon],
                radius=50,
                color="blue",
                fill=True,
                fill_color="blue",
            ).add_to(m)

    # Display the map in Streamlit
    st_folium(m, width=700, height=500)

if __name__ == "__main__":
    app()
