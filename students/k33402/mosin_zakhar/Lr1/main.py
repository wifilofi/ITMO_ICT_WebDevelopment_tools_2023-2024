import uvicorn
from fastapi import FastAPI
from sqlmodel import SQLModel

from db.db import engine
from endpoints.user_endpoints import user_router
from endpoints.money_endpoints import main_router
from models.user_models import *

app = FastAPI()

app.include_router(user_router)
app.include_router(main_router, prefix="/api")


def create_db():
    SQLModel.metadata.create_all(engine)


@app.on_event("startup")
def on_startup():
    create_db()


if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8007)

