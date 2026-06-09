from pydantic import BaseModel


class AdvisoryContext(BaseModel):

    crop_stage: str

    soil_type: str

    irrigation_type: str

    temperature_c: float
    max_temperature_c: float
    min_temperature_c: float

    humidity_percent: float

    rainfall_mm_per_day: float

    wind_speed_kmh: float

    consecutive_days: int

    soil_moisture_percent: float