from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.auth import (
    get_current_farmer
)

from app.schemas.crop_stage import (
    CropStageResponse
)

from app.services.crop_stage_service import (
    get_current_crop_stage
)

router = APIRouter(
    prefix="/crop-stage",
    tags=["Crop Stage"]
)
@router.get(
    "/current",
    response_model=CropStageResponse
)
def current_stage(
    current_farmer=Depends(
        get_current_farmer
    )
):

    return get_current_crop_stage(
        current_farmer.sowing_date
    )