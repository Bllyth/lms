from datetime import datetime, timedelta

from jose import jwt
from ormar import Model, Integer, String, Boolean
from passlib.context import CryptContext
from pydantic import BaseModel

from ..config import settings
from ..base import BaseMeta

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str


class User(Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = Integer(primary_key=True)
    name: str = String(max_length=200, nullable=False)
    username: str = String(unique=True, max_length=128, nullable=False)
    email: str = String(max_length=128, unique=True, nullable=False)
    password: str = String(max_length=128, nullable=False)
    id_no: str = Integer(unique=True)
    phone_no: int = Integer(unique=True, nullable=False)
    active: bool = Boolean(default=True, nullable=False)

    def check_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password)

    @property
    def token(self) -> str:
        now = datetime.utcnow()
        exp = (now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()

        data = {
            "exp": exp,
            "email": self.email
        }

        return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def hash_password(password: str) -> str:
    # Generate a hashed password of the provided password
    return pwd_context.hash(password)
