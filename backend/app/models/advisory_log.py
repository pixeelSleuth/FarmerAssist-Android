from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import DateTime
from sqlalchemy import Text

from sqlalchemy.sql import func

from app.db.base import Base


class AdvisoryLog(Base):

    __tablename__ = "advisory_logs"

    advisory_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    farmer_id = Column(
        Integer,
        nullable=False,
        index=True
    )

    rule_id = Column(
        String(50),
        nullable=True
    )

    advisory_type = Column(
        String(50),
        nullable=True
    )

    category = Column(
        String(50),
        nullable=True
    )

    severity = Column(
        String(20),
        nullable=True
    )

    risk_score = Column(
        Integer,
        nullable=True
    )

    confidence_score = Column(
        Float,
        nullable=True
    )

    advisory_text = Column(
        Text,
        nullable=True
    )

    generated_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    feedback = Column(
        String(20),
        nullable=True
    )
