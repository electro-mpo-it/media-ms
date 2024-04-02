from fastapi import APIRouter, File, Query, Request, UploadFile

from internal.dto import files as files_dto
from internal.services.files import FilesService

files_router: APIRouter = APIRouter(
    prefix="/files",
    tags=["Файлы"],
)


@files_router.post(
    "/upload",
    response_model=list[files_dto.UploadedIMGDTO],
)
def upload(
    req: Request,
    files: list[UploadFile] = File(),
    entity: files_dto.EntityENUM = Query(),
    unique_name: str = Query(),
):
    """Загружает файл."""
    service: FilesService = FilesService(
        req.state.s3,
        ["image/jpeg", "image/png"],
    )
    res = service.upload_images(files, entity, unique_name)

    for file in files:
        file.file.close()

    return res
