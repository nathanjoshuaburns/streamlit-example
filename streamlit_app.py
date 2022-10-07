from collections import namedtuple
from random import sample
import altair as alt
import math
import pandas as pd
import streamlit as st
from datetime import time, datetime, timedelta
import numpy as np
import plotly.graph_objects as go
from map import render_map
from model_predictions import make_predictions
import requests

st.set_page_config(
        page_title="Price forecasting",
        layout="wide"
)

featureOne = requests.get("https://corporatebs-generator.sameerkumar.website/")
featureTwo = requests.get("https://corporatebs-generator.sameerkumar.website/")
featureThree = requests.get("https://corporatebs-generator.sameerkumar.website/")

"""
# Welcome to our Electricity Price Forecaster!

This tool predicts prices using previous price data and weather data.

Key features include:

"""

st.write("- " + featureOne.json()['phrase'])
st.write("- " + featureTwo.json()['phrase'])
st.write("- " + featureThree.json()['phrase'])

selectedDate = st.date_input(
    label="Choose a date:",
    value=datetime(2016, 7, 6),
    min_value=datetime(2016,1,1),
    max_value=datetime(2016,12,31)
    )

col1, col2 = st.columns([2,2])

#
#timeOfDay = st.slider(
#    label="Time of day:",
#    min_value=time(0, 0),
#    max_value=time(23, 0),
#    value=time(12, 0),
#    step=timedelta(minutes=60))

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

forecast_prices, previous_day_prices = make_predictions(selectedDate)
max_forecast = max(forecast_prices)
max_previous = max(forecast_prices)
max_value = max(max_forecast, max_previous)

previous_day = selectedDate - timedelta(days=1)

with col1:
    st.subheader("Previous day prices for " + previous_day.strftime("%d/%m/%Y"))

    # previous_day_prices = get_previous_day_prices(selectedDate)
    previousDayFig = go.Figure()
    previousDayFig.add_trace(go.Scatter(x=hour, y=previous_day_prices, name='Sample',
                            line=dict(color='lightgreen', width=4)))

    previousDayFig.update_layout(title='',
                    xaxis_title='Hour',
                    yaxis_title='Price',
                    yaxis_range=(0, max_value))

    st.plotly_chart(previousDayFig, use_container_width=True)

with col2:
    st.subheader("Forecast prices for " + selectedDate.strftime("%d/%m/%Y"))

    # forecast_prices = get_forecast_prices(selectedDate)

    forecastFig = go.Figure()
    forecastFig.add_trace(go.Scatter(x=hour, y=forecast_prices, name='Sample',
                            line=dict(color='dodgerblue', width=4, dash='dash')))

    forecastFig.update_layout(title='',
                    xaxis_title='Hour',
                    yaxis_title='Price',
                    yaxis_range=(0, max_value))

    st.plotly_chart(forecastFig, use_container_width=True)

mapBufferLeft, mapColumn, mapBufferRight = st.columns([2,6,2])
with mapBufferLeft:
    st.write("")

with mapColumn:
    st.subheader("Weather for " + previous_day.strftime("%d/%m/%Y"))
    render_map(selectedDate)

with mapBufferRight:
    st.write("")