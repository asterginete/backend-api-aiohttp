from aiohttp import web
import aiomysql

from .routes import setup_routes
from .utils.database import init_db, close_db
from .middlewares.jwt_middleware import jwt_middleware
from .utils.cache import setup_cache
from .tasks import setup_celery

def create_app(config):
    app = web.Application(middlewares=[jwt_middleware])

    # Set up routes
    setup_routes(app)

    # Load configurations
    app['config'] = config

    # Set up database connection on startup and cleanup on shutdown
    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)

    # Set up caching mechanism
    setup_cache(app)

    # Set up Celery for background tasks
    celery_app = setup_celery(config)
    app['celery_app'] = celery_app

    return app
