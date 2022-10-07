import pandas as pd
import numpy as np

# Author: Jesus Lago

# License: AGPL-3.0 License


def _process_inputs_for_metrics(p_real, p_pred):
    """Function that checks that the two standard inputs of the metric functions satisfy some requirements


    Parameters
    ----------
    p_real : numpy.ndarray, pandas.DataFrame, pandas.Series
        Array/dataframe containing the real prices
    p_pred : numpy.ndarray, pandas.DataFrame, pandas.Series
        Array/dataframe containing the predicted prices

    Returns
    -------
    np.ndarray, np.ndarray
        The p_real and p_pred as numpy.ndarray objects after checking that they satisfy requirements

    """

    # Checking that both arrays are of the same type
    if type(p_real) != type(p_pred):
        raise TypeError('p_real and p_pred must be of the same type. p_real is of type {}'.format(type(p_real)) +
                        ' and p_pred of type {}'.format(type(p_pred)))

    # Checking that arrays are of the allowed types
    if type(p_real) != pd.DataFrame and \
            type(p_real) != pd.Series and \
            type(p_real) != np.ndarray:
        raise TypeError('p_real and p_pred must be either a pandas.DataFrame, a pandas.Serie, or ' +
                        ' a numpy.aray. They are of type {}'.format(type(p_real)))

    # Transforming dataset if it is a pandas.Series to pandas.DataFrame
    if type(p_real) == pd.Series:
        p_real = p_real.to_frame()
        p_pred = p_pred.to_frame()

    # Checking that both datasets share the same indices
    if type(p_real) == pd.DataFrame:
        if not (p_real.index == p_pred.index).all():
            raise ValueError('p_real and p_pred must have the same indices')

        # Extracting their values as numpy.ndarrays
        p_real = p_real.values.squeeze()
        p_pred = p_pred.values.squeeze()

    return p_real, p_pred


def MAE(p_real, p_pred):
    """Function that computes the mean absolute error (MAE) between two forecasts:
    """

    # Checking if inputs are compatible
    p_real, p_pred = _process_inputs_for_metrics(p_real, p_pred)

    return np.mean(np.abs(p_real - p_pred))


def sMAPE(p_real, p_pred):
    """Function that computes the symmetric mean absolute percentage error (sMAPE) between two forecasts
    """

    # Checking if inputs are compatible
    p_real, p_pred = _process_inputs_for_metrics(p_real, p_pred)

    return np.mean(np.abs(p_real - p_pred) / ((np.abs(p_real) + np.abs(p_pred)) / 2))