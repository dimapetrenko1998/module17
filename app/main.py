from fastapi import FastAPI
from routers import task, user
from sqlalchemy import create_engine
from module17.app.backend.db import Base
from models import User, Task


app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task.router)
app.include_router(user.router)
engine = create_engine("sqlite:///taskmanager.db", echo=True)
Base.metadata.create_all(engine)
