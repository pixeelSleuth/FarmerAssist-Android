from app.notifications.repository import (
    NotificationRepository
)


class NotificationService:

    @staticmethod
    def send_notification(
        db,
        farmer_id,
        title,
        message
    ):

        return (
            NotificationRepository
            .create(
                db,
                farmer_id,
                title,
                message
            )
        )