import abc
from abc import ABC

from elasticsearch import AsyncElasticsearch

from src.domain.entities.auth import User


class RepoPort(ABC):
    users_index = "users"
    vehicles_index = "vehicles"

    def __init__(self, client):
        self.client = client


class InsertRepoPort(RepoPort, abc.ABC):
    @abc.abstractmethod
    async def insert(self, entity): ...


class AuthRepoPort(InsertRepoPort, abc.ABC):
    @abc.abstractmethod
    async def insert(self, user: User): ...

    @abc.abstractmethod
    async def get(self, email: str) -> User | None: ...
