from pymongo import MongoClient
from app.core.config import settings
import logging
import certifi
logger = logging.getLogger(__name__)

_client = None
_db = None
_voice_collection = None
_chat_collection = None


def get_client():
    global _client
    if _client is None and settings.MONGODB_URI:
        try:
            _client = MongoClient(
                settings.MONGODB_URI,
                serverSelectionTimeoutMS=5000,
                ssl=True,
                tlsAllowInvalidCertificates=True,
                tlsCAFile=certifi.where()
            )
            _client.admin.command('ping')
            logger.info("✓ MongoDB connected successfully")
        except Exception as e:
            logger.error(f"✗ MongoDB connection failed: {e}")
            _client = None
    return _client


def get_db():
    global _db
    client = get_client()
    if client is not None and settings.MONGODB_DB:
        _db = client[settings.MONGODB_DB]
    return _db


def get_voice_collection():
    global _voice_collection
    db = get_db()
    if db is not None:
        _voice_collection = db["voice_conversations"]
    return _voice_collection


def get_chat_collection():
    global _chat_collection
    db = get_db()
    if db is not None:
        _chat_collection = db["chat_conversations"]
    return _chat_collection


client = None
db = None
voice_collection = None
chat_collection = None