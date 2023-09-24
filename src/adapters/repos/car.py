from src.domain.entities.car import Car
from src.domain.ports.repo import InsertRepoPort


class CarRepo(InsertRepoPort):

    async def insert(self, car: Car):
        response = await self.client.create(
            index=self.cars_index,
            id=car.id,
            document=car.to_dict(),
        )
        if response['result'] != 'created':
            raise Exception('Could not create car')
