from typing import Union

import pandas as pd
from pandas.core.frame import DataFrame
import plotly.graph_objects as go


def show_candlesticks(data: DataFrame) -> None:
    """
    Showing data to monitor through plotly lib
    """
    fig = go.Figure(data=[go.Candlestick(x=data.index,
                                         open=data['Open'], high=data['High'],
                                         low=data['Low'], close=data['Close']),
                          go.Scatter(x=data.index, y=data.MA, line=dict(color='orange', width=1))
                          ])

    fig.show()


def main(path: str, timerange: str, ema: Union[int, float]) -> DataFrame:
    """
    Makes candlesticks dataframe and EMA
    """
    df = pd.read_csv(path, index_col='TS')

    df.index = pd.to_datetime(df.index, format='%Y-%m-%d %H:%M:%S.%f')
    candle_summary = pd.DataFrame()
    candle_summary['Open'] = df.PRICE.resample(timerange).first()
    candle_summary['High'] = df.PRICE.resample(timerange).max()
    candle_summary['Low'] = df.PRICE.resample(timerange).min()
    candle_summary['Close'] = df.PRICE.resample(timerange).last()
    candle_summary['Mean'] = df.PRICE.resample(timerange).mean()
    candle_summary['MA'] = candle_summary['Mean'].ewm(span=ema, adjust=False).mean()

    return candle_summary


if __name__ == '__main__':
    path = r'prices.csv/prices.csv'
    try:
        timerange, ema = input('enter time range and EMA (for example: 3T 14): ').split()
    except ValueError:
        print('provide exactly 2 arguments. Example: 3T 14')
    else:
        if ema.replace('.', '', 1).isdigit():
            data = main(path, timerange, float(ema))
            show_candlesticks(data)
        else:
            print('EMA must be a number')
