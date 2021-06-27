from fastapi import FastAPI

from app.db import User, database

app = FastAPI()


@app.get('/')
async def root():
    return {
        "message": "Welcome to vercel"
    }


@app.on_event('startup')
async def startup():
    if not database.is_connected():
        await database.connect()

    await User.objects.get_or_create(email="test@test.com")


@app.on_event('shutdown')
async def shutdown():
    if database.is_connected:
        await database.disconnect()