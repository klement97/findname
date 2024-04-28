from src.domain.use_cases.auth.login import LoginUseCase
from src.domain.use_cases.auth.read_user_info import ReadUserInfoUseCase
from src.domain.use_cases.auth.signup import SignupUseCase
from src.tests.mock_db import MockDatabaseClient
from src.tests.mock_repos.mock_auth_repo import MockAuthRepo


def mock_db():
    return MockDatabaseClient()


def mock_auth_repo() -> MockAuthRepo:
    return MockAuthRepo(client=mock_db())


def mock_signup_use_case() -> SignupUseCase:
    return SignupUseCase(repo=mock_auth_repo())


def mock_login_use_case() -> LoginUseCase:
    return LoginUseCase(repo=mock_auth_repo())


def mock_read_use_info_use_case() -> ReadUserInfoUseCase:
    return ReadUserInfoUseCase(repo=mock_auth_repo())
