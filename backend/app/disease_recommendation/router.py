from fastapi import (
    APIRouter,
    HTTPException
)

from app.disease_recommendation.service import (
    DiseaseRecommendationService
)

router = APIRouter(
    prefix="/recommendation",
    tags=["Disease Recommendation"]
)
@router.get("/{disease_name}")
def get_recommendation(
    disease_name: str
):

    recommendation = (
        DiseaseRecommendationService
        .get_recommendation(
            disease_name,
            0.95
        )
    )

    if not recommendation:

        raise HTTPException(
            status_code=404,
            detail="Disease not found"
        )

    return recommendation