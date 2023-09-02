import aiocache
from aiocache import cached, Cache
from app.config import REDIS_URL

# Configure aiocache to use Redis
aiocache.Cache.CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_URL': REDIS_URL
}

cache = Cache(Cache.REDIS)

async def set_cache(key, value, ttl=300):
    """
    Set a value in the cache with an optional time-to-live (TTL).
    
    Args:
    - key (str): The cache key.
    - value: The value to cache.
    - ttl (int): Time-to-live in seconds. Default is 300 seconds (5 minutes).
    """
    await cache.set(key, value, ttl=ttl)

async def get_cache(key):
    """
    Get a value from the cache by its key.
    
    Args:
    - key (str): The cache key.
    
    Returns:
    - The cached value or None if the key is not found.
    """
    return await cache.get(key)

async def delete_cache(key):
    """
    Delete a value from the cache by its key.
    
    Args:
    - key (str): The cache key.
    """
    await cache.delete(key)

async def clear_cache():
    """
    Clear all values from the cache.
    """
    await cache.clear()
