import uuid
from dataclasses import dataclass, field, asdict
from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext

from src.infra import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@dataclass
class SignupData:
    email: str
    password: str
    re_password: str

    def verify_password(self):
        if self.password != self.re_password:
            raise ValueError("Passwords don't match")


@dataclass
class LoginData:
    email: str
    password: str


@dataclass
class User:
    email: str
    password: str
    full_name: str | None = None
    phone: str | None = None
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)

    def get_public_info(self):
        d = asdict(self)
        d.pop("password")

        return d

    def hash_password(self):
        self.password = pwd_context.hash(self.password)

    def verify_password(self, plain_password) -> bool:
        return pwd_context.verify(plain_password, self.password)

    def create_access_token(self, expires_delta: timedelta | None = None):
        expires_delta = expires_delta or timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        expire = datetime.now() + expires_delta
        to_encode = {
            "sub": self.email,
            "exp": expire,
        }
        encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)

        return encoded_jwt
