from fastapi import APIRouter, Form

from .models import User

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login')
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


@user_router.post('/add_user', response_model=User)
async def add_user(user: User):
    await user.save()
    return user


@user_router.get('/{user_id}', response_model=User)
async def get_user(user_id: int):
    user_db = await User.objects.get(id=user_id)
    return user_db
