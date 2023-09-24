from src.adapters.repos.car import CarRepo
from src.domain.entities.car import Car
from src.domain.ports.use_case import UseCasePort
from src.infra.schemas.car import CarModel


class PublishCarUseCase(UseCasePort):

    def __init__(self, car_repo: CarRepo):
        self.car_repository = car_repo

    async def execute(self, car_model: CarModel):
        car = Car(**car_model.model_dump())
        return await self.car_repository.insert(car)
