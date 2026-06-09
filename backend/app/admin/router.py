from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import (
    Session
)

from app.db.mysql import (
    get_db
)

from app.admin.schemas import (

    AdminLoginRequest

)

from app.admin.service import (
    AdminService
)

router = APIRouter(

    prefix="/admin",

    tags=["Admin"]
)
@router.post(
    "/login"
)
def login(

    request:
    AdminLoginRequest,

    db: Session =
    Depends(get_db)

):

    result = (
        AdminService.login(

            db,

            request.username,

            request.password
        )
    )

    if not result:

        raise HTTPException(

            status_code=401,

            detail=
            "Invalid credentials"
        )

    return result

@router.get(
    "/dashboard"
)
def dashboard(

    db: Session =
    Depends(get_db)

):

    return (

        AdminService
        .dashboard_summary(
            db
        )
    )