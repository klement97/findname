import pytest
from faker import Faker

from src.domain.entities.auth import User
from src.tests.mock_deps import mock_read_use_info_use_case, mock_auth_repo

pytestmark = pytest.mark.anyio
faker = Faker()


async def test_password_is_excluded():
    user = User(
        email=faker.email(),
        password=faker.password(),
    )
    repo = mock_auth_repo()
    await repo.insert(user)

    use_case = mock_read_use_info_use_case()
    data = await use_case.execute(user.email)

    assert "password" not in data
