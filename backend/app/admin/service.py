from datetime import (
    datetime,
    timedelta
)

from jose import jwt

from passlib.context import (
    CryptContext
)

from app.admin.repository import (
    AdminRepository
)

from app.core.config import (
    settings
)


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


class AdminService:

    @staticmethod
    def verify_password(

        plain_password,

        hashed_password

    ):

        return (
            pwd_context.verify(
                plain_password,
                hashed_password
            )
        )

    @staticmethod
    def create_access_token(

        data: dict,

        expires_minutes=1440

    ):

        payload = data.copy()

        payload["exp"] = (
            datetime.utcnow()
            +
            timedelta(
                minutes=
                expires_minutes
            )
        )

        return jwt.encode(

            payload,

            settings.JWT_SECRET,

            algorithm="HS256"
        )

    @classmethod
    def login(

        cls,

        db,

        username,

        password

    ):

        admin = (
            AdminRepository
            .get_admin_by_username(
                db,
                username
            )
        )

        if not admin:

            return None

        valid = (
            cls.verify_password(
                password,
                admin.password_hash
            )
        )

        if not valid:

            return None

        token = (
            cls.create_access_token(
                {
                    "admin_id":
                    admin.admin_id,

                    "role":
                    admin.role
                }
            )
        )

        return {

            "access_token":
                token,

            "token_type":
                "bearer",

            "role":
                admin.role
        }

    @staticmethod
    def dashboard_summary(
        db
    ):

        return {

            "total_farmers":

                AdminRepository
                .get_total_farmers(
                    db
                ),

            "total_detections":

                AdminRepository
                .get_total_detections(
                    db
                ),

            "total_alerts":

                AdminRepository
                .get_total_alerts(
                    db
                ),

            "total_notifications":

                AdminRepository
                .get_total_notifications(
                    db
                )
        }