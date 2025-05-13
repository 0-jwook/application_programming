#main_response.py

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float | None = None

class ItemResp(BaseModel):
    name: str
    description: str
    price_with_tax: float

app = FastAPI()

@app.post("/items/", response_model=ItemResp)
async def create_item(item: Item):
    price_with_tax = item.price + item.tax
    return ItemResp(name=item.name, description=item.description, price_with_tax=price_with_tax)