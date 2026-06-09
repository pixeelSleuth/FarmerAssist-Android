from app.context_builder.calculators import ContextCalculators


class ContextBuilder:

    @staticmethod
    async def build(
        farmer,
        crop_stage,
        weather,
        weather_history
    ):

        consecutive_days = (
            ContextCalculators
            .calculate_consecutive_humidity_days(
                weather_history
            )
        )

        soil_moisture = (
            ContextCalculators
            .estimate_soil_moisture(
                weather.get("rainfall", 0),
                farmer.irrigation_type
            )
        )

        return {

            "crop_stage":
                crop_stage.strip().lower(),

            "soil_type":
                farmer.soil_type,

            "irrigation_type":
                farmer.irrigation_type,

            "temperature_c":
                weather.get("temperature", 0),

            "max_temperature_c":
                weather.get("temperature", 0),

            "min_temperature_c":
                weather.get("temperature", 0),

            "humidity_percent":
                weather.get("humidity", 0),

            "rainfall_mm_per_day":
                weather.get("rainfall", 0),

            "wind_speed_kmh":
                weather.get("wind_speed", 0),

            "consecutive_days":
                consecutive_days,

            "soil_moisture_percent":
                soil_moisture
        }