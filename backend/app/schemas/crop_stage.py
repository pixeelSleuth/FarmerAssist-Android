from pydantic import BaseModel


class CropStageResponse(
    BaseModel
):

    crop_age: int

    current_stage: str

    stage_name: str

    