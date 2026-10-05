from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
   return {"message": "Hello, FastAPI in Docker!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
   return {"item_id": item_id, "description": f"Item {item_id} description"}