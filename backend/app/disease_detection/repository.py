from datetime import date

from app.models.disease_history import (
    DiseaseHistory
)


class DiseaseRepository:

    @staticmethod
    def save_detection(
        db,
        farmer_id,
        disease_name,
        confidence,
        image_path,
        treatment_given=None
    ):

        record = DiseaseHistory(
            treatment_given=treatment_given,
            farmer_id=farmer_id,
            disease_name=disease_name,
            detection_date=date.today(),
            confidence=confidence,
            image_path=image_path
        )

        db.add(record)

        db.commit()

        db.refresh(record)

        return record

    @staticmethod
    def get_history(
        db,
        farmer_id
    ):

        return (
            db.query(
                DiseaseHistory
            )
            .filter(
                DiseaseHistory.farmer_id
                == farmer_id
            )
            .order_by(
                DiseaseHistory.detected_at.desc()
            )
            .all()
        )