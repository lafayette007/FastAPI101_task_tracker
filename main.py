from fastapi import (
    FastAPI,
    Depends             # инъекция зависимостей
)
from pydantic import BaseModel
from sqlalchemy.sql.annotation import Annotated

app = FastAPI()

# это схемы в Pydantic - для проверки типов данных и ввода значений полей
class STaskAdd(BaseModel):
    name: str
    description: str | None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
):
    tasks.append(task)
    return {"Ok": True}

# @app.get("/tasks")
# def get_tasks():
#     task = STask(name="Создай Strategy OS", description="Система стратегического планирования")
#     return {"data": task}
