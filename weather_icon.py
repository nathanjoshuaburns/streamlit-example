import random
from meteostat import Hourly, Stations
from datetime import datetime, date
import pandas as pd



#def gettempandhumid(long, lat, day):
#    point = Point(long, lat)
#    df = Hourly(point, day, day).fetch()
#    rhum = df.rhum[0]
#    temp = df.temp[0]
#    return {'humidity': rhum, 'temperature': temp}
#gettempandhumid(48.8567, 2.3522, datetime(2015,1,1,12,0,0))
def gettempandhumid(long, lat, day):
    stations = Stations()
    nearbystations = stations.nearby(long, lat).fetch(100)

    for nstation in nearbystations.wmo:
        try:

            df = Hourly(nstation, day, day).fetch()

            rhum = df.rhum[0]

        except Exception:

            continue
        break
    for nstation in nearbystations.wmo:
        try:

            df = Hourly(nstation, day, day).fetch()

            temp = df.temp[0]

        except Exception:

            continue
        break
    return {'humidity': rhum, 'temperature': temp}

def get_icon(coords, selectedDate) -> str:

    selectedDateAsDateTime = datetime.combine(selectedDate, datetime.min.time())

    tempdict = gettempandhumid(coords[0], coords[1], selectedDateAsDateTime)

    humidity = tempdict['humidity']
    temperature = tempdict['temperature']

    icon_name = "cloud" # Default to cloud
    if temperature >= 19 and humidity > 100:
        icon_name = "sun-o"
    elif temperature >= 19:
        icon_name = "sun-o"
    elif humidity > 80:
        icon_name = "tint"
    else:
        icon_name = "cloud"
    return icon_name