import os
import uuid
from fastapi import UploadFile
from app.core.config import settings
from app.utils.logging import logger

async def handle_upload(file: UploadFile) -> str:
    ext = os.path.splitext(file.filename)[1]
    uid = uuid.uuid4().hex
    filename = f"{uid}{ext}"
    os.makedirs(settings.DATA_DIR, exist_ok=True)
    dest = os.path.join(settings.DATA_DIR, filename)
    logger.info(f"Saving file to {dest}")
    with open(dest, "wb") as f:
        content = await file.read()
        f.write(content)
    return uid
