from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import DATABASE_URL

# Create an asynchronous engine tied to the database URL from the config
engine = create_async_engine(DATABASE_URL, echo=True)

# Create a custom session class bound to the engine
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()

async def init_db():
    """
    Initialize the database by creating tables.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def close_db():
    """
    Close the database connection.
    """
    await engine.dispose()

