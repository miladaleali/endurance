import pandas as pd

from finrl import config
from finrl.meta.preprocessor.preprocessors import FeatureEngineer, data_split

TIMEFRAMES = [
    '1m',
    '5m',
    '10m',
    '15m',
    '30m',
    '45m',
    '1h',
    '2h',
    '4h',
    '6h',
    '12h',
    '1d',
    '1w',
    '1M',
    '1y',
]

def fetch_ohlcv_data(
    start_date: str,
    end_date: str,
    ticker_list: list[str],
    data_source: str,
    time_interval: str,
) -> pd.DataFrame:
    pass

def add_indicators(
    data: pd.DataFrame,
    indicators_list: list[str],
) -> pd.DataFrame:
    pass

def preprocess_data(
    data: pd.DataFrame,
    indicators_list: list[str],
) -> pd.DataFrame:
    pass

def preprocess_data_finrl(
    data: pd.DataFrame,
    indicators_list: list[str] = None,
    **kwargs
) -> pd.DataFrame:
    fe = FeatureEngineer(
        use_technical_indicator=True,
        tech_indicator_list=indicators_list or config.INDICATORS,
        use_vix=False,
        user_defined_feature=False,
        use_turbulence=kwargs.get('use_turbulence', True)
    )
    return fe.preprocess_data(data)

def train_test_split_data(
    processed_data: pd.DataFrame,
    train_start_date: str,
    test_start_date: str,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    train = data_split(processed_data, train_start_date, test_start_date)
    test = data_split(processed_data, test_start_date, processed_data.date.iloc[-1])
    return (train, test)
