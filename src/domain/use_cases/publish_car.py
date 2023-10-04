from src.adapters.repos.car import CarRepo
from src.domain.entities.car import Car
from src.domain.ports.use_case import UseCasePort


class PublishCarUseCase(UseCasePort):

    def __init__(self, car_repo: CarRepo):
        self.car_repository = car_repo

    async def execute(self, car: Car):
        return await self.car_repository.insert(car)
