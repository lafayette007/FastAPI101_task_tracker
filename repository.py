# пишем запросы к БД - реализовываем паттерн репозиторий - работаем с БД как с коллекцией объектов - CRUD-операции
# здесь упрощённый паттерн Репозиторий - не будем создавать экземпляры репозитория, не будет Unit_Of_Work
from sqlalchemy import select
from database import new_session, TasksModel
from schemas import TaskAddSchema


class TaskRepository:
    @classmethod        # чтобы не нужно было создавать инстанс/экземпляр этого класса
    async def add_one(cls, data: TaskAddSchema) -> int:
        async with new_session() as session:
            task_dict = data.model_dump()   # метод model_dump() превращает дынные (data = task) к виду словаря
            task = TasksModel(**task_dict)  # не указываем поля таблицы явно - а передаём раскрытый словарь **task_dict
            session.add(task)               # добавляем объект task в сессию БД
            await session.flush()           # чтобы узнать первичный ключ (id) перед коммитом
            await session.commit()          # вот здесь только происходит обращение к БД и происходят все изменения
            return task.id                  # возвращаем значение id новой задачи - её первичный ключ (автоинкремент в БД)


    @classmethod  # чтобы не нужно было создавать инстанс/экземпляр этого класса
    async def find_all(cls):
        async with new_session() as session:
            query = select(TasksModel)
            result = await session.execute(query)   # итератор
            task_models = result.scalars().all()
            return task_models