from typing import List

from fastapi import APIRouter, Form, HTTPException
from ormar import NoMatch

from .models import User, AuthModel

auth_router = APIRouter()
user_router = APIRouter()


@auth_router.post('/login')
async def login(user_details: AuthModel):
    try:
        user = await User.objects.get(username=user_details.username)
        password = await User.objects.get(password=user_details.password)
        if user and password:
            return user.dict(exclude={'password'})
    except NoMatch:
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
