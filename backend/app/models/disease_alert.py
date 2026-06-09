from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.sql import func

from app.db.base import Base


class DiseaseAlert(Base):

    __tablename__ = "disease_alerts"

    alert_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    source_farmer_id = Column(
        Integer,
        ForeignKey(
            "pro.farmer_id"
        ),
        nullable=False
    )

    target_farmer_id = Column(
        Integer,
        ForeignKey(
            "pro.farmer_id"
        ),
        nullable=False
    )

    disease_name = Column(
        String(100)
    )

    distance_km = Column(
        Float
    )

    sent_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )

    status = Column(
        String(20),
        default="SENT"
    )