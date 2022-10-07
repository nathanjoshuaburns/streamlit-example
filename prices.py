import datetime
import random
from typing import List

def get_prices(date: datetime.date) -> List[float]:
    # TODO
    # test data

    test_prices = []

    for i in range(24):
        next_test_price = random.uniform(10, 60)
        test_prices.append(next_test_price)

    return test_prices