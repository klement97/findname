from enum import unique, StrEnum


@unique
class AppEnv(StrEnum):
    DEV = 'DEV'
    STAGING = 'STAGING'
    PROD = 'PROD'
