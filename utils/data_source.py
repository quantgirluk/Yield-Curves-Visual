from datetime import datetime

import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader as pdr


def get_us_yield_curve_data():
    # start = '1980-01-01'
    start = '1990-01-01'
    tickers = ['GS30', 'GS10', 'GS5', 'GS3', 'GS2', 'GS1', 'GS6m', 'GS3m', 'GS1m']
    df = pdr.get_data_fred(tickers, start)
    df.columns = ['30Y', '10Y', '5Y', '3Y', '2Y', '1Y', '6M', '3M', '1M']
    # Changing format from 1st day of the month to last day of the month
    df.index = df.index + pd.offsets.MonthEnd(0)
    as_of_date = df.index[-1]

    return df


def get_uk_yield_curve_data():
    recent = pd.read_excel("data/glcnominalmonthedata/GLC Nominal month end data_2016 to present.xlsx",
                           sheet_name="4. spot curve", skiprows=[0, 1, 2, 4], parse_dates=True, index_col=0)
    older = pd.read_excel("data/glcnominalmonthedata/GLC Nominal month end data_1970 to 2015.xlsx",
                          sheet_name="4. spot curve",
                          skiprows=[0, 1, 2, 4], parse_dates=True, index_col=0)

    df = pd.concat([older, recent])
    df = df[df.index >= datetime(1990, 1, 1)]
    # df = df.iloc[::-1]  # to reverse order of rows in a df
    df = df[df.columns[::-1]]
    df.columns = ['40Y', '39.5Y', '39Y', '38.5Y', '38Y', '37.5Y', '37Y', '36.5Y',
     '36Y', '35.5Y', '35Y', '34.5Y', '34Y', '33.5Y', '33Y', '32.5Y',
     '32Y', '31.5Y', '31Y', '30.5Y', '30Y', '29.5Y', '29Y', '28.5Y',
     '28Y', '27.5Y', '27Y', '26.5Y', '26Y', '25.5Y', '25Y', '24.5Y',
     '24Y', '23.5Y', '23Y', '22.5Y', '22Y', '21.5Y', '21Y', '20.5Y',
     '20Y', '19.5Y', '19Y', '18.5Y', '18Y', '17.5Y', '17Y', '16.5Y',
     '16Y', '15.5Y', '15Y', '14.5Y', '14Y', '13.5Y', '13Y', '12.5Y',
     '12Y', '11.5Y', '11Y', '10.5Y', '10Y', '9.5Y', '9Y', '8.5Y',
     '8Y', '7.5Y', '7Y', '6.5Y', '6Y', '5.5Y', '5Y', '4.5Y', '4Y',
     '3.5Y', '3Y', '2.5Y', '2Y', '1.5Y', '1Y', '0.5Y']
    return df
