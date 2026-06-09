from datetime import datetime


class ContextCalculators:

    @staticmethod
    def calculate_consecutive_humidity_days(
        weather_history,
        threshold=85
    ):

        count = 0

        for day in reversed(weather_history):

            if day["humidity_percent"] >= threshold:
                count += 1
            else:
                break

        return count

    @staticmethod
    def estimate_soil_moisture(
        rainfall_mm,
        irrigation_type
    ):

        score = 30

        if rainfall_mm >= 20:
            score += 30

        if irrigation_type == "Drip":
            score += 20

        return min(score, 100)