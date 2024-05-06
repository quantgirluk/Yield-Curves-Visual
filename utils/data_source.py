import pandas as pd
import pandas_datareader as pdr


def retrieve_us_yield_curve_data():
    start = '1990-01-01'
    tickers = ['GS30', 'GS10', 'GS5', 'GS3', 'GS2', 'GS1', 'GS6m', 'GS3m', 'GS1m']
    df = pdr.get_data_fred(tickers, start)
    df.columns = ['30-year', '10-year', '5-year', '3-year', '2-year', '1-year', '6-month', '3-month', '1-month']
    # df.columns = [30, 10, 5, 3, 2, 1, 0.5, 0.25, 0.083]
    df.index = df.index + pd.offsets.MonthEnd(0)
    df.to_csv('../data/data_fed_yc.csv', header=True, index=True)

    return df


def get_us_yield_curve_data():
    # start = '1990-01-01'
    # tickers = ['GS30', 'GS10', 'GS5', 'GS3', 'GS2', 'GS1', 'GS6m', 'GS3m', 'GS1m']
    # df = pdr.get_data_fred(tickers, start)
    # df.columns = ['30-year', '10-year', '5-year', '3-year', '2-year', '1-year', '6-month', '3-month', '1-month']
    # # Changing format from 1st day of the month to last day of the month
    # df.index = df.index + pd.offsets.MonthEnd(0)

    df = pd.read_csv('data/data_fed_yc.csv', index_col=0)
    df.index = pd.to_datetime(df.index)

    return df


def get_uk_yield_curve_data():
    df = pd.read_csv('data/data_boe_yc.csv', index_col=0)
    df.index = pd.to_datetime(df.index)

    return df

# retrieve_us_yield_curve_data()
