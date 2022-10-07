from collections import namedtuple
from random import sample
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import time, datetime, timedelta

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
    value=time(12, 0),
    step=timedelta(minutes=60))

sampleData = {
    "0":32.542,
"1":21.549,
"2":15.711,
"3":10.583,
"4":10.324,
"5":10.325,
"6":9.223,
"7":10.002,
"8":10.191,
"9":30,
"10":46.022,
"11":50.835,
"12":53.024,
"13":46.616,
"14":43.441,
"15":36.36,
"16":39.222,
"17":56.276,
"18":63.02,
"19":62.379,
"20":57.473,
"21":49.373,
"22":52.013,
"23":47.004}

df = pd.DataFrame(sampleData)

st.line_chart(
    data=df,
    x="Hours",
    y="Price")

# center on Liberty Bell, add marker
m = folium.Map(location=[46.6714327602744, 2.5419523299087947], zoom_start=6)
folium.Marker(
    [46.6714327602744, 2.5419523299087947], 
    popup="France", 
    tooltip="France"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)