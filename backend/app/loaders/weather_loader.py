import pandas as pd

from pathlib import Path
from functools import lru_cache


BASE_DIR = Path(__file__).resolve().parent.parent

WEATHER_PATH = (
    BASE_DIR
    / "knowledge_base"
    / "weather"
    / "weather.csv"
)


@lru_cache(maxsize=1)
def load_weather_data():

    return pd.read_csv(
        WEATHER_PATH
    )