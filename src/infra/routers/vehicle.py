from fastapi import APIRouter, Depends

from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.use_cases.publish_vehicle import PublishVehicleUseCase
from src.infra.dependencies import publish_vehicle_use_case

router = APIRouter()


@router.post(
    "/publish",
    response_model=dict[str, str],
)
async def publish(
        vehicle_model: VehiclePublication,
        use_case: PublishVehicleUseCase = Depends(publish_vehicle_use_case),
):
    await use_case.execute(vehicle_model)
    return {"message": "Vehicle published successfully"}
