from contextlib import asynccontextmanager

import boto3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from internal import settings as sett
from internal.api.v1 import api_v1_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Выполняется перед стартом и завершением работы приложения."""
    # Подключение к сторонним приложениям
    session = boto3.session.Session()
    s3 = session.client(
        service_name=sett.SERVICE_NAME,
        region_name=sett.REGION_NAME,
        endpoint_url=sett.ENDPOINT_URL,
        aws_access_key_id=sett.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=sett.AWS_SECRET_ACCESS_KEY,
    )

    # Передача управления приложению с прокидыванием
    # зависимостей в Request.state.<ключ словаря>
    yield {"s3": s3}


app: FastAPI = FastAPI(title="Media-ms", lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Подключение роутов
app.include_router(api_v1_router)
