from enum import Enum

from pydantic import BaseModel, HttpUrl


class EntityENUM(str, Enum):
    """Перечисление сущностей, к которым загружается изображение."""

    CATEGORY = "category"
    PRODUCT = "product"
    OTHER = "other"


class UploadedIMGDTO(BaseModel):
    """Данные загруженного изображения."""

    filename: str
    img_url: HttpUrl
