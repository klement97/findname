from typing import Annotated

from fastapi import APIRouter, Depends

from src.domain.entities.vehicle_publication import VehiclePublication
from src.domain.ports.repo import VehicleRepoPort
from src.infra import dependencies as deps

router = APIRouter()


@router.get(
    "/publication",
    response_model=list[VehiclePublication],
)
async def get_my_publications(
        email: Annotated[str, Depends(deps.get_current_user_email)],
        repo: Annotated[VehicleRepoPort, Depends(deps.vehicle_repo)],
):
    return await repo.get(email)
