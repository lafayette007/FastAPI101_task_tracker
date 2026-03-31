from fastapi import (
    FastAPI,
    Depends             # инъекция зависимостей
)
from pydantic import BaseModel
from typing import Annotated

# https://fastapi.tiangolo.com/advanced/events/ - копируем код отсюда про Lifespan (жизненный цикл)
from contextlib import asynccontextmanager  # декоратор, который позволяет создавать контекстные менеджеры со словом yield

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # вставим 2 ф-ции -
    # 1) удалять все старые таблицы при старте приложения - просто сейчас так удобно
    # 2) создавать все новые таблицы при старте приложения
    await delete_tables()
    print("База таблиц очищена")
    await create_tables()
    print("База таблиц готова к работе")

    yield
    print("Выключение приложения")

app = FastAPI(lifespan=lifespan)
 
# это схемы в Pydantic - для проверки типов данных и ввода значений полей
class TaskAddSchema(BaseModel):
    name: str
    description: str | None


class TaskSchema(TaskAddSchema):
    id: int


tasks = []

@app.post("/tasks")
async def add_task(
        # task: TaskAddSchema
        task: Annotated[TaskAddSchema, Depends()],
):
    tasks.append(task)
    return {"Ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = TaskSchema(name="Создай Strategy OS", description="Система стратегического планирования")
#     return {"data": task}
