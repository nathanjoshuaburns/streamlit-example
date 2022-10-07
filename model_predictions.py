import os
from joblib import dump, load
from import_data import read_data
import numpy as np
import pandas as pd

day_ahead = '2016-12-01'

def make_predictions(day_ahead):
    dataset = 'data_with_weather'
    model = load(os.path.join('.', 'saved_models/model.joblib'))
    df_train, df_test = read_data(path=os.path.join('.', 'datasets'), dataset=dataset, years_test=None, begin_test_date=day_ahead, end_test_date=day_ahead)

    # Defining empty forecast array and the real values to be predicted in a more friendly format
    forecast = pd.DataFrame(index=df_test.index[::24], columns=['h' + str(k) for k in range(24)])
    real_values = df_test.loc[:, ['Price']].values.reshape(-1, 24)
    real_values = pd.DataFrame(real_values, index=forecast.index, columns=forecast.columns)

    forecast_dates = forecast.index

    # For loop over the recalibration dates
    for date in forecast_dates:
        # For simulation purposes, we assume that the available data is
        # the data up to current date where the prices of current date are not known
        data_available = pd.concat([df_train, df_test.loc[:date + pd.Timedelta(hours=23), :]], axis=0)

        # We set the real prices for current date to NaN in the dataframe of available data
        data_available.loc[date:date + pd.Timedelta(hours=23), 'Price'] = np.NaN

        # Recalibrating the model with the most up-to-date available data and making a prediction
        # for the next day
        Yp = model.recalibrate_and_forecast_next_day(df=data_available, next_day_date=date, recalibrate=False)
        # Saving the current prediction
        forecast.loc[date, :] = Yp

    last_day_historic = df_train['Price'].loc[date-pd.Timedelta(hours=24):]

    return forecast.to_numpy().reshape((-1,)), last_day_historic.to_numpy()

forecast, last_day_historic = make_predictions(day_ahead = day_ahead)

a = 1