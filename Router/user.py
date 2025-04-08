from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
async def read_user():
    return [{"username": "Rickie"}, {"username": "Martin"}]

@router.post("/me")
async def read_user_me():
    return {"username": "current_user"}

@router.put("/{username}")
async def read_user(username: str):
    return {"username": username}