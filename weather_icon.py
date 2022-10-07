import random
from meteostat import Point, Hourly
from datetime import datetime, date
import pandas as pd



#def gettempandhumid(long, lat, day):
#    point = Point(long, lat)
#    df = Hourly(point, day, day).fetch()
#    rhum = df.rhum[0]
#    temp = df.temp[0]
#    return {'humidity': rhum, 'temperature': temp}

#gettempandhumid(48.8567, 2.3522, datetime(2015,1,1,12,0,0))

def get_icon(coords, selectedDate) -> str:

    selectedDateAsDateTime = datetime.combine(selectedDate, datetime.min.time())

    point = Point(coords[0], coords[1])
    df = Hourly(point, selectedDateAsDateTime, selectedDateAsDateTime).fetch()

    if df.empty:
        return "cloud"
    else:
        humidity = df.rhum[0]
        temperature = df.temp[0]

        icon_name = "cloud" # Default to cloud

        if temperature >= 30 and humidity > 100:
            icon_name = "sun-o"
        elif temperature >= 50:
            icon_name = "fire"
        elif temperature >= 30:
            icon_name = "sun-o"
        elif humidity > 100:
            icon_name = "tint"
        else:
            icon_name = "cloud"

        return icon_name