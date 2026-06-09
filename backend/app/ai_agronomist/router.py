from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.mysql import get_db
from app.dependencies.auth import get_current_farmer

from app.ai_agronomist.schemas import (
    ChatRequest
)

from app.ai_agronomist.service import (
    AIAgronomist
)

router = APIRouter(
    prefix="/ai",
    tags=["AI Agronomist"]
)
@router.post("/chat")
async def chat(

    request: ChatRequest,

    current_farmer=Depends(
        get_current_farmer
    ),

    db: Session = Depends(
        get_db
    )
):

    return await AIAgronomist.chat(

        current_farmer,

        request.query,

        db
    )