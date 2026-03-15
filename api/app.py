from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import Dict, Any
import os
import asyncio

from hive.pipeline import DocumentPipeline

app = FastAPI(title="DOC-CHECK API")

pipeline = DocumentPipeline()

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)) -> Dict[str, Any]:
    """
    Analyze an uploaded document.
    """
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())
    
    doc_type = file.filename.split('.')[-1].lower()
    try:
        result = await pipeline.run_pipeline(temp_path, doc_type)
        return result
    finally:
        os.remove(temp_path)

@app.get("/report/{id}")
async def get_report(id: str):
    """
    Retrieve a report by ID.
    TODO: Implement storage and retrieval logic.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@app.post("/compare")
async def compare_documents(files: list[UploadFile] = File(...)):
    """
    Compare multiple documents.
    TODO: Implement comparison logic.
    """
    raise HTTPException(status_code=501, detail="Not implemented")

@app.get("/status/{id}")
async def get_status(id: str):
    """
    Get status of an analysis by ID.
    TODO: Implement status tracking.
    """
    raise HTTPException(status_code=501, detail="Not implemented")
