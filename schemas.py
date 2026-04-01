from pydantic import BaseModel

# это схемы в Pydantic - для проверки типов данных и ввода значений полей
class TaskAddSchema(BaseModel):
    name: str
    description: str | None = None


class TaskSchema(TaskAddSchema):
    id: int
