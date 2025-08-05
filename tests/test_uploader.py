from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_upload_csv(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    response = client.post("/upload", files={"file": ("test.csv", "col1,col2\n1,2", "text/csv")})
    assert response.status_code == 200
    json_data = response.json()
    assert "file_id" in json_data and json_data["filename"] == "test.csv"