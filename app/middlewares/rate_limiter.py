from aiohttp import web
from collections import defaultdict
import time

# Simple rate limiter: 100 requests per minute per user
RATE_LIMIT = 100
TIME_WINDOW = 60
user_timestamps = defaultdict(list)

async def rate_limiter_middleware(app, handler):
    async def middleware(request):
        user = request.user if hasattr(request, 'user') else 'guest'
        
        # Clean up old timestamps
        current_time = time.time()
        user_timestamps[user] = [ts for ts in user_timestamps[user] if current_time - ts < TIME_WINDOW]

        if len(user_timestamps[user]) >= RATE_LIMIT:
            return web.Response(text="Too many requests", status=429)

        user_timestamps[user].append(current_time)
        return await handler(request)
    return middleware
