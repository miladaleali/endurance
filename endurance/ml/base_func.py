import pandas as pd
from typing import Callable

def create_signal(
    data: pd.DataFrame,
    signal_func: Callable
) -> pd.DataFrame:
    data['signal'] = signal_func(data)
    return data
