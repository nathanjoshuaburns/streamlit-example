import datetime
import random
from typing import List

def get_previous_day_prices(date: datetime.date) -> List[float]:
    # TODO

    previous_day_prices = []

    # START OF GENERATE TEST DATA
    for i in range(24):
        next_previous_day_price = random.uniform(10, 60)
        previous_day_prices.append(next_previous_day_price)
    # END OF GENERATE TEST DATA

    return previous_day_prices

def get_forecast_prices(date: datetime.date) -> List[float]:
    # TODO
    
    forecast_prices = []

    # START OF GENERATE TEST DATA
    for i in range(24):
        next_forecast_price = random.uniform(10, 60)
        forecast_prices.append(next_forecast_price)
    # END OF GENERATE TEST DATA

    return forecast_prices