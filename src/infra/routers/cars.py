from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import Container
from src.domain.entities.car import Car
from src.domain.ports.use_case import UseCasePort

router = APIRouter()


@router.post(
    "/publish",
    response_model=dict[str, str],
)
@inject
async def publish_car(
        car_model: Car,
        publish_car_use_case: UseCasePort = Depends(Provide[Container.publish_car_use_case]),
):
    await publish_car_use_case.execute(car_model)
    return {"message": "Car published successfully"}
