from fastapi import APIRouter
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.db import Base

router = APIRouter(prefix="/user", tags=["user"])


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)

    tasks = relationship("Task", back_populates="user")


@router.get("/")
def all_users():
    pass


@router.get("/{user_id}")
def user_by_id(user_id: int):
    pass


@router.post("/create")
def create_user():
    pass


@router.put("/update")
def update_user():
    pass


@router.delete("/delete")
def delete_user():
    pass
