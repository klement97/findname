"""Containers module."""
import os

from dependency_injector import containers, providers

from src.adapters.repos.vehicle import VehicleRepo
from src.domain.use_cases.publish_vehicle import PublishVehicleUseCase
from src.infra.db import Database, AiohttpHttpNode


class Container(containers.DeclarativeContainer):
    app_env = os.getenv('APP_ENV')
    db_url = os.getenv('DB_URL')
    es_user = os.getenv('ES_USER')
    es_password = os.getenv('ES_PASSWORD')
    verify_certs = bool(int(os.getenv('VERIFY_CERTS')))
    ca_certs = os.getenv('CA_CERTS') if verify_certs else None

    db = providers.Singleton(
        Database,
        address=db_url,
        config={
            "headers": {"accept": "application/vnd.elasticsearch+json; compatible-with=8"},
            "http_compress": True,
            "node_class": AiohttpHttpNode,
            "request_timeout": 100,
            "basic_auth": (es_user, es_password) if es_user else None,
            "verify_certs": verify_certs,
            "ca_certs": ca_certs,
        },
    )

    vehicle_repo = providers.Factory(
        VehicleRepo,
        client=db.provided.client
    )

    publish_vehicle_use_case = providers.Factory(
        PublishVehicleUseCase,
        vehicle_repo=vehicle_repo,
    )


container = Container()
