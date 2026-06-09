from app.ai_agronomist.context_builder import (
    AIContextBuilder
)

from app.ai_agronomist.llm_service import (
    LLMService
)

from app.ai_agronomist.conversation_service import (
    ConversationService
)


class AIAgronomist:

    @staticmethod
    async def chat(
        farmer,
        query,
        db
    ):

        context = (
            await AIContextBuilder.build(
                farmer,
                db
            )
        )

        intent = (
            await LLMService.classify_intent(
                query
            )
        )

        response = (
            await LLMService.generate_response(
                query=query,
                context=context,
                language=
                farmer.preferred_language
            )
        )

        ConversationService.save(

            farmer_id=
            farmer.farmer_id,

            query=query,

            response=response,

            language=
            farmer.preferred_language,

            intent=
            intent["intent"]
        )

        return {

            "intent":
            intent["intent"],

            "response":
            response
        }