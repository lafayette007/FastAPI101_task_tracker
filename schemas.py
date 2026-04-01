from pydantic import BaseModel, ConfigDict


# это схемы в Pydantic - для проверки типов данных и ввода значений полей
class TaskAddSchema(BaseModel):
    name: str
    description: str | None = None


class TaskSchema(TaskAddSchema):
    id: int
    # попробуй не только как словарь распарсить этот объект, а ещё как экземпляр класса из атрибутов его достань все свойства
    model_config = ConfigDict(from_attributes=True)


class TaskIdSchema(BaseModel):
    ok: bool = True
    task_id: int
