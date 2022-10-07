from collections import namedtuple
from random import sample
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import time, datetime, timedelta
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
        page_title="Price forecasting",
)

from streamlit_folium import st_folium
import folium


"""
# Welcome to our Electricity Price Forecaster!

This tool predicts prices using previous price data and weather data

"""

#
#timeOfDay = st.slider(
#    label="Time of day:",
#    min_value=time(0, 0),
#    max_value=time(23, 0),
#    value=time(12, 0),
#    step=timedelta(minutes=60))

selectedDate = st.date_input(
    "Enter date:",
    datetime(2016, 7, 6))

hour = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
samplePrices = [
32.542,
21.549,
15.711,
10.583,
10.324,
10.325,
9.223,
10.002,
10.191,
30,
46.022,
50.835,
53.024,
46.616,
43.441,
36.36,
39.222,
56.276,
63.02,
62.379,
57.473,
49.373,
52.013,
47.004]

forecastFig = go.Figure()
forecastFig.add_trace(go.Scatter(x=hour, y=samplePrices, name='Sample',
                         line=dict(color='firebrick', width=4)))

forecastFig.update_layout(title='Forecast price',
                   xaxis_title='Hour',
                   yaxis_title='Price')

st.plotly_chart(forecastFig, use_container_width=True)

previousDayFig = go.Figure()
previousDayFig.add_trace(go.Scatter(x=hour, y=samplePrices, name='Sample',
                         line=dict(color='firebrick', width=4)))

previousDayFig.update_layout(title='Previous day',
                   xaxis_title='Hour',
                   yaxis_title='Price')

st.plotly_chart(previousDayFig, use_container_width=True)

# center on Liberty Bell, add marker
m = folium.Map(location=[46.6714327602744, 2.5419523299087947], zoom_start=6)
folium.Marker(
    location=[46.6714327602744, 2.5419523299087947], 
    popup="France", 
    tooltip="France"
).add_to(m)

folium.Marker(
    location=[46.6714327602744, 2.5419523299087947],
    icon=folium.Icon(color='lightgray', icon='cloud', prefix='fa')
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)