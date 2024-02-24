import pytest
from faker import Faker
from jose import jwt

from src.domain.entities.auth import SignupData, User
from src.infra import config

faker = Faker()


def test_signup_data_raises_error_when_passwords_dont_match():
    signup_data = SignupData(
        email=faker.email(),
        password=faker.password(),
        re_password=faker.password(),
    )

    with pytest.raises(ValueError):
        signup_data.verify_password()


def test_signup_data_dont_raise_error_when_passwords_match():
    password = faker.password()
    signup_data = SignupData(
        email=faker.email(),
        password=password,
        re_password=password,
    )

    assert signup_data.verify_password() is None


def test_user_get_public_info_removes_password():
    user = User(email=faker.email(), password=faker.password())
    info = user.get_public_info()

    assert "password" not in info


def test_hash_password_changes_plain_password():
    plain_password = faker.password()
    user = User(email=faker.email(), password=plain_password)
    user.hash_password()

    assert user.password != plain_password


def test_verify_password_returns_true_when_passwords_match():
    plain_password = faker.password()
    user = User(email=faker.email(), password=plain_password)
    user.hash_password()

    assert user.verify_password(plain_password)


def test_verify_password_returns_false_when_passwords_dont_match():
    user = User(email=faker.email(), password=faker.password())
    user.hash_password()

    assert not user.verify_password(faker.password())


def test_create_access_token():
    user = User(email=faker.email(), password=faker.password())
    encoded_jwt = user.create_access_token()

    decoded_jwt = jwt.decode(encoded_jwt, key=config.SECRET_KEY, algorithms=config.ALGORITHM)

    assert decoded_jwt["sub"] == user.email
