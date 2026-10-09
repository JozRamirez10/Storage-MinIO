import logging
from fastapi import FastAPI
import uvicorn
from app.core.constants import FORMAT_LOG
from app.controllers.storage_controller import router as storage_router

logging.basicConfig(
    level=logging.INFO,
    format=FORMAT_LOG
)

app = FastAPI(title="Storage API", version="1.0.0")
app.include_router(storage_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=7003)