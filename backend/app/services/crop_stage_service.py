from fastapi import HTTPException

from app.engines.crop_stage_engine import (
    CropStageEngine
)


def get_current_crop_stage(
    sowing_date
):

    if sowing_date is None:

        raise HTTPException(
            status_code=400,
            detail="Sowing date not set"
        )

    crop_age = (
        CropStageEngine
        .calculate_crop_age(
            sowing_date
        )
    )

    stage = (
        CropStageEngine
        .get_stage(
            crop_age
        )
    )

    return {
        "crop_age": crop_age,
        "current_stage":
            stage["current_stage"],
        "stage_name":
            stage["stage_name"]
    }


def determine_stage(
    sowing_date
):

    current_stage = get_current_crop_stage(
        sowing_date
    )

    return (
        current_stage["current_stage"]
        .lower()
    )