#main.py
from fastapi import FastAPI
import item, user

app = FastAPI()

app.include_router(item.router)
app.include_router(item.user)