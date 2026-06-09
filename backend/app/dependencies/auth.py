from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.orm import Session

from app.db.mysql import get_db

from app.core.firebase import verify_firebase_token

from app.models.farmer import Farmer

security = HTTPBearer()


def get_current_farmer(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    try:

        decoded = verify_firebase_token(
            token
        )

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid Firebase Token"
        )

    uid = decoded["uid"]

    farmer = (
        db.query(Farmer)
        .filter(
            Farmer.firebase_uid == uid
        )
        .first()
    )

    if not farmer:

        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    return farmer