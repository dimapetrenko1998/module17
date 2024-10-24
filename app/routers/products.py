from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from ..backend.db_depends import get_db
from typing import Annotated
from ..models import user, task
from ..schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete

router = APIRouter()


@router.get("/tasks", response_model=list[task])
def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.execute(select(task)).scalars().all()
    return tasks


@router.get("/tasks/{task_id}", response_model=task)
def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)], task=None):
    task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/tasks/create", status_code=status.HTTP_201_CREATED)
def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)], user=None):
    user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = task(**task.dict(), user_id=user_id)
    db.execute(insert(task).values(new_task))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.put("/tasks/update/{task_id}", status_code=status.HTTP_200_OK)
def update_task(task_id: int, task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(update(task).where(task.id == task_id).values(**task.dict()))
    db.commit()
    return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete("/tasks/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_task = db.execute(select(task).where(task.id == task_id)).scalar_one_or_none()
    if existing_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(delete(task).where(task.id == task_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'Task deleted successfully!'}


@router.get("/users/{user_id}/tasks", response_model=list[task])
def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    tasks = db.execute(select(task).where(task.user_id == user_id)).scalars().all()
    return tasks


@router.delete("/users/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(user).where(user.id == user_id)).scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(task).where(task.user_id == user_id))
    db.execute(delete(user).where(user.id == user_id))
    db.commit()
    return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'User and associated tasks deleted successfully!'}
