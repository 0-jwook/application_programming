#main_path.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/all") 
def read_all_items():
    return {"message": "all items"}


@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id} 

