import asyncio

from sqlalchemy.dialects.postgresql import asyncpg

from config import *
from celery import Celery
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flat_parse import parse_and_save

broker = f'redis://{REDIS_HOST}:{REDIS_PORT}'
worker = Celery('tasks', broker=broker)

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
db_session = Session()


@worker.task(name='Parse')
def parse_flat(url: str):
    asyncio.run(parse_and_save(url, DATABASE_URL))

