from app.models.disease_alert import (
    DiseaseAlert
)
from app.models.farmer import Farmer


class DiseaseAlertRepository:

    @staticmethod
    def save_alert(
        db,
        source_farmer_id,
        target_farmer_id,
        disease_name,
        distance_km
    ):

        alert = DiseaseAlert(

            source_farmer_id=
                source_farmer_id,

            target_farmer_id=
                target_farmer_id,

            disease_name=
                disease_name,

            distance_km=
                distance_km,

            status="SENT"
        )

        db.add(alert)

        db.commit()

        db.refresh(alert)

        return alert

    @staticmethod
    def get_all_farmers(db):
        return (
            db.query(Farmer)
            .all()
        )