from app.models.farmer import Farmer


def update_farmer_profile(
    farmer: Farmer,
    payload
):

    farmer.farmer_name = payload.farmer_name

    farmer.phone = payload.phone

    farmer.latitude = payload.latitude

    farmer.longitude = payload.longitude

    farmer.soil_type = payload.soil_type

    farmer.sowing_date = payload.sowing_date

    farmer.irrigation_type = payload.irrigation_type

    farmer.farm_dim = payload.farm_dim

    farmer.water_source = payload.water_source

    farmer.preferred_language = (
        payload.preferred_language
    )

    farmer.onboarding_completed = (
        payload.onboarding_completed
    )

    return farmer