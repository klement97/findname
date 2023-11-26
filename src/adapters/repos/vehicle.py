from dataclasses import asdict

from src.domain.entities.vehiclepublication import VehiclePublication
from src.domain.ports.repo import InsertRepoPort


class VehicleRepo(InsertRepoPort):

    async def insert(self, vp: VehiclePublication):
        response = await self.client.create(
            index=self.vehicles_index,
            id=str(vp.id),
            document=asdict(vp),
        )
        if response['result'] != 'created':
            raise Exception('Could not create vehicle')
