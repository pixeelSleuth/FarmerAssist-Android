import json

from google import genai

from app.core.config import settings

from app.prompts.intent_prompt import (
    INTENT_PROMPT
)

from app.prompts.agronomist_prompt import (
    AGRONOMIST_PROMPT
)

client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class LLMService:

    @staticmethod
    async def classify_intent(
        query: str
    ):

        prompt = f"""
{INTENT_PROMPT}

User Query:

{query}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        text = response.text.strip()

        try:
            return json.loads(text)

        except Exception:

            return {
                "intent": "GENERAL"
            }

    @staticmethod
    async def generate_response(
        query: str,
        context: dict,
        language: str
    ):

        prompt = f"""
{AGRONOMIST_PROMPT}

LANGUAGE:
{language}

FARMER CONTEXT:

{json.dumps(
    context,
    default=str,
    indent=2
)}

QUESTION:

{query}
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        return response.text