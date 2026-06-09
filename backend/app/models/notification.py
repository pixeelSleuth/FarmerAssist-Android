from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    TIMESTAMP,
    ForeignKey
)

from app.db.base import Base


class Notification(Base):

    __tablename__ = "notifications"

    notification_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farmer_id = Column(
        Integer,
        ForeignKey(
            "pro.farmer_id"
        )
    )

    title = Column(
        String(200)
    )

    message = Column(
        Text
    )

    status = Column(
        String(20)
    )

    sent_at = Column(
        TIMESTAMP
    )