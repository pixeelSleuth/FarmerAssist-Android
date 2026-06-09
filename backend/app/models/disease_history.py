from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Text,
    Date,
    TIMESTAMP,
    ForeignKey
)

from sqlalchemy.sql import func

from app.db.base import Base


class DiseaseHistory(Base):

    __tablename__ = "disease_history"

    disease_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farmer_id = Column(
        Integer,
        ForeignKey("pro.farmer_id")
    )

    disease_name = Column(
        String(100)
    )

    detection_date = Column(
        Date
    )

    confidence = Column(
        Float
    )

    image_path = Column(
        Text
    )

    treatment_given = Column(
        Text
    )

    detected_at = Column(
        TIMESTAMP,
        server_default=func.now()
    )