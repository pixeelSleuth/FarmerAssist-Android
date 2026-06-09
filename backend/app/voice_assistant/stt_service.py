import mimetypes
import requests

from app.core.config import settings


class SarvamSTT:

    @staticmethod
    def transcribe(
        audio_file_path
    ):

        mime_type, _ = mimetypes.guess_type(
            audio_file_path
        )

        if mime_type is None:
            mime_type = "audio/mpeg"

        headers = {
            "api-subscription-key":
                settings.SARVAM_API_KEY
        }

        with open(
            audio_file_path,
            "rb"
        ) as f:

            files = {

                "file": (

                    audio_file_path.split("/")[-1],

                    f,

                    mime_type
                )
            }

            response = requests.post(

                settings.SARVAM_STT_URL,

                headers=headers,

                files=files
            )

        print(
            "STT STATUS:",
            response.status_code
        )

        try:

            data = response.json()

            print(
                "STT RESPONSE:",
                data
            )

            return data

        except Exception:

            print(
                "INVALID STT RESPONSE"
            )

            raise Exception(
                "Sarvam STT failed"
            )