import json
import redis

from app.db.redis import redis_client


CACHE_TTL = 1800   # 30 minutes


def get_cache(key: str):
    try:
        data = redis_client.get(key)
    except redis.exceptions.RedisError:
        return None

    if data:
        return json.loads(data)

    return None


def set_cache(
    key: str,
    value: dict
):
    try:
        redis_client.setex(
            key,
            CACHE_TTL,
            json.dumps(value)
        )
    except redis.exceptions.RedisError:
        # If Redis is unavailable, silently skip caching.
        return