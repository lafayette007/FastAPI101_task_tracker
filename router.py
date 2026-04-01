# API / ручки / эндпойнты

from typing import Annotated

from fastapi import (
    APIRouter,           # чтобы объявить декораторы эндпойнтов - @router (любое имя)
    Depends              # инъекция зависимостей
)

from repository import TaskRepository
from schemas import TaskAddSchema

router = APIRouter(
    prefix="/tasks",                # чтобы не писать его в каждом эндпойнте как здесь @router.post("/tasks")
    tags=["Задачи"],                # название группы на странице API
)

@router.post("")
async def add_task(
        # task: TaskAddSchema
        task: Annotated[TaskAddSchema, Depends()],
):
    # tasks.append(task)
    task_id = await TaskRepository.add_one(task)
    return {"Ok": True, "task_id": task_id}

@router.get("")
async def get_tasks():
    tasks = await TaskRepository.find_all()
    return {"tasks": tasks}
