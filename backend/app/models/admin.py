from sqlalchemy import (
    Column,
    Integer,
    String,
    TIMESTAMP,
    text
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Admin(Base):

    __tablename__ = "admins"

    admin_id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String(100),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(50),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        server_default=text(
            "CURRENT_TIMESTAMP"
        )
    )