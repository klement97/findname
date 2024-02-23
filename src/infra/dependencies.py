from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from fastapi import status
from jose import jwt, JWTError

from src.adapters.repos.auth import AuthRepo
from src.adapters.repos.vehicle import VehicleRepo
from src.domain.use_cases.login import LoginUseCase
from src.domain.use_cases.publish_vehicle import PublishVehicleUseCase
from src.domain.use_cases.read_user_info import ReadUserInfoUseCase
from src.domain.use_cases.signup import SignupUseCase
from src.infra import config
from src.infra.db import Database, AiohttpHttpNode

# Using an additional /auth/login-form endpoint so we can use the class directly.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login-form")


async def get_current_user_email(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    return email


async def get_db():
    # todo: implement singleton
    return Database(
        address=config.DB_URL,
        config={
            "headers": {"accept": "application/vnd.elasticsearch+json; compatible-with=8"},
            "http_compress": True,
            "node_class": AiohttpHttpNode,
            "request_timeout": 100,
            "basic_auth": (config.ES_USER, config.ES_PASSWORD) if config.ES_USER else None,
            "verify_certs": False,
            "ca_certs": config.CA_CERTS,
        },
    )


async def vehicle_repo():
    db = await get_db()
    return VehicleRepo(client=db.client)


async def auth_repo():
    db = await get_db()
    return AuthRepo(db.client)


async def signup_use_case():
    repo = await auth_repo()
    return SignupUseCase(repo)


async def login_use_case():
    repo = await auth_repo()
    return LoginUseCase(repo)


async def read_user_info_use_case():
    repo = await auth_repo()
    return ReadUserInfoUseCase(repo)


async def publish_vehicle_use_case():
    repo = await vehicle_repo()
    return PublishVehicleUseCase(repo)
