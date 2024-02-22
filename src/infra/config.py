import os
from enum import unique, StrEnum


@unique
class AppEnv(StrEnum):
    DEV = 'DEV'
    STAGING = 'STAGING'
    PROD = 'PROD'


SECRET_KEY = os.getenv(
    "SECRET_KEY",
    default="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 7 days
APP_ENV = os.getenv('APP_ENV')
DB_URL = os.getenv('DB_URL')
ES_USER = os.getenv('ES_USER')
ES_PASSWORD = os.getenv('ES_PASSWORD')
VERIFY_CERTS = bool(int(os.getenv('VERIFY_CERTS')))
CA_CERTS = os.getenv('CA_CERTS') if VERIFY_CERTS else None
