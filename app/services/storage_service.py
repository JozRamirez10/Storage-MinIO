import os
import logging
import concurrent.futures
from typing import Optional
from minio import Minio
from minio.error import S3Error

from app.core.config import MINIO_ACCESS_KEY, MINIO_ENDPOINT, MINIO_SECRET_KEY, MINIO_SECURE, TMP_DIR

logger = logging.getLogger(__name__)

class StorageService:

    def __init__(self):
        self.client = Minio(
            MINIO_ENDPOINT,
            access_key=MINIO_ACCESS_KEY,
            secret_key=MINIO_SECRET_KEY,
            secure=MINIO_SECURE
        )
        logger.info(f"*** Storage Service initialized connecting to {MINIO_ENDPOINT}")

    def upload_file_batch(self, bucket_name: str, object_name: str, local_file_paths: list[str]) -> list[str]:
        self._ensure_bucket_exists(bucket_name)
        uploaded_paths = []

        if not object_name.endswith('/'):
            object_name += '/'

        def _upload_single(local_path: str) -> Optional[str]:
            abs_path = self._validate_local_path(local_path)

            if not os.path.exists(abs_path):
                logger.warning(f"Local file not found: {abs_path}")
                return None

            file_name = os.path.basename(abs_path)
            target_object_name = f"{object_name}{file_name}"

            logger.info(f"*** Uploading {abs_path} to {bucket_name}/{target_object_name}")
            self.client.fput_object(bucket_name, target_object_name, abs_path)
            return f"minio://{bucket_name}/{target_object_name}"

        with concurrent.futures.ThreadPoolExecutor() as executor:
            results = executor.map(_upload_single, local_file_paths)

        for res in results:
            if res:
                uploaded_paths.append(res)

        logger.info(f"*** Upload complete!")
        return uploaded_paths

    def download_file(self, bucket_name: str, object_name: str, destination_folder: str) -> str:
        abs_folder = self._validate_local_path(destination_folder)
        os.makedirs(abs_folder, exist_ok=True)

        local_file_path = os.path.join(abs_folder, object_name.split("/")[-1])

        logger.info(f"*** Downloading {bucket_name}/{object_name} to {local_file_path}...")
        self.client.fget_object(bucket_name, object_name, local_file_path)
        logger.info("*** Download complete!")

        return local_file_path

    def _ensure_bucket_exists(self, bucket_name: str):
            try:
                if not self.client.bucket_exists(bucket_name):
                    self.client.make_bucket(bucket_name)
                    logger.info(f"*** Created bucket: {bucket_name}")
            except S3Error as e:
                logger.exception(f"*** Error checking/creating bucket {bucket_name}: {e}")
                raise Exception(f"MinIO Bucket Error: {str(e)}")

    def _validate_local_path(self, path: str):
        abs_path = os.path.abspath(path)
        if not abs_path.startswith(TMP_DIR):
            raise PermissionError(f"Path traversal blocked for: {path}")
        return abs_path

storage_service = StorageService()