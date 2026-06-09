from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.auth import (
    get_current_farmer
)

from app.schemas.weather import (
    CurrentWeatherResponse,
    ForecastResponse,
    WeatherIntelligenceResponse
)

from app.services.weather_service import (
    current_weather,
    forecast_weather,
    weather_context
)

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)
@router.get(
    "/current",
    response_model=CurrentWeatherResponse
)
def get_current_weather(
    current_farmer=Depends(
        get_current_farmer
    )
):

    weather = current_weather(
        current_farmer
    )
    return weather

@router.get(
    "/forecast",
    response_model=ForecastResponse
)
def get_forecast(
    current_farmer=Depends(
        get_current_farmer
    )
):

    return {

        "forecast":
            forecast_weather(
                current_farmer
            )["forecast"]
    }

@router.get(
    "/agri-context",
    response_model=
    WeatherIntelligenceResponse
)
def agricultural_weather(
    current_farmer=Depends(
        get_current_farmer
    )
):

    return weather_context(
        current_farmer
    )