import pytest
from faker import Faker

from src.domain.entities.auth import SignupData, User
from src.domain.exceptions import UserAlreadyExistsException
from src.tests.mock_deps import mock_signup_use_case, mock_auth_repo

faker = Faker()
pytestmark = pytest.mark.anyio


async def test_verifies_password():
    use_case = mock_signup_use_case()
    data = SignupData(
        email=faker.email(),
        password=faker.password(),
        re_password=faker.password(),
    )

    with pytest.raises(ValueError):
        await use_case.execute(data)


async def test_when_user_exists_raises_error():
    user = User(
        email=faker.email(),
        password=faker.password()
    )
    repo = mock_auth_repo()
    await repo.insert(user)

    use_case = mock_signup_use_case()
    data = SignupData(
        email=user.email,
        password=user.password,
        re_password=user.password,
    )

    with pytest.raises(UserAlreadyExistsException):
        await use_case.execute(data)


async def test_creates_user_and_hashes_password():
    use_case = mock_signup_use_case()
    plain_password = faker.password()
    data = SignupData(
        email=faker.email(),
        password=plain_password,
        re_password=plain_password,
    )
    await use_case.execute(data)

    repo = mock_auth_repo()
    user = await repo.get(data.email)

    assert user.id
    assert user.password != plain_password
