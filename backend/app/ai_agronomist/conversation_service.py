from app.mongodb.client import (
    get_voice_collection
)
import logging

logger = logging.getLogger(__name__)


class ConversationService:

    @staticmethod
    def save(

        farmer_id,

        query,

        response,

        language,

        intent

    ):

        collection = get_voice_collection()
        
        if collection is None:
            logger.warning("Cannot save to MongoDB: voice_collection is None. Check MongoDB connection.")
            return

        try:
            collection.insert_one({

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

            })
            logger.info(f"✓ Chat saved for farmer {farmer_id}")
        except Exception as e:
            logger.error(f"✗ Failed to save chat to MongoDB: {e}")