import sqlalchemy

from .base import metadata
from .config import settings

from .auth.models import User

engine = sqlalchemy.create_engine(settings.DB_URL)
metadata.create_all(engine)
