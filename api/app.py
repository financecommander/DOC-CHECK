from fastapi import FastAPI, HTTPException, UploadFile, File
from typing import Dict, Any
import asyncio
import os

from hive.pipeline import Pipeline

app = FastAPI(title="DOC-CHECK API")

pipeline = Pipeline()

@app.post("/analyze")
async def analyze_document(file: UploadFile = File(...)):
    """Analyze an uploaded document."""
    temp_path = f"/tmp/{file.filename}"
    with open(temp_path, "wb") as buffer:
        buffer.write(await file.read())
    
    doc_type = file.filename.split('.')[-1].lower()
    try:
        result = await pipeline.run(temp_path, doc_type)
        os.remove(temp_path)
        return result
    except Exception as e:
        os.remove(temp_path) if os.path.exists(temp_path) else None
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/report/{id}")
async def get_report(id: str):
    """Get analysis report by ID."""
    # TODO: Implement database lookup for report
    return {"id": id, "status": "not_implemented"}

@app.post("/compare")
async def compare_documents(data: Dict[str, Any]):
    """Compare two documents for changes."""
    # TODO: Implement comparison logic
    return {"status": "not_implemented"}

@app.get("/status/{id}")
async def get_status(id: str):
    """Get processing status by ID."""
    # TODO: Implement status tracking
    return {"id": id, "status": "not_implemented"}
