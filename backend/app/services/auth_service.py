from sqlalchemy.orm import Session

from app.models.farmer import Farmer


def get_farmer_by_uid(
    db: Session,
    uid: str
):

    return (
        db.query(Farmer)
        .filter(
            Farmer.firebase_uid == uid
        )
        .first()
    )


def create_farmer(
    db: Session,
    uid: str
):

    farmer = Farmer(
        firebase_uid=uid
    )

    db.add(farmer)

    db.commit()

    db.refresh(farmer)

    return farmer