from src.adapters.repos.vehicle import VehicleRepo
from src.domain.entities.vehiclepublication import VehiclePublication
from src.domain.ports.use_case import UseCasePort


class PublishVehicleUseCase(UseCasePort):

    def __init__(self, vehicle_repo: VehicleRepo):
        self.vehicle_repository = vehicle_repo

    async def execute(self, vp: VehiclePublication):
        return await self.vehicle_repository.insert(vp)
