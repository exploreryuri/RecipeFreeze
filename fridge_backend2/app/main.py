from fastapi import FastAPI
from app.routers import user
from app.models.user import User
from app.database import engine

app = FastAPI()

# Подключаем роутеры
app.include_router(user.router)

# Создаём таблицы
User.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to Fridge Backend API!"}