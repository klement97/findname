from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from src.domain.entities.auth import SignupData, LoginData
from src.domain.use_cases.auth.login import LoginUseCase
from src.domain.use_cases.auth.read_user_info import ReadUserInfoUseCase
from src.domain.use_cases.auth.signup import SignupUseCase
from src.infra import dependencies as deps

router = APIRouter()


@router.post("/signup")
async def signup(
        signup_data: SignupData,
        use_case: SignupUseCase = Depends(deps.signup_use_case)
):
    await use_case.execute(signup_data)
    return {"status": "success"}


@router.post("/login")
async def login(
        login_data: LoginData,
        use_case: LoginUseCase = Depends(deps.login_use_case)
):
    return await use_case.execute(login_data)


@router.post("/login-form")
async def login_form(
        login_form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm),
        use_case: LoginUseCase = Depends(deps.login_use_case)
):
    return await use_case.execute(
        LoginData(
            email=login_form_data.username,
            password=login_form_data.password,
        )
    )


@router.get("/me")
async def me(
        use_case: ReadUserInfoUseCase = Depends(deps.read_user_info_use_case),
        email: str = Depends(deps.get_current_user_email)
):
    return await use_case.execute(email)
