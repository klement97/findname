from typing import Annotated

from fastapi import APIRouter, Depends

from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.use_cases.vehicle.publish_vehicle import PublishVehicleUseCase
from src.infra import dependencies as deps
from src.infra.dependencies import publish_vehicle_use_case

router = APIRouter()


@router.post(
    "/publication",
    response_model=dict[str, str],
)
async def publish(
        _: Annotated[str, Depends(deps.oauth2_scheme)],
        vehicle_model: VehiclePublication,
        use_case: PublishVehicleUseCase = Depends(publish_vehicle_use_case),
):
    await use_case.execute(vehicle_model)
    return {"message": "Vehicle published successfully"}
