from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

from config import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

db_session = Session(bind=engine)
def init_db():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session