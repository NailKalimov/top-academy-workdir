messages = []

"""
Асинхронный движок SQLAlchemy + фабрика асинхронных сессий.
Используется драйвер aiosqlite (sqlite+aiosqlite://).
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# URL подключения: относительный файл database.sqlite в корне проекта
DATABASE_URL = "sqlite+aiosqlite:///./database.sqlite"

# Создаём асинхронный движок. echo=True выводит SQL-запросы в лог (полезно при разработке)
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# async_sessionmaker создаёт сессии AsyncSession.
# expire_on_commit=False предотвращает "истечение" объектов после commit, что упрощает доступ к атрибутам.
AsyncSessionLocal = async_sessionmaker(
   bind=engine,
   expire_on_commit=False,
)

# Базовый класс моделей
Base = declarative_base()

class Item(Base):
   __tablename__ = "items"

   id = Column(Integer, primary_key=True, index=True)
   text = Column(String(300), nullable=False)
