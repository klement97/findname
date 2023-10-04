from dataclasses import asdict

from src.domain.entities.car import Car
from src.domain.ports.repo import InsertRepoPort


class CarRepo(InsertRepoPort):

    async def insert(self, car: Car):
        response = await self.client.create(
            index=self.cars_index,
            id=str(car.id),
            document=asdict(car),
        )
        if response['result'] != 'created':
            raise Exception('Could not create car')
