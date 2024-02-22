from src.adapters.repos.auth import AuthRepo
from src.adapters.repos.vehicle import VehicleRepo
from src.domain.use_cases.login import LoginUseCase
from src.domain.use_cases.publish_vehicle import PublishVehicleUseCase
from src.domain.use_cases.signup import SignupUseCase
from src.infra import config
from src.infra.db import Database, AiohttpHttpNode


async def get_db():
    # todo: implement singleton
    return Database(
        address=config.DB_URL,
        config={
            "headers": {"accept": "application/vnd.elasticsearch+json; compatible-with=8"},
            "http_compress": True,
            "node_class": AiohttpHttpNode,
            "request_timeout": 100,
            "basic_auth": (config.ES_USER, config.ES_PASSWORD) if config.ES_USER else None,
            "verify_certs": False,
            "ca_certs": config.CA_CERTS,
        },
    )


async def get_vehicle_repo():
    db = await get_db()
    return VehicleRepo(client=db.client)


async def get_auth_repo():
    db = await get_db()
    return AuthRepo(db.client)


async def get_signup_use_case():
    repo = await get_auth_repo()
    return SignupUseCase(repo)


async def get_login_use_case():
    repo = await get_auth_repo()
    return LoginUseCase(repo)


async def get_publish_vehicle_use_case():
    repo = await get_vehicle_repo()
    return PublishVehicleUseCase(repo)
