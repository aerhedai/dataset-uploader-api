# 📁 Dataset Uploader API

A modular Python-based REST API for uploading datasets in formats such as CSV, JSON, Excel, and Parquet. This API is the first step in a data processing pipeline and is intended to be used in conjunction with other tools or AI agents that perform further analysis, transformation, or modelling.

---

## 🚀 Features

- Upload datasets via HTTP POST requests
- Supported formats: `.csv`, `.json`, `.xlsx`, `.parquet`
- Saves files to a local directory or configurable storage path
- Returns metadata and a reference path to the uploaded file
- Built using FastAPI with automatic Swagger UI documentation

---

## 🏗 Project Structure

```
dataset-uploader-api/
│
├── app/
│   ├── api/
│   │   └── routes.py         # API endpoints
│   ├── core/
│   │   └── config.py         # Settings and environment config
│   ├── services/
│   │   └── uploader.py       # Upload handling logic
│   └── main.py               # Entry point for the app
│
├── uploads/                  # Directory where uploaded datasets are stored
├── .env                      # Environment variable definitions
├── requirements.txt          # Python package dependencies
├── README.md                 # Documentation (this file)
└── run.py                    # Launch script using uvicorn
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/aerhedai/dataset-uploader-api.git
cd dataset-uploader-api
```

### 2. Create & Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If using Pydantic v2, make sure this is installed too:

```bash
pip install pydantic-settings
```

### 4. Set Environment Variables

Create a `.env` file in the root directory:

```env
PROJECT_NAME=Dataset Uploader API
FILE_UPLOAD_DIR=uploads
```

---

## ▶️ Run the API Locally

Use the provided `run.py` script:

```bash
python run.py
```

The API will be available at:

```
http://127.0.0.1:8000
```

Docs available at:

- Swagger UI: `/docs`
- ReDoc: `/redoc`

---

## 📤 Upload Endpoint

### POST `/upload`

Upload a dataset file.

#### Request (multipart/form-data):

```
file: <your_dataset.csv|.json|.xlsx|.parquet>
```

#### Example with `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@/path/to/your/dataset.csv"
```

#### Response:

```json
{
  "filename": "dataset.csv",
  "filepath": "uploads/dataset.csv",
  "message": "File uploaded successfully"
}
```

---

## ✅ Supported File Types

| Extension | Description     |
|-----------|-----------------|
| `.csv`    | Comma-separated values |
| `.json`   | JSON formatted data |
| `.xlsx`   | Excel file |
| `.parquet`| Apache Parquet |

---

## 🔐 Notes

- Ensure the `uploads/` directory exists and is writable.
- File size limits or authentication can be added if needed.
- To integrate cloud storage (like GCP or AWS), modify `uploader.py`.

---

## 🧱 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)
- [Pydantic v2](https://docs.pydantic.dev/)
- [Python 3.9+](https://www.python.org/)

---

## 🧠 Use Cases

This API is ideal for:

- Feeding datasets to machine learning or data science pipelines
- Integrating with AI agents to automate dataset intake
- Modular data apps that require isolated upload functionality

---

## 🏢 Part of the Aerhed AI Tool Suite

This uploader is designed to be part of a suite of modular APIs under the Aerhed AI ecosystem. It can be composed with:

- Data Cleaner API
- Schema Detector API
- Visualiser API
- Model Training API
- and more...

Each API is independent but can be orchestrated by an AI agent for powerful automation.

---

## 📬 Contact

Built by [aerhedai](https://github.com/aerhedai). For questions or collaborations, feel free to reach out via GitHub or add issues/pull requests to this repo.
