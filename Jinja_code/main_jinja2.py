#main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# jinja2 Template 생성. 인자로 directory 입력
templates = Jinja2Templates(directory="Templates")

class Item(BaseModel):
    name: str
    price: float


@app.get("/all_items", response_class=HTMLResponse)
async def read_all_items(request: Request):
    all_items = [Item(name="test_item_"+str(i), price=i) for i in range(5)]
    return templates.TemplateResponse(
        request=request, 
        name="for_item.html", 
        context={"all_items": all_items}
    )