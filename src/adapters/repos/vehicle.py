from dataclasses import asdict

from elasticsearch import ConflictError

from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.exceptions import PublicationException, PublicationExistsException
from src.domain.ports.repo import VehicleRepoPort


class VehicleRepo(VehicleRepoPort):

    async def insert(self, vp: VehiclePublication):
        try:
            response = await self.client.create(
                index=self.vehicles_index,
                id=str(vp.id),
                document=asdict(vp),
            )
            if response['result'] != 'created':
                raise PublicationException(vp.id)

        except ConflictError:
            raise PublicationExistsException(vp.id)

    async def get(self, email):
        query = {
            "query": {
                "term": {
                    "publisher.email.keyword": email
                }
            }
        }
        result = await self.client.search(index=self.vehicles_index, body=query)
        if hits := result['hits']['hits']:
            return [
                r["_source"] for r in hits
            ]
