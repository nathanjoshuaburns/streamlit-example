import pandas as pd
import os


def read_data(path, dataset='PJM', years_test=2, begin_test_date=None, end_test_date=None):
    """Function to read and import data from day-ahead electricity markets. """

    # Checking if provided directory exist and if not create it
    if not os.path.exists(path):
        os.makedirs(path)

    # If dataset is one of the existing open-access ones,
    # they are imported if they exist locally or download from
    # the repository if they do not
    if dataset in ['PJM', 'NP', 'FR', 'BE', 'DE']:
        file_path = os.path.join(path, dataset + '.csv')

        # The first time this function is called, the datasets
        # are downloaded and saved in a local folder
        # After the first called they are imported from the local
        # folder
        if os.path.exists(file_path):
            data = pd.read_csv(file_path, index_col=0)
        else:
            url_dir = 'https://sandbox.zenodo.org/api/files/fb5bae17-de91-4ce7-b348-0d62e52824b5/'
            data = pd.read_csv(url_dir + dataset + '.csv', index_col=0)
            data.to_csv(file_path)
    else:
        try:
            file_path = os.path.join(path, dataset + '.csv')
            data = pd.read_csv(file_path, index_col=0)
        except IOError as e:
            raise IOError("%s: %s" % (path, e.strerror))

    data.index = pd.to_datetime(data.index)

    columns = ['Price']
    n_exogeneous_inputs = len(data.columns) - 1

    for n_ex in range(1, n_exogeneous_inputs + 1):
        columns.append('Exogenous ' + str(n_ex))

    data.columns = columns

    # The training and test datasets can be defined by providing a number of years for testing
    # or by providing the init and end date of the test period
    if begin_test_date is None and end_test_date is None:
        number_datapoints = len(data.index)
        number_training_datapoints = round(number_datapoints - 24 * 364 * years_test)

        # We consider that a year is 52 weeks (364 days) instead of the traditional 365
        df_train = data.loc[:data.index[0] + pd.Timedelta(hours=number_training_datapoints - 1), :]
        df_test = data.loc[data.index[0] + pd.Timedelta(hours=number_training_datapoints):, :]

    else:
        try:
            begin_test_date = pd.to_datetime(begin_test_date, dayfirst=True)
            end_test_date = pd.to_datetime(end_test_date, dayfirst=True)
        except ValueError:
            print("Provided values for dates are not valid")

        if begin_test_date.hour != 0:
            raise Exception("Starting date for test dataset should be midnight")
        if end_test_date.hour != 23:
            if end_test_date.hour == 0:
                end_test_date = end_test_date + pd.Timedelta(hours=23)
            else:
                raise Exception("End date for test dataset should be at 0h or 23h")

        print('Test datasets: {} - {}'.format(begin_test_date, end_test_date))
        df_train = data.loc[:begin_test_date - pd.Timedelta(hours=1), :]
        df_test = data.loc[begin_test_date:end_test_date, :]

    return df_train, df_test