from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import time

st.set_page_config(
        page_title="Price forecasting",
)

from streamlit_folium import st_folium
import folium


"""
# Welcome to our Electricity Price Forecaster!

This tool predicts prices using previous price data and weather data

"""


timeOfDay = st.slider(
    label="Time of day:",
    min_value=time(0, 0),
    max_value=time(23, 0),
    value=time(12, 0))

# center on Liberty Bell, add marker
m = folium.Map(location=[46.6714327602744, 2.5419523299087947], zoom_start=6)
folium.Marker(
    [46.6714327602744, 2.5419523299087947], 
    popup="France", 
    tooltip="France"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)