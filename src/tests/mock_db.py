from dataclasses import asdict

from src.domain.entities.auth import User


class MockDatabaseClient:
    db = {
        "users": [],
        "vehicles": [],
    }

    async def get(self, email):
        result = list(filter(lambda x: x["email"] == email, self.db["users"]))
        if result:
            return result[0]

    async def insert(self, user: User):
        self.db["users"].append(asdict(user))
