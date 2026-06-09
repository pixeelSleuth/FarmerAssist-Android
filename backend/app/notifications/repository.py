from datetime import datetime

from app.models.notification import Notification


class NotificationRepository:

    @staticmethod
    def create(
        db,
        farmer_id,
        title,
        message,
        status="UNREAD"
    ):

        notification = Notification(

            farmer_id=farmer_id,

            title=title,

            message=message,

            status=status,

            sent_at=datetime.utcnow()
        )

        db.add(notification)

        db.commit()

        db.refresh(notification)

        return notification

    @staticmethod
    def get_latest(
        farmer_id,
        limit=10
    ):
        from app.db.mysql import SessionLocal
        
        db = SessionLocal()
        
        try:
            notifications = (
                db.query(Notification)
                .filter(
                    Notification.farmer_id == farmer_id
                )
                .order_by(
                    Notification.sent_at.desc()
                )
                .limit(limit)
                .all()
            )
            return notifications
        finally:
            db.close()