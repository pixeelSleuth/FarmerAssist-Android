from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.mysql import get_db

from app.schemas.auth import (
    FirebaseTokenRequest,
    AuthResponse
)

from app.core.firebase import verify_firebase_token

from app.services.auth_service import (
    get_farmer_by_uid,
    create_farmer
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/verify",
    response_model=AuthResponse
)
def verify_user(
    request: FirebaseTokenRequest,
    db: Session = Depends(get_db)
):

    decoded = verify_firebase_token(
        request.firebase_token
    )

    uid = decoded["uid"]

    farmer = get_farmer_by_uid(
        db,
        uid
    )

    if farmer:

        return {
            "success": True,
            "farmer_exists": True,
            "farmer_id": farmer.farmer_id
        }

    farmer = create_farmer(
        db,
        uid
    )

    return {
        "success": True,
        "farmer_exists": False,
        "farmer_id": farmer.farmer_id
    }