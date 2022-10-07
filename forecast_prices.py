import datetime
import random
from typing import List

def get_forecast_prices(date: datetime.date) -> List[float]:
    # TODO
    
    forecast_prices = []

    # START OF GENERATE TEST DATA
    for i in range(24):
        next_forecast_price = random.uniform(10, 60)
        forecast_prices.append(next_forecast_price)
    # END OF GENERATE TEST DATA

    return forecast_prices