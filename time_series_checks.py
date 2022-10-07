from statsmodels.tsa.stattools import adfuller
from matplotlib import pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

def adfuller(series):

    result = adfuller(series)

    print('ADF Statistic: %f' % result[0])
    print('p-value: %f' % result[1])
    print('Critical Values:')
    for key, value in result[4].items():
        print('\t%s: %.3f' % (key, value))

    if (result[1] <= 0.05) & (result[4]['5%'] > result[0]):
        print("\u001b[32mStationary\u001b[0m")
    else:
        print("\x1b[31mNon-stationary\x1b[0m")

def autocorrelations(series):
    f, ax = plt.subplots(nrows=2, ncols=1, figsize=(2, 2*2))
    plot_acf(series, ax=ax[0])
    plot_pacf(series, ax=ax[1], method='ols')

    plt.tight_layout()
    plt.show()

def time_series_analysis(series):
    # adfuller(series)
    autocorrelations(series)