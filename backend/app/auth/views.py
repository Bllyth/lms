from typing import List

from fastapi import APIRouter, Form, HTTPException

from .models import User

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    user = User.objects.get(username=username)
    if user:
        return user
    raise HTTPException(status_code=400, detail="Invalid username or password")


@user_router.post('/add_user', response_model=User)
async def add_user(user: User):
    await user.save()
    return user


@user_router.get('/', response_model=List[User])
async def get_users():
    users = await User.objects.all()
    return users


@user_router.get('/{user_id}', response_model=User)
async def get_user(user_id: int):
    user_db = await User.objects.get(id=user_id)
    return user_db
