from pydantic import BaseModel


class NotificationCreate(
    BaseModel
):

    farmer_id: int

    title: str

    message: str

    notification_type: str