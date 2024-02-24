import pytest
from jose import jwt

from src.domain.entities.auth import LoginData, User
from src.domain.exceptions import IncorrectCredentialsException
from src.infra import config
from src.tests.domain.entities.test_auth import faker
from src.tests.mock_deps import mock_login_use_case, mock_auth_repo

pytestmark = pytest.mark.anyio


async def test_raises_exception_when_user_does_not_exist():
    use_case = mock_login_use_case()
    login = LoginData(
        email=faker.email(),
        password=faker.password(),
    )

    with pytest.raises(IncorrectCredentialsException):
        await use_case.execute(login)


async def test_raises_exception_when_password_is_incorrect():
    user = User(
        email=faker.email(),
        password=faker.password(),
    )
    user.hash_password()
    repo = mock_auth_repo()
    await repo.insert(user)

    login = LoginData(
        email=user.email,
        password=faker.password(),
    )
    use_case = mock_login_use_case()

    with pytest.raises(IncorrectCredentialsException):
        await use_case.execute(login)


async def test_returns_access_token_when_success():
    plain_password = faker.password()
    user = User(
        email=faker.email(),
        password=plain_password,
    )
    user.hash_password()
    repo = mock_auth_repo()
    await repo.insert(user)

    login = LoginData(
        email=user.email,
        password=plain_password,
    )
    use_case = mock_login_use_case()
    response = await use_case.execute(login)

    assert "access_token" in response
    decoded_jwt = jwt.decode(
        response["access_token"],
        key=config.SECRET_KEY,
        algorithms=config.ALGORITHM,
    )
    assert decoded_jwt["sub"] == user.email
