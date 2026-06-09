from pydantic import BaseModel


class FirebaseTokenRequest(BaseModel):

    firebase_token: str


class AuthResponse(BaseModel):

    success: bool

    farmer_exists: bool

    farmer_id: int | None