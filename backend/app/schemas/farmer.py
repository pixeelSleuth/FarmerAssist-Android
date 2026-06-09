from datetime import date

from pydantic import BaseModel
from pydantic import Field
from pydantic import field_validator


class FarmerProfileCreate(BaseModel):

    farmer_name: str = Field(...)

    phone: str = Field(...)

    latitude: float

    longitude: float

    soil_type: str | None = None

    sowing_date: date | None = None

    irrigation_type: str | None = None

    farm_dim: float | None = None

    water_source: str | None = None

    preferred_language: str = "Kannada"

    onboarding_completed: bool = True

    @field_validator("farm_dim")
    def validate_farm_area(cls, value):

        if value is not None and value <= 0:
            raise ValueError(
                "Farm area must be greater than 0"
            )

        return value


class FarmerProfileResponse(BaseModel):

    farmer_id: int

    farmer_name: str | None

    phone: str | None

    latitude: float | None

    longitude: float | None

    soil_type: str | None

    sowing_date: date | None

    irrigation_type: str | None

    farm_dim: float | None

    water_source: str | None

    preferred_language: str | None

    onboarding_completed: bool | None

    class Config:
        from_attributes = True

class FarmerDashboardResponse(BaseModel):

    farmer_id: int

    farmer_name: str | None

    crop_age: int | None

    soil_type: str | None

    irrigation_type: str | None

    onboarding_completed: bool