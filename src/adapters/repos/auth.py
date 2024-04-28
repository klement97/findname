from dataclasses import asdict

from src.domain.entities.auth import User
from src.domain.ports.repo import AuthRepoPort


class AuthRepo(AuthRepoPort):

    async def get(self, email: str) -> User | None:
        user_query = {
            "query": {
                "term": {
                    "email.keyword": email
                }
            }
        }
        result = await self.client.search(index=self.users_index, body=user_query)

        if result["hits"]["hits"]:
            return User(**result["hits"]["hits"][0]["_source"])

    async def insert(self, entity: User):
        await self.client.index(index=self.users_index, body=asdict(entity))
