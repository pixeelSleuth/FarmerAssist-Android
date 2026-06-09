from pymongo import MongoClient
from app.core.config import settings

client = MongoClient(settings.MONGO_URI)

mongodb = client["farmer_advisory"]

chat_collection = mongodb["ai_chats"]

voice_collection = mongodb["voice_queries"]

activity_collection = mongodb["activity_logs"]