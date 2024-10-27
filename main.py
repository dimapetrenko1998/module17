from fastapi import FastAPI
from models.task import router as task_router
from models.user import router as user_router
from sqlalchemy import create_engine
from backend.db import Base


engine = create_engine("sqlite:///taskmanager.db", echo=True)

Base.metadata.create_all(engine)

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to Taskmanager"}


app.include_router(task_router)
app.include_router(user_router)
