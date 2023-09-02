import aiomysql.sa
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

# SQLAlchemy configurations
DATABASE_URL = f"mysql+mysqlconnector://{config.DB_CONFIG['user']}:{config.DB_CONFIG['password']}@{config.DB_CONFIG['host']}:{config.DB_CONFIG['port']}/{config.DB_CONFIG['db']}"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

metadata = MetaData()

async def init_db(app):
    config = app['config']['DB_CONFIG']
    engine = await aiomysql.sa.create_engine(
        db=config['db'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port'],
        autocommit=config['autocommit']
    )
    app['db'] = engine

async def close_db(app):
    app['db'].close()
    await app['db'].wait_closed()
