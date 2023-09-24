import os

from src.infra.config import AppEnv

APP_ENV = os.getenv('APP_ENV', AppEnv.DEV)
DEBUG = APP_ENV == AppEnv.DEV
VERSION = os.getenv('VERSION', "1")
SECRET_KEY = os.getenv('SECRET_KEY')
JWT_ALGORITHM = os.getenv('JWT_ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES = 720
PAGE_SIZE = 50
