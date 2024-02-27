from dataclasses import asdict
from typing import Annotated

from fastapi import APIRouter, Depends

from src.domain.ports.repo import AuthRepoPort
from src.infra import dependencies as deps
from src.infra.schemas import CurrentUser

router = APIRouter()


@router.get("/me")
async def me(
        repo: Annotated[AuthRepoPort, Depends(deps.auth_repo)],
        email: str = Depends(deps.get_current_user_email),
):
    user = await repo.get(email)
    return CurrentUser(**asdict(user))
