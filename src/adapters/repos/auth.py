from dataclasses import asdict

from elasticsearch import NotFoundError

from src.domain.entities.auth import User
from src.domain.exceptions import UserDoesNotExist
from src.domain.ports.repo import AuthRepoPort


class AuthRepo(AuthRepoPort):

    async def get(self, email: str) -> User:
        try:
            user_query = {
                "query": {
                    "term": {
                        "email.keyword": email
                    }
                }
            }
            result = await self.client.search(index=self.users_index, body=user_query)

            if result['hits']['total']['value'] == 0:
                raise UserDoesNotExist()

            return User(**result["hits"]["hits"][0]["_source"])

        except NotFoundError:
            raise UserDoesNotExist()

    async def insert(self, entity: User):
        await self.client.index(index=self.users_index, body=asdict(entity))
