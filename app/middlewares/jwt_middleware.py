from aiohttp import web
import jwt
from app.config import SECRET_KEY

async def jwt_middleware(app, handler):
    async def middleware(request):
        if request.path.startswith('/login') or request.path.startswith('/register'):
            return await handler(request)

        token = request.headers.get('Authorization')
        if not token:
            return web.Response(text="Token missing", status=401)

        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            request.user = decoded_token.get('username')
        except jwt.ExpiredSignatureError:
            return web.Response(text="Token has expired", status=401)
        except jwt.InvalidTokenError:
            return web.Response(text="Invalid token", status=401)

        return await handler(request)
    return middleware
