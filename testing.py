import os
from import_data import read_data
import pandas as pd
import model
import numpy as np
from matplotlib import pyplot as plt
import evaluation
from joblib import dump, load
from time_series_checks import time_series_analysis


calibration_window = 364*3# 3 years (in days)
dataset = 'FR'

# IF YEARS_TEST, REMOVE DAY_DAHEAD
day_ahead = None # '2016-12-01'
years_test = 1 #30/364
use_trained_model = False
recalibrate = False

if use_trained_model:
    model = load(os.path.join('.', 'saved_models/model.joblib'))
else:
    model = model.LEAR(calibration_window=calibration_window)

df_train, df_test = read_data(path=os.path.join('.','datasets'), dataset=dataset, years_test=years_test, begin_test_date=day_ahead, end_test_date=day_ahead)

# time_series_analysis(df_train['Price'].to_numpy())

# Defining unique name to save the forecast
forecast_file_name = 'LEAR_forecast' + '_dat' + str(dataset) + '_YT' + str(years_test) + \
                     '_CW' + str(calibration_window) + '.csv'

forecast_file_path = os.path.join('.', forecast_file_name)

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
    Yp = model.recalibrate_and_forecast_next_day(df=data_available, next_day_date=date, recalibrate=recalibrate)
    # Saving the current prediction
    forecast.loc[date, :] = Yp

    # Computing metrics up-to-current-date
    mae = np.mean(evaluation.MAE(forecast.loc[:date].values.squeeze(), real_values.loc[:date].values))
    smape = np.mean(evaluation.sMAPE(forecast.loc[:date].values.squeeze(), real_values.loc[:date].values)) * 100

    # Pringint information
    print('{} - sMAPE: {:.2f}%  |  MAE: {:.3f}'.format(str(date)[:10], smape, mae))

    # Saving forecast
    forecast.to_csv(forecast_file_path)

# Visualise forecasts
plt.figure()
plt.plot(forecast.to_numpy().flatten(), 'r')
plt.plot(real_values.to_numpy().flatten(), 'k')
plt.show()

print('Saving model..')
dump(model, os.path.join('.', 'saved_models/model.joblib'))



