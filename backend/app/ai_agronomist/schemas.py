from pydantic import BaseModel


class ChatRequest(
    BaseModel
):

    farmer_id: int

    query: str


class ChatResponse(
    BaseModel
):

    intent: str

    response: str