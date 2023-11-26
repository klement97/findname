from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import Container
from src.domain.entities.vehiclepublication import VehiclePublication
from src.domain.ports.use_case import UseCasePort

router = APIRouter()


@router.post(
    "/publish",
    response_model=dict[str, str],
)
@inject
async def publish(
        vehicle_model: VehiclePublication,
        publish_vehicle_use_case: UseCasePort = Depends(Provide[Container.publish_vehicle_use_case]),
):
    await publish_vehicle_use_case.execute(vehicle_model)
    return {"message": "Vehicle published successfully"}
