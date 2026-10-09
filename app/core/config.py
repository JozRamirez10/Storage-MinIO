import os
from dotenv import load_dotenv

load_dotenv()

MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "")
MINIO_SECURE = os.getenv("MINIO_SECURE", "False").lower() in ("true", "1", "t")

TMP_DIR = os.getenv("TMP_DIR", "")

if not MINIO_ENDPOINT:
    raise ValueError("CRITICAL ERROR: MINIO_ENDPOINT is not defined in the .env file")
if not MINIO_ACCESS_KEY:
    raise ValueError("CRITICAL ERROR: MINIO_ACCESS_KEY is not defined in the .env file")
if not MINIO_SECRET_KEY:
    raise ValueError("CRITICAL ERROR: MINIO_SECRET_KEY is not defined in the .env file")
if not TMP_DIR:
    raise ValueError("CRITICAL ERROR: TMP_DIR is not defined in the .env file")