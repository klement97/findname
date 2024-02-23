from src.domain.ports.repo import AuthRepoPort
from src.domain.ports.use_case import UseCasePort


class ReadUserInfoUseCase(UseCasePort):
    def __init__(self, repo: AuthRepoPort):
        self.repo = repo

    async def execute(self, email: str):
        user = await self.repo.get(email)
        return user.get_public_info()
