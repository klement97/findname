from src.domain.entities.auth import User
from src.domain.ports.repo import AuthRepoPort


class MockAuthRepo(AuthRepoPort):
    async def insert(self, user: User):
        await self.client.insert(user)

    async def get(self, email: str) -> User:
        data = await self.client.get(email)
        if data:
            return User(**data)
