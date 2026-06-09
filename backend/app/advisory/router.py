from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies.auth import get_current_farmer
from app.engines.advisory_pipeline import AdvisoryPipeline
from app.db.mysql import get_db

router = APIRouter(
    prefix="/advisory",
    tags=["Advisory"]
)


@router.get("/generate")
async def generate_advisory(
    current_farmer=Depends(
        get_current_farmer
    ),
    db: Session = Depends(get_db)
):

    pipeline = AdvisoryPipeline(db)

    advisories = await pipeline.run(
        current_farmer
    )

    return {
        "success": True,
        "advisories": advisories
    }