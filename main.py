from aiohttp import web
import aiomysql
import config

from app.routes import setup_routes
from app.utils.database import init_db, close_db
from app.middlewares.jwt_middleware import jwt_middleware
from app.utils.cache import setup_cache
from app.tasks import setup_celery

app = web.Application(middlewares=[jwt_middleware])

# Set up routes from the routes module
setup_routes(app)

# Load configurations from config.py
app['config'] = config

# Set up database connection on startup and cleanup on shutdown
app.on_startup.append(init_db)
app.on_cleanup.append(close_db)

# Set up caching mechanism
setup_cache(app)

# Set up Celery for background tasks
celery_app = setup_celery(config)
app['celery_app'] = celery_app

if __name__ == '__main__':
    web.run_app(app, host=config.HOST, port=config.PORT)
