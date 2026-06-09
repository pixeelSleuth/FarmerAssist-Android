from pathlib import Path
import shutil
import uuid

from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.mysql import get_db
from app.models.farmer import Farmer

from app.voice_assistant.service import (
    VoiceAssistantService
)

router = APIRouter(
    prefix="/voice",
    tags=["Voice Assistant"]
)

UPLOAD_DIR = Path("uploads/voice")

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)


@router.post("/query")
async def voice_query(

    farmer_id: int,

    file: UploadFile = File(...),

    db: Session = Depends(get_db)

):

    farmer = (
        db.query(Farmer)
        .filter(
            Farmer.farmer_id == farmer_id
        )
        .first()
    )

    if not farmer:

        raise HTTPException(
            status_code=404,
            detail="Farmer not found"
        )

    extension = file.filename.split(".")[-1]

    filename = (
        f"{uuid.uuid4()}.{extension}"
    )

    audio_path = (
        UPLOAD_DIR / filename
    )

    with open(
        audio_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    result = await (
        VoiceAssistantService
        .process_voice(
            farmer,
            str(audio_path),
            db
        )
    )

    return result