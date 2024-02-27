import logging

from fastapi import FastAPI
from starlette.responses import JSONResponse

from src.infra.routers.write.auth import router as write_auth_router
from src.infra.routers.read.auth import router as read_auth_router
from src.infra.routers.write.vehicle import router as write_vehicle_router
from src.infra.routers.read.vehicle import router as read_vehicle_router
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
app.include_router(read_auth_router, prefix='/auth', tags=['Auth Read Operations'])
app.include_router(write_auth_router, prefix='/auth', tags=['Auth Write Operations'])
app.include_router(read_vehicle_router, prefix='/vehicle', tags=['Vehicle Read Operations'])
app.include_router(write_vehicle_router, prefix='/vehicle', tags=['Vehicle Write Operations'])


@app.get("/health-check")
async def health_check():
    return {"status": "ok"}


for exception_class, handler in EXCEPTION_MAP.items():
    @app.exception_handler(exception_class)
    async def handle_exception(request, exc, _handler=handler):
        http_exception = _handler(exc)
        content = {'detail': http_exception.detail}
        return JSONResponse(status_code=http_exception.status_code, content=content)
