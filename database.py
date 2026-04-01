from sqlalchemy.ext.asyncio import (
    create_async_engine,                # движок для БД
    async_sessionmaker                  # фабрика создания сессий (транзакций для работы с БД)
)
from sqlalchemy.orm import (
    DeclarativeBase,                    # декларативное создание таблиц
    Mapped,                             # для объявления типов полей
    mapped_column                       # для полей типа Column
)

# движок для подключения к БД
engine = create_async_engine(
    url="sqlite+aiosqlite:///tasks.db"
)

# фабрика сессий для работы с БД
new_session = async_sessionmaker(engine, expire_on_commit=False)

# таблицы БД
# базовый класс всех остальных таблиц - от него будем их наследовать
# 1 таблица БД = 1 класс
class Base(DeclarativeBase):
    pass

# таблица Задачи
class TasksModel(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)   # указываем что это поле - первичный ключ таблицы (нам обязательно нужен хотя бы один)
    name: Mapped[str] = mapped_column()
    description: Mapped[str | None] = mapped_column()

# создание таблиц - эта АСИНХРОННАЯ функция берётся из доки по SQLAlchemy
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# удаление таблиц - обычно не используется (т.к. таблицы БД это очень ценная инфа)
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)