from fastapi import FastAPI

# https://fastapi.tiangolo.com/advanced/events/ - копируем код отсюда про Lifespan (жизненный цикл)
from contextlib import asynccontextmanager  # декоратор, который позволяет создавать контекстные менеджеры со словом yield

from database import create_tables, delete_tables
from router import router as tasks_router


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
app.include_router(tasks_router)        # добавление нового роутера в FastAPI
