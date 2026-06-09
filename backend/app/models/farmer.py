from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import DateTime

from sqlalchemy.sql import func

from app.db.base import Base


class Farmer(Base):

    __tablename__ = "pro"

    farmer_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    firebase_uid = Column(
        String(128),
        unique=True,
        nullable=False
    )

    farmer_name = Column(
        String(100),
        nullable=True
    )

    phone = Column(
        String(15),
        unique=True,
        nullable=True
    )

    latitude = Column(
        Float,
        nullable=True
    )

    longitude = Column(
        Float,
        nullable=True
    )

    soil_type = Column(
        String(50),
        nullable=True
    )

    sowing_date = Column(
        Date,
        nullable=True
    )

    irrigation_type = Column(
        String(50),
        nullable=True
    )

    farm_dim = Column(
        Float,
        nullable=True
    )

    water_source = Column(
        String(50),
        nullable=True
    )

    preferred_language = Column(
        String(20),
        default="Kannada"
    )

    onboarding_completed = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )