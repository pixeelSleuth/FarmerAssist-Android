from pydantic import BaseModel


class VoiceResponse(
    BaseModel
):

    query: str

    intent: str

    response: str

    audio_file: str