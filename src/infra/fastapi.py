import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from src.infra.routers.auth import router as auth_router
from src.infra.routers.vehicle import router as vehicle_router
from . import settings
from .exception_handling import EXCEPTION_MAP

logging.basicConfig(
    level="INFO",
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

app = FastAPI(
    debug=settings.DEBUG,
    title='My API',
    version=settings.VERSION,
    docs_url='/docs',
)
app.include_router(auth_router, prefix='/auth', tags=['auth'])
app.include_router(vehicle_router, prefix='/vehicle', tags=['vehicle'])


@app.get("/health-check")
async def health_check():
    return {"status": "ok"}


for exception_class, handler in EXCEPTION_MAP.items():
    @app.exception_handler(exception_class)
    async def handle_exception(request, exc, _handler=handler):
        http_exception = _handler(exc)
        content = {'detail': http_exception.detail}
        return JSONResponse(status_code=http_exception.status_code, content=content)
