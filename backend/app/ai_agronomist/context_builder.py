from app.services.weather_service import (
    get_current_weather
)

from app.services.crop_stage_service import (
    determine_stage
)

from app.advisory.repository import (
    get_recent_advisories
)

from app.disease_detection.repository import (
    DiseaseRepository
)

from app.notifications.repository import (
    NotificationRepository
)


class AIContextBuilder:

    @staticmethod
    async def build(
        farmer,
        db
    ):

        crop_stage = determine_stage(
            farmer.sowing_date
        )

        weather = get_current_weather(
            farmer.latitude,
            farmer.longitude
        )

        diseases = (
            DiseaseRepository
            .get_history(
                db,
                farmer.farmer_id
            )
        )

        notifications = (
            NotificationRepository
            .get_latest(
                farmer.farmer_id
            )
        )

        advisories = (
            get_recent_advisories(
                farmer.farmer_id
            )
        )

        return {

            "farmer": farmer,

            "crop_stage":
                crop_stage,

            "weather":
                weather,

            "disease_history":
                diseases,

            "notifications":
                notifications,

            "advisories":
                advisories
        }