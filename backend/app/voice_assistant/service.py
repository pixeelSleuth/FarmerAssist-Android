from pathlib import Path
import uuid

from app.voice_assistant.stt_service import (
    SarvamSTT
)

from app.voice_assistant.tts_service import (
    SarvamTTS
)

from app.ai_agronomist.service import (
    AIAgronomist
)

from app.core.config import settings


class VoiceAssistantService:

    AUDIO_DIR = Path(
        "generated_audio"
    )

    AUDIO_DIR.mkdir(
        exist_ok=True
    )

    @classmethod
    async def process_voice(

        cls,

        farmer,

        audio_path,

        db

    ):

        stt_response = (
            SarvamSTT.transcribe(
                audio_path
            )
        )

        if "error" in stt_response:

            return {

                "success": False,

                "message":
                    stt_response["error"][
                        "message"
                    ]
            }

        query = (

            stt_response.get(
                "transcript"
            )

            or

            stt_response.get(
                "text"
            )

            or

            ""
        )

        if not query:

            return {

                "success": False,

                "message":
                    "No transcript returned"
            }

        result = await (
            AIAgronomist.chat(

                farmer,

                query,

                db
            )
        )

        output_audio = (
            cls.AUDIO_DIR
            /
            f"{uuid.uuid4()}.mp3"
        )

        SarvamTTS.synthesize(

            text=
                result["response"],

            language=
                farmer.preferred_language,

            output_file=
                str(output_audio)
        )

        audio_url = (

            f"{settings.BASE_URL}"

            f"/audio/"

            f"{output_audio.name}"
        )

        return {

            "success": True,

            "query":
                query,

            "intent":
                result["intent"],

            "response":
                result["response"],

            "audio_url":
                audio_url
        }