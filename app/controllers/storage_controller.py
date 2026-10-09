import logging
from fastapi import APIRouter, HTTPException
from minio.error import S3Error
from app.models.payload import DownloadResponse, UploadFilesRequest, DownloadRequest, UploadFilesResponse
from app.services.storage_service import storage_service

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/storage")

@router.post("/upload", response_model=UploadFilesResponse)
def upload_to_minio(payload: UploadFilesRequest):
    try:
        uploaded = storage_service.upload_file_batch(
            payload.bucket_name,
            payload.object_name,
            payload.local_file_paths
        )
        return UploadFilesResponse(
            file_paths=uploaded
        )
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Upload error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/download", response_model=DownloadResponse)
def download_from_minio(payload: DownloadRequest):
    try:
        local_path = storage_service.download_file(
            payload.bucket_name,
            payload.object_name,
            payload.destination_folder
        )
        return DownloadResponse(
            file_path=local_path
        )
    except S3Error as e:
        if e.code == "NoSuchKey":
            raise HTTPException(status_code=404, detail=f"Object not found in MinIO: {payload.object_name}")
        raise HTTPException(status_code=502, detail=f"MinIO Storage Error: {e.message}")
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        logger.error(f"*** Download error: {e}")
        raise HTTPException(status_code=500, detail=str(e))