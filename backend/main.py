from fastapi import FastAPI

from app.base import database
from api import api_router

app = FastAPI()


@app.on_event("startup")
async def startup() -> None:
    if not database.is_connected:
        await database.connect()
    # # create a dummy entry
    # await User.objects.get_or_create(email="test@test.com")


@app.on_event("shutdown")
async def shutdown() -> None:
    if database.is_connected:
        await database.disconnect()


app.include_router(api_router)
