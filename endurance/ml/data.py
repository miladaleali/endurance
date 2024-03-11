import pandas_ta as ta
import pandas as pd

def prepare_data(
    data: pd.DataFrame,
    indicators: list[dict],
) -> pd.DataFrame:
    indis = ta.Strategy(
        name='custom_indicators',
        ta=indicators
    )
    data.ta.strategy(indis)
    return data
