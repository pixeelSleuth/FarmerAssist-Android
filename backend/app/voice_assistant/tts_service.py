import base64
import requests
from pathlib import Path

from app.core.config import settings


class SarvamTTS:

    AUDIO_DIR = Path(
        "generated_audio"
    )

    AUDIO_DIR.mkdir(
        exist_ok=True
    )

    @staticmethod
    def synthesize(

        text: str,

        language: str,

        output_file: str

    ):

        language = str(
            language
        ).lower().strip()

        if language in [
            "kn",
            "kannada"
        ]:
            language = "kn-IN"

        elif language in [
            "en",
            "english"
        ]:
            language = "en-IN"

        else:
            language = "en-IN"

        headers = {

            "api-subscription-key":
                settings.SARVAM_API_KEY,

            "Content-Type":
                "application/json"
        }

        payload = {

            "inputs": [text],

            "target_language_code":
                language,

            "speaker":
                "arya",

            "pitch": 0,

            "pace": 1.0,

            "loudness": 1.0,

            "speech_sample_rate":
                22050,

            "enable_preprocessing":
                True
        }

        response = requests.post(

            settings.SARVAM_TTS_URL,

            headers=headers,

            json=payload,

            timeout=60
        )

        print(
            "\n===== TTS RESPONSE ====="
        )

        print(
            "STATUS:",
            response.status_code
        )

        print(
            response.text[:500]
        )

        print(
            "========================\n"
        )

        response.raise_for_status()

        result = response.json()

        audio_list = result.get(
            "audios",
            []
        )

        if not audio_list:

            raise Exception(
                "No audio returned by Sarvam"
            )

        audio_base64 = (
            audio_list[0]
        )

        audio_bytes = (
            base64.b64decode(
                audio_base64
            )
        )

        with open(
            output_file,
            "wb"
        ) as f:

            f.write(
                audio_bytes
            )

        print(
            "Audio saved:",
            output_file
        )

        return output_file