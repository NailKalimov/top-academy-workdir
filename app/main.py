from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db import engine, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
   return {"message": "Hello, FastAPI in Docker!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
   return {"item_id": item_id, "description": f"Item {item_id} description"}

@app.get("/students_on_final_less")
def get_students():
   return{"response": ["Ivan", "Nikolay", "Andrew"]}