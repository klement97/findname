from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.ports.repo import InsertRepoPort
from src.domain.ports.use_case import UseCasePort


class PublishVehicleUseCase(UseCasePort):

    def __init__(self, vehicle_repo: InsertRepoPort):
        self.vehicle_repo = vehicle_repo

    async def execute(self, vp: VehiclePublication):
        return await self.vehicle_repo.insert(vp)
