"""Containers module."""
from dependency_injector import containers, providers

from infra.db import Database, AiohttpHttpNode


class AppContainer(containers.DeclarativeContainer):
    config = providers.Configuration()
    config.app_env.from_env('APP_ENV')
    config.db_url.from_env('DB_URL')
    config.es_user.from_env('ES_USER')
    config.es_password.from_env('ES_PASSWORD')
    config.es_verify_certs.from_env('ES_VERIFY_CERTS')
    config.curl_ca_bundle.from_env('CURL_CA_BUNDLE')

    db = providers.Singleton(
        Database,
        address=config.db_url,
        config={
            "headers": {"accept": "application/vnd.elasticsearch+json; compatible-with=8"},
            "http_compress": True,
            "node_class": AiohttpHttpNode,
            "request_timeout": 100,
            "basic_auth": (config.es_user, config.es_password) if config.es_user else None,
            "verify_certs": config.es_verify_certs,
            "ca_certs": config.curl_ca_bundle,
        },
    )


container = AppContainer()
