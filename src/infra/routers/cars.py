from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from src.containers import Container
from src.domain.ports.use_case import UseCasePort
from src.infra.schemas.car import CarModel

router = APIRouter()


@router.post("/publish_car")
@inject
async def publish_car(
        car_model: CarModel,
        publish_car_use_case: UseCasePort = Depends(Provide[Container.publish_car_use_case]),
):
    await publish_car_use_case.execute(car_model)
    return {"message": "Car published successfully"}
