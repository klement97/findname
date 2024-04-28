from src.domain.entities.auth import LoginData
from src.domain.exceptions import IncorrectCredentialsException
from src.domain.ports.repo import AuthRepoPort
from src.domain.ports.use_case import UseCasePort


class LoginUseCase(UseCasePort):
    def __init__(self, repo: AuthRepoPort):
        self.repo = repo

    async def execute(self, login_data: LoginData):
        user = await self.repo.get(email=login_data.email)
        if not user:
            # todo: hash password here to remove time difference
            raise IncorrectCredentialsException()

        if not user.verify_password(login_data.password):
            raise IncorrectCredentialsException()

        return {
            "access_token": user.create_access_token()
        }
