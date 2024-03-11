import pandas_ta as ta
import pandas as pd

# Implement all functions that needed in lab.
def convert_resample_timeframe(timeframe: str) -> str:
    c = timeframe[:-1]
    t = timeframe[-1]
    if t == 'm':
        t = "T"
    else:
        t = t.upper()
    tmp = f"{c}{t}"
    return tmp

def resample_data(
    base_data: pd.DataFrame,
    resample_timeframe: str,
) -> pd.DataFrame:
    resample_tm = convert_resample_timeframe(resample_timeframe)
    dfr = base_data.resample(resample_tm).agg(
        {
            'open': 'first',
            'high': 'max',
            'low': 'min',
            'close': 'last',
            'volume': 'sum'
        }
    ).reset_index()
    dfr.set_index('timestamp', drop=True, inplace=True)
    return dfr.iloc[:-1]

def add_indicators(
    data: pd.DataFrame,
    indicators: list[dict],
) -> pd.DataFrame:
    indis = ta.Strategy(
        name='custom_indicators',
        ta=indicators
    )
    data.ta.strategy(indis)
    return data

def preprocess_data(
    data: pd.DataFrame,
    scaler: ...,
) -> pd.DataFrame:
    scaled_data = scaler.fit(data)
    return scaled_data
