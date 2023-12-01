from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import Container
from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.use_cases.publish_vehicle import PublishVehicleUseCase

router = APIRouter()


@router.post(
    "/publish",
    response_model=dict[str, str],
)
@inject
async def publish(
    vehicle_model: VehiclePublication,
    publish_vehicle_use_case: PublishVehicleUseCase = Depends(
        Provide[Container.publish_vehicle_use_case]
    ),
):
    await publish_vehicle_use_case.execute(vehicle_model)
    return {"message": "Vehicle published successfully"}
