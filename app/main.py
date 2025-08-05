from fastapi import FastAPI
from app.api import routes

app = FastAPI(
    title="Dataset Uploader API",
    description="Upload and manage datasets for further processing.",
    version="0.1.0"
)

app.include_router(routes.router)

@app.get("/health")
def health():
    return {"status": "ok"}
