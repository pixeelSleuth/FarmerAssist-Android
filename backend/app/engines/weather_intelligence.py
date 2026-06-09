class WeatherIntelligence:

    @staticmethod
    def analyze(
        weather
    ):

        temperature = weather["temperature"]

        humidity = weather["humidity"]

        rainfall = weather["rainfall"]

        wind_speed = weather["wind_speed"]

        rain_expected = rainfall > 2

        high_humidity = humidity >= 85

        high_temperature = temperature >= 35

        spraying_safe = (
            wind_speed < 25
            and rainfall < 1
        )

        irrigation_needed = (
            rainfall < 2
            and humidity < 70
        )

        disease_risk = "LOW"

        if (
            rainfall > 5
            and humidity > 85
        ):
            disease_risk = "HIGH"

        elif humidity > 80:
            disease_risk = "MEDIUM"

        return {

            "temperature":
                temperature,

            "humidity":
                humidity,

            "rainfall":
                rainfall,

            "wind_speed":
                wind_speed,

            "weather_code":
                weather["weather_code"],

            "rain_expected_next_24h":
                rain_expected,

            "high_humidity":
                high_humidity,

            "high_temperature":
                high_temperature,

            "spraying_safe":
                spraying_safe,

            "irrigation_needed":
                irrigation_needed,

            "disease_risk_weather":
                disease_risk
        }