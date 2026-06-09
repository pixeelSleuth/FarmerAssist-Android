from fastapi import APIRouter
from fastapi import Depends

from app.dependencies.auth import (
    get_current_farmer
)

from app.rule_engine.services.rule_service import (
    evaluate_all_rules
)

from app.schemas.advisory import (
    AdvisoryResponse
)

router = APIRouter(
    prefix="/advisory",
    tags=["Advisory"]
)
@router.get(
    "/test",
    response_model=
    AdvisoryResponse
)
def test_rule_engine(
    current_farmer=Depends(
        get_current_farmer
    )
):

    context = {

        "temperature_c": 38,

        "humidity_percent": 88,

        "forecast_rainfall_mm": 80,

        "crop_stage": "silking",

        "wind_speed_kmh": 32
    }

    triggered = (
        evaluate_all_rules(
            context
        )
    )

    return {

        "triggered_rules":
            triggered
    }