from app.engines.weather_engine import (
    WeatherEngine
)

from app.engines.weather_intelligence import (
    WeatherIntelligence
)

from app.services.cache_service import (
    get_cache,
    set_cache
)


def current_weather(
    farmer
):
    """
    Returns agricultural weather intelligence
    for current farmer location.
    """

    latitude = round(
        farmer.latitude,
        2
    )

    longitude = round(
        farmer.longitude,
        2
    )

    cache_key = (
        f"weather_current:"
        f"{latitude}:"
        f"{longitude}"
    )

    cached = get_cache(
        cache_key
    )

    if cached:
        return cached

    weather = (
        WeatherEngine
        .get_current_weather(
            latitude,
            longitude
        )
    )

    weather_intelligence = (
        WeatherIntelligence
        .analyze(
            weather
        )
    )

    set_cache(
        cache_key,
        weather_intelligence
    )

    return weather_intelligence


def get_current_weather(
    latitude,
    longitude
):

    return WeatherEngine.get_current_weather(
        latitude,
        longitude
    )


def forecast_weather(
    farmer
):
    """
    Returns 7-day weather forecast.
    """

    latitude = round(
        farmer.latitude,
        2
    )

    longitude = round(
        farmer.longitude,
        2
    )

    cache_key = (
        f"weather_forecast:"
        f"{latitude}:"
        f"{longitude}"
    )

    cached = get_cache(
        cache_key
    )

    if cached:
        return cached

    forecast = {

        "forecast":
            WeatherEngine
            .get_forecast(
                latitude,
                longitude
            )
    }

    set_cache(
        cache_key,
        forecast
    )

    return forecast


def weather_context(
    farmer
):
    """
    Unified weather context for Rule Engine.
    This is the function that future
    Advisory Engine and Rule Engine
    should call.
    """

    current = current_weather(
        farmer
    )

    forecast = forecast_weather(
        farmer
    )
    # derive whether rain is expected in the next 3 days
    forecast_list = forecast.get("forecast", [])

    rain_expected_next_3_days = any(
        (day.get("rainfall", 0) > 2) for day in forecast_list[:3]
    )

    return {
        "current_weather": current,
        "forecast": forecast_list,
        "rain_expected_next_3_days": rain_expected_next_3_days,
        "high_humidity": current.get("high_humidity", False),
        "high_temperature": current.get("high_temperature", False),
        "spraying_safe": current.get("spraying_safe", False),
        "irrigation_needed": current.get("irrigation_needed", False),
        "disease_risk_weather": current.get("disease_risk_weather", "UNKNOWN")
    }