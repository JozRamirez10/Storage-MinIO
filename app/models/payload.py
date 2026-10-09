from pydantic import BaseModel

class BaseStorageRequest(BaseModel):
    bucket_name: str
    object_name: str

class UploadFilesRequest(BaseStorageRequest):
    local_file_paths: list[str]

class UploadFilesResponse(BaseModel):
    file_paths: list[str]

class DownloadRequest(BaseStorageRequest):
    destination_folder: str

class DownloadResponse(BaseModel):
    file_path: str