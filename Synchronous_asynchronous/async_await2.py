#main.py
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()
	
@app.get("/task")
async def run_task():
    time.sleep(20)
    return {"status": "long_running task completed"}

@app.get("/quick")
async def quick_response():
    return {"status": "quick Response"}