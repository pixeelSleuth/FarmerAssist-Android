from app.disease_alerts.utils import (
    calculate_distance_km
)

from app.disease_alerts.repository import (
    DiseaseAlertRepository
)

from app.notifications.service import (
    NotificationService
)
class DiseaseAlertService:

    ALERT_RADIUS_KM = 5

    @classmethod
    def process_alerts(

        cls,

        db,

        source_farmer,

        disease_name
    ):

        if not source_farmer:
            return 0

        farmers = (
            DiseaseAlertRepository
            .get_all_farmers(db)
        )

        alerts_created = 0

        for farmer in farmers:

            if (
                farmer.farmer_id
                ==
                source_farmer.farmer_id
            ):
                continue

            distance = (
                calculate_distance_km(

                    source_farmer.latitude,
                    source_farmer.longitude,

                    farmer.latitude,
                    farmer.longitude
                )
            )

            if (
                distance
                <=
                cls.ALERT_RADIUS_KM
            ):
                DiseaseAlertRepository.save_alert(

                    db=db,

                    source_farmer_id=
                        source_farmer.farmer_id,

                    target_farmer_id=
                        farmer.farmer_id,

                    disease_name=
                        disease_name,

                    distance_km=
                        round(distance, 2)
                )
                NotificationService.send_notification(

                    db=db,

                    farmer_id=
                        farmer.farmer_id,

                    title=
                        "Disease Alert",

                    message=
                        f"{disease_name} "
                        f"reported "
                        f"{round(distance,2)} km "
                        f"from your farm."
                )

                alerts_created += 1

        return alerts_created