from abc import ABC

from elasticsearch import AsyncElasticsearch


class RepoPort(ABC):
    vehicles_index = 'vehicles'

    def __init__(self, client: AsyncElasticsearch):
        self.client = client


class InsertRepoPort(RepoPort):

    def insert(self, entity):
        raise NotImplementedError()
