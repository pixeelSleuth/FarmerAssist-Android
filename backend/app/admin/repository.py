from sqlalchemy.orm import Session

from app.models.admin import Admin

from app.models.farmer import Farmer

from app.models.disease_history import (
    DiseaseHistory
)

from app.models.notification import (
    Notification
)

from app.models.disease_alert import (
    DiseaseAlert
)


class AdminRepository:

    @staticmethod
    def get_admin_by_username(

        db: Session,

        username: str

    ):

        return (
            db.query(Admin)
            .filter(
                Admin.username ==
                username
            )
            .first()
        )

    @staticmethod
    def get_total_farmers(
        db: Session
    ):

        return (
            db.query(Farmer)
            .count()
        )

    @staticmethod
    def get_total_detections(
        db: Session
    ):

        return (
            db.query(
                DiseaseHistory
            ).count()
        )

    @staticmethod
    def get_total_alerts(
        db: Session
    ):

        return (
            db.query(
                DiseaseAlert
            ).count()
        )

    @staticmethod
    def get_total_notifications(
        db: Session
    ):

        return (
            db.query(
                Notification
            ).count()
        )