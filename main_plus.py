# FastAPI import
from fastapi import FastAPI

# FastAPI instance 생성.
app = FastAPI()

# Path 오퍼레이션 생성. Path는 도메인명을 제외하고 / 로 시작하는 URL 부분
# 만약 url이 https://example.com/items/foo 라면 path는 /items/foo
# Operation은 GET, POST, PUT/PATCH, DELETE등의 HTTP 메소드임.
@app.get("/1", summary="덧셈", tags=["sum"])
def root():
    return 1+3
@app.get("/2", summary="뼬셈", tags=["sub"])
def root():
    return 9-5
@app.get("/3", summary="곱셈", tags=["mul"])
def root():
    return 2*2
@app.get("/4", summary="나눗셈", tags=["div"])
def root():
    return 8/2
@app.get("/5", summary="제곱", tags=["power"])
def root():
    return 2**2