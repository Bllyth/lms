from ormar import Model, Integer, String, Boolean

from ..db import BaseMeta 


class User(Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = Integer(primary_key=True)
    name: str = String(nullable=False)
    username: str = String(unique=True, max_length=128, nullable=False)
    email: str = String(max_length=128, unique=True, nullable=False)
    password: str = String(nullable=False)
    id_no: str = Integer(unique=True)
    phone_no: int = Integer(unique=True, nullable=False)
    active: bool = Boolean(default=True, nullable=False)