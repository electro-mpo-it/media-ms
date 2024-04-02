from fastapi import APIRouter

from .files import files_router

api_v1_router: APIRouter = APIRouter(
    prefix="/api/v1",
)

# Подключение роутов
api_v1_router.include_router(files_router)
