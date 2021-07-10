from ormar import ModelMeta
from sqlalchemy import MetaData
from databases import Database
from .config import settings

# Initialize Database
DATABASE_URL = settings.DATABASE_URL
database = Database(DATABASE_URL)
metadata = MetaData()


# Declare a BaseMeta
class BaseMeta(ModelMeta):
    database = database
    metadata = metadata
