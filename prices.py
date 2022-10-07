import datetime
import random
from typing import List, Tuple

def get_prices(date: datetime.date) -> Tuple[List[float], List[float]]:
    # TODO
    # test data
    
    previous_day_prices = []
    forecast_prices = []

    # START OF GENERATE TEST DATA
    for i in range(24):
        next_forecast_price = random.uniform(10, 60)
        forecast_prices.append(next_forecast_price)

        next_previous_day_price = random.uniform(10, 60)
        previous_day_prices.append(next_previous_day_price)
    # END OF GENERATE TEST DATA

    return forecast_prices