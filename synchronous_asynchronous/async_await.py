#main.py
import multiprocessing
import threading
from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

@app.get("/quick")
async def quick_response():
    return {"status": "Server is running"}

# ----------------
async def long_running_task():
    await asyncio.sleep(5)        
    print("Async task completed")

@app.get("/async_task")
async def run_task():
    await long_running_task()
    return {"status": "long_running task completed"}

#--------------------
def long_running_task2():
    time.sleep(5)  
    print("Thread task completed")      
    return 

@app.get("/thread-task")
def run_thread_task():
    thread1 = threading.Thread(target=long_running_task2)
    thread1.start()
    return {"thread task : start"}

#--------------------
def long_running_task3():
    time.sleep(5)  
    print("Multiprocessing task completed")      
    return 

@app.get("/multiprocessing-task")
def run_thread_task():
    prosess = multiprocessing.Process(target=long_running_task3)
    prosess.start()
    return {"multiprocessing task : start"}