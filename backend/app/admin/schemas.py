from pydantic import BaseModel


class AdminLoginRequest(
    BaseModel
):

    username: str

    password: str


class AdminLoginResponse(
    BaseModel
):

    access_token: str

    token_type: str

    role: str


class DashboardSummary(
    BaseModel
):

    total_farmers: int

    total_detections: int

    total_alerts: int

    total_notifications: int