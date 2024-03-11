import pandas as pd
import pandas_ta as ta

def ema_cross_up_rsi(data: pd.DataFrame) -> pd.Series:
    signal = (
        (data.rsi <= 35)
        & (ta.cross(data.fast, data.slow))
    )
    return signal
