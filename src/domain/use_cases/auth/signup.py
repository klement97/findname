from src.domain.entities.auth import SignupData, User
from src.domain.exceptions import UserAlreadyExistsException
from src.domain.ports.repo import AuthRepoPort
from src.domain.ports.use_case import UseCasePort


class SignupUseCase(UseCasePort):
    def __init__(self, repo: AuthRepoPort):
        self.repo = repo

    async def execute(self, signup_data: SignupData):
        signup_data.verify_password()
        user = await self.repo.get(signup_data.email)
        if user:
            raise UserAlreadyExistsException()

        user = User(email=signup_data.email, password=signup_data.password)
        user.hash_password()
        await self.repo.insert(user)
