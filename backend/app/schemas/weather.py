from pydantic import BaseModel


class CurrentWeatherResponse(
    BaseModel
):

    temperature: float

    humidity: float

    rainfall: float

    wind_speed: float

    weather_code: int


class ForecastDay(
    BaseModel
):

    date: str

    temp_max: float

    temp_min: float

    rainfall: float

    humidity: float

    wind_speed: float


class ForecastResponse(
    BaseModel
):

    forecast: list[ForecastDay]


class WeatherIntelligenceResponse(
    BaseModel
):

    current_weather: CurrentWeatherResponse

    forecast: list[ForecastDay]

    rain_expected_next_3_days: bool

    high_humidity: bool

    high_temperature: bool

    spraying_safe: bool

    irrigation_needed: bool

    disease_risk_weather: str