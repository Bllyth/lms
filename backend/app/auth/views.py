from fastapi import APIRouter, Form

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login/')
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}
