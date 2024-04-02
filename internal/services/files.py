import uuid
from typing import NoReturn

from fastapi import HTTPException, UploadFile, status

from internal.dto import files as files_dto
from internal.settings import BUCKET_NAME


class FilesService:
    """Файловый сервис."""

    def __init__(self, s3, allowed_cts: list[str]):
        self.s3 = s3
        self.allowed_cts: list[str] = allowed_cts

    def upload_images(
        self, files: list[UploadFile], entity: files_dto.EntityENUM, unique_name: str
    ) -> list[files_dto.UploadedIMGDTO]:
        """Загружает изображения, следом возвращает ссылки на них."""

        # Сначала валидация всех изображений.
        for file in files:
            self._validate_image(file)

        uploaded: list[files_dto.UploadedIMGDTO] = []

        for file in files:
            uri: str = (
                f'{entity.value}/{unique_name}/{uuid.uuid4()}'
                f'.{file.filename.split(".")[-1]}'
            )

            self.s3.put_object(
                Bucket=BUCKET_NAME,
                Key=uri,
                Body=file.file.read(),
            )

            uploaded.append(
                files_dto.UploadedIMGDTO(
                    filename=file.filename,
                    img_url=f"https://storage.yandexcloud.net/{BUCKET_NAME}/{uri}",
                ),
            )

        return uploaded

    def _validate_image(self, file: UploadFile) -> NoReturn:
        """Валидирует изображение, выбрасывает ошибку."""

        if file.content_type not in self.allowed_cts:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=(
                    f"invalid file ({file.filename}). "
                    f"allowed content-types -> {self.allowed_cts}"
                ),
            )
