from collections import namedtuple
from random import sample
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import time, datetime, timedelta
import numpy as np
import plotly.graph_objects as go
from weather_icon import get_icon
from forecast_prices import get_forecast_prices
from previous_day_prices import get_previous_day_prices

st.set_page_config(
        page_title="Price forecasting",
)

col1, col2 =st.columns([2,2])

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
    label="Enter date:",
    value=datetime(2016, 7, 6),
    min_value=datetime(2016,1,1),
    max_value=datetime(2016,12,31)
    )

hour = ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
testPrices = [
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

with col1:
    st.subheader("Previous day prices")

    #previous_day_prices = get_previous_day_prices(selectedDate)
    previous_day_prices = []
    previousDayFig = go.Figure()
    previousDayFig.add_trace(go.Scatter(x=hour, y=previous_day_prices, name='Sample',
                            line=dict(color='firebrick', width=4)))

    previousDayFig.update_layout(title='Previous day',
                    xaxis_title='Hour',
                    yaxis_title='Price')

    st.plotly_chart(previousDayFig, use_container_width=True)

with col2:
    st.subheader("Forecast prices")

    # forecast_prices = get_forecast_prices(selectedDate)
    forecast_prices = []

    forecastFig = go.Figure()
    forecastFig.add_trace(go.Scatter(x=hour, y=forecast_prices, name='Sample',
                            line=dict(color='firebrick', width=4)))

    forecastFig.update_layout(title='Forecast price',
                    xaxis_title='Hour',
                    yaxis_title='Price')

    st.plotly_chart(forecastFig, use_container_width=True)

regionalCoords = [
    [48.14244663381307, -2.8732976551510263],
    [49.01203292123912, 0.15538061753084026],
    [49.97415434164336, 2.8261190286911333],
    [48.71212499407923, 2.5523685049282405],
    [47.439278433081036, 1.7071332414921612],
    [45.10197257034414, 0.09584511043028773],
    [43.58037639713084, 2.169507159438924],
    [43.83998471721191, 6.162653828372608],
    [45.40905180537371, 4.326744974917686],
    [47.12840752815982, 5.067991805604691],
    [48.76520936142879, 5.440004567794441]
]

# center on France
m = folium.Map(location=[46.6714327602744, 2.5419523299087947], zoom_start=6)

iconsDict = {}

for regionCoords in regionalCoords:
    # TODO get weather and calculate icon
    icon = get_icon(regionCoords)
    iconsDict[icon] = regionCoords

for key, value in iconsDict.items():
    folium.Marker(
        location=key,
        icon=folium.Icon(color='lightgray', icon=value, icon_color='white', prefix='fa')
    ).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 725)