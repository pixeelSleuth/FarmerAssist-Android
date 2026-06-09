from pathlib import Path
import shutil
import uuid
from app.disease_recommendation.service import (
    DiseaseRecommendationService
)
from app.notifications.service import (
    NotificationService
)
from app.disease_alerts.service import (
    DiseaseAlertService
)
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.db.mysql import get_db
from app.dependencies.auth import get_current_farmer
from app.models.farmer import Farmer

from app.disease_detection.service import (
    DiseaseDetectionService
)

from app.disease_detection.repository import (
    DiseaseRepository
)

router = APIRouter(
    prefix="/disease",
    tags=["Disease Detection"]
)

UPLOAD_DIR = Path(
    "uploads/disease_images"
)

UPLOAD_DIR.mkdir(
    parents=True,
    exist_ok=True
)
@router.post("/detect")
async def detect_disease(

    file: UploadFile = File(...),

    current_farmer=Depends(
        get_current_farmer
    ),

    db: Session = Depends(get_db)

):

    try:

        extension = (
            file.filename
            .split(".")[-1]
        )

        filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        file_path = (
            UPLOAD_DIR / filename
        )

        with open(
            file_path,
            "wb"
        ) as buffer:

            shutil.copyfileobj(
                file.file,
                buffer
            )

        detections = (
            DiseaseDetectionService
            .detect(
                str(file_path)
            )
        )

        recommendations = []

        for detection in detections:

            recommendation = (
                DiseaseRecommendationService
                .get_recommendation(
                    detection[
                        "disease_name"
                    ],
                    detection[
                        "confidence"
                    ]
                )
            )

            DiseaseRepository.save_detection(

                db=db,

                farmer_id=current_farmer.farmer_id,

                disease_name=
                    detection[
                        "disease_name"
                    ],

                confidence=
                    detection[
                        "confidence"
                    ],

                image_path=
                    str(file_path),

                treatment_given=
                    "\n".join(
                        recommendation.get(
                            "chemical_control",
                            []
                        )
                    )
            )
            source_farmer = (
                db.query(Farmer)
                .filter(
                    Farmer.farmer_id
                    ==
                    current_farmer.farmer_id
                )
                .first()
            )
            if detection["confidence"] >= 0.80:

                DiseaseAlertService.process_alerts(

                    db=db,

                    source_farmer=
                        source_farmer,

                    disease_name=
                        detection[
                            "disease_name"
                        ]
                )

            recommendations.append(
                recommendation
            )
            NotificationService.send_notification(

                db=db,

                farmer_id=current_farmer.farmer_id,

                title="Disease Detected",

                message=(
                    f"{detection['disease_name']} "
                    f"detected with "
                    f"{round(detection['confidence']*100,2)}%"
                    f" confidence"
                )
            )

        return {

            "success": True,

            "total_detections":
                len(detections),

            "detections":
                recommendations
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

@router.get(
    "/history"
)
def get_history(

    current_farmer=Depends(
        get_current_farmer
    ),

    db: Session = Depends(
        get_db
    )
):

    records = (
        DiseaseRepository
        .get_history(
            db,
            current_farmer.farmer_id
        )
    )

    return records