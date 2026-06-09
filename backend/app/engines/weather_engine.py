import requests
import requests_cache
from retry_requests import retry
import logging
from dotenv import load_dotenv
import os

load_dotenv()

logger = logging.getLogger(__name__)

cache_session = requests_cache.CachedSession(
    '.cache', 
    expire_after=3600,
    stale_if_error=True
)

retry_session = retry(
    cache_session, 
    retries=2,
    backoff_factor=0.3
)

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

class WeatherEngine:

    BASE_URL = "https://api.openweathermap.org/data/2.5"
    
    @staticmethod
    def get_current_weather(
        latitude: float,
        longitude: float
    ):

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric"
        }

        try:
            response = retry_session.get(
                f"{WeatherEngine.BASE_URL}/weather",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "rainfall": data.get("rain", {}).get("1h", 0),
                "wind_speed": data["wind"]["speed"],
                "weather_code": data["weather"][0]["id"]
            }
        except Exception as e:
            logger.error(
                f"Weather API error for ({latitude}, {longitude}): {str(e)}"
            )
            return {
                "temperature": 0,
                "humidity": 0,
                "rainfall": 0,
                "wind_speed": 0,
                "weather_code": 0,
                "error": "Weather service unavailable"
            }

    @staticmethod
    def get_forecast(
        latitude: float,
        longitude: float
    ):

        params = {
            "lat": latitude,
            "lon": longitude,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "cnt": 40
        }

        try:
            response = retry_session.get(
                f"{WeatherEngine.BASE_URL}/forecast",
                params=params,
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            forecast = []
            processed_dates = set()

            for item in data["list"]:
                date_str = item["dt_txt"].split(" ")[0]
                
                if date_str not in processed_dates and len(forecast) < 7:
                    processed_dates.add(date_str)
                    forecast.append({
                        "date": date_str,
                        "temp_max": item["main"]["temp_max"],
                        "temp_min": item["main"]["temp_min"],
                        "rainfall": item.get("rain", {}).get("3h", 0),
                        "humidity": item["main"]["humidity"],
                        "wind_speed": item["wind"]["speed"]
                    })

            return forecast
        except Exception as e:
            logger.error(
                f"Forecast API error for ({latitude}, {longitude}): {str(e)}"
            )
            return []


    @staticmethod
    def get_agri_weather(
        latitude: float,
        longitude: float
    ):

        current = (
            WeatherEngine
            .get_current_weather(
                latitude,
                longitude
            )
        )

        forecast = (
            WeatherEngine
            .get_forecast(
                latitude,
                longitude
            )
        )

        rainfall_next_3_days = sum(
            day["rainfall"]
            for day in forecast[:3]
        )

        humidity_high = (
            current["humidity"] >= 85
        )

        rain_expected = (
            rainfall_next_3_days >= 5
        )

        high_temperature = (
            current["temperature"] >= 35
        )

        spraying_safe = (
            current["wind_speed"] < 25
            and current["rainfall"] < 1
        )

        irrigation_needed = (
            rainfall_next_3_days < 5
            and current["humidity"] < 70
        )

        disease_risk = "LOW"

        if (
            rain_expected
            and humidity_high
        ):
            disease_risk = "HIGH"

        elif (
            current["humidity"] >= 80
        ):
            disease_risk = "MEDIUM"

        return {

            "current_weather":
                current,

            "forecast":
                forecast,

            "rain_expected_next_3_days":
                rain_expected,

            "high_humidity":
                humidity_high,

            "high_temperature":
                high_temperature,

            "spraying_safe":
                spraying_safe,

            "irrigation_needed":
                irrigation_needed,

            "disease_risk_weather":
                disease_risk
        }