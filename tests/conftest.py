import pytest
from aiohttp import web
from aiohttp.test_utils import TestClient, TestServer
from app import create_app
from app.utils.database import init_db, close_db

@pytest.fixture
def app():
    """Create and return an aiohttp Application."""
    app = create_app()
    return app

@pytest.fixture
async def client(aiohttp_client, app):
    """Create and return an aiohttp TestClient."""
    return await aiohttp_client(app)

@pytest.fixture
async def db_session(app):
    """Create a database session for testing."""
    async with app['db'].acquire() as conn:
        yield conn

@pytest.fixture
async def test_server(loop, app):
    """Create and return a TestServer instance."""
    return TestServer(app, loop=loop)

@pytest.fixture
async def test_client(loop, test_server):
    """Create and return a TestClient instance."""
    client = TestClient(test_server, loop=loop)
    await client.start_server()
    return client

@pytest.fixture(scope='function', autouse=True)
async def setup_db(app):
    """Set up the database before each test and tear it down after."""
    # Set up
    await init_db(app)

    yield

    # Tear down
    await close_db(app)
