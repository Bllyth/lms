import databases
import ormar
import sqlalchemy

from .config import settings

database = databases.Database(settings.DB_URL)
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


