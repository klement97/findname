from dataclasses import asdict

from elasticsearch import ConflictError

from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.exceptions import PublicationException, PublicationExistsException
from src.domain.ports.repo import InsertRepoPort


class VehicleRepo(InsertRepoPort):

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
