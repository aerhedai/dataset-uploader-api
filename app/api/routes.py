from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.uploader import handle_upload
from app.models.upload_schema import UploadResponse

router = APIRouter()

@router.post("/upload", response_model=UploadResponse, summary="Upload dataset file")
async def upload_dataset(file: UploadFile = File(...)):
    if file.content_type not in ["text/csv", "application/json", "application/vnd.ms-excel", "application/octet-stream"]:
        raise HTTPException(status_code=415, detail="Unsupported file type")
    file_id = await handle_upload(file)
    return UploadResponse(file_id=file_id, filename=file.filename)
