from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.db.mysql import get_db

from app.dependencies.auth import (
    get_current_farmer
)

from app.schemas.farmer import (
    FarmerProfileCreate,
    FarmerProfileResponse,
    FarmerDashboardResponse
)

from app.services.farmer_service import (
    update_farmer_profile
)

from app.utils.crop_utils import (
    calculate_crop_age
)
router = APIRouter(
    prefix="/farmers",
    tags=["Farmers"]
)
@router.post(
    "/complete-profile",
    response_model=FarmerProfileResponse
)
def complete_profile(
    payload: FarmerProfileCreate,
    current_farmer=Depends(
        get_current_farmer
    ),
    db: Session = Depends(get_db)
):

    update_farmer_profile(
        current_farmer,
        payload
    )

    db.commit()

    db.refresh(current_farmer)

    return current_farmer

@router.get(
    "/me",
    response_model=FarmerProfileResponse
)
def get_profile(
    current_farmer=Depends(
        get_current_farmer
    )
):

    return current_farmer

@router.put(
    "/update-profile",
    response_model=FarmerProfileResponse
)
def update_profile(
    payload: FarmerProfileCreate,
    current_farmer=Depends(
        get_current_farmer
    ),
    db: Session = Depends(get_db)
):

    update_farmer_profile(
        current_farmer,
        payload
    )

    db.commit()

    db.refresh(current_farmer)

    return current_farmer

@router.get(
    "/dashboard",
    response_model=FarmerDashboardResponse
)
def dashboard(
    current_farmer=Depends(
        get_current_farmer
    )
):

    crop_age = calculate_crop_age(
        current_farmer.sowing_date
    )

    return {
        "farmer_id":
        current_farmer.farmer_id,

        "farmer_name":
        current_farmer.farmer_name,

        "crop_age":
        crop_age,

        "soil_type":
        current_farmer.soil_type,

        "irrigation_type":
        current_farmer.irrigation_type,

        "onboarding_completed":
        current_farmer.onboarding_completed
    }