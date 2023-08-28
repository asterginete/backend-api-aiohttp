from aiohttp import web
import aiomysql
import config

from app.routes import setup_routes
from app.utils.database import init_db, close_db

app = web.Application()

# Set up routes from the routes module
setup_routes(app)

# Load configurations from config.py
app['config'] = config

# Set up database connection on startup and cleanup on shutdown
app.on_startup.append(init_db)
app.on_cleanup.append(close_db)

if __name__ == '__main__':
    web.run_app(app, host=config.HOST, port=config.PORT)
