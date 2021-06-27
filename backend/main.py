import databases
import ormar
import sqlalchemy
from fastapi import FastAPI

from app.config import settings

app = FastAPI()

database = databases.Database(settings.db_url)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    active: bool = ormar.Boolean(default=True, nullable=False)


engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)


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
