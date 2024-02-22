from fastapi import APIRouter, Depends

from src.domain.entities.auth import SignupData, LoginData
from src.domain.use_cases.login import LoginUseCase
from src.domain.use_cases.signup import SignupUseCase
from src.infra.dependencies import get_signup_use_case, get_login_use_case

router = APIRouter(prefix="/auth")


@router.post("/signup")
async def signup(
        signup_data: SignupData,
        use_case: SignupUseCase = Depends(get_signup_use_case)
):
    await use_case.execute(signup_data)
    return {"status": "success"}


@router.post("/login")
async def login(
        login_data: LoginData,
        use_case: LoginUseCase = Depends(get_login_use_case)
):
    return await use_case.execute(login_data)
