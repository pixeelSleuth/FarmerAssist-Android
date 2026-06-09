from app.mongodb.client import get_voice_collection


class ConversationService:

    @classmethod
    def save(
        cls,
        farmer_id,
        query,
        response,
        language,
        intent
    ):

        collection = get_voice_collection()
        
        if collection is None:
            return

        collection.insert_one(
            {
                "farmer_id":
                    farmer_id,

                "query":
                    query,

                "response":
                    response,

                "language":
                    language,

                "intent":
                    intent
            }
        )