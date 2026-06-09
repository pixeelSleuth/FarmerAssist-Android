from pydantic import BaseModel


class DetectionResult(BaseModel):

    disease_name: str

    confidence: float


class DetectionResponse(BaseModel):

    success: bool

    detections: list