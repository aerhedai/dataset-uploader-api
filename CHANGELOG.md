# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-08-05

### 🎉 Initial Release

#### Added
- Initial implementation of the Dataset Uploader API.
- Endpoint to upload datasets in `.csv`, `.json`, `.xlsx`, and `.parquet` formats.
- File validation for supported extensions and file size.
- File saving to a local directory (`uploads/`).
- Automatic directory creation if it does not exist.
- Config management via Pydantic settings (migrated to `pydantic-settings`).
- Logging setup for successful and failed uploads.
- API documentation with automatic schema generation via FastAPI.

---

> Future versions will include enhancements like database support, authentication, advanced logging, environment-based configuration, and more.

