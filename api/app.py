from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(title="DOC-CHECK API")

class AnalysisRequest(BaseModel):
    file_path: str
    doc_type: str

@app.post("/analyze")
async def analyze_document(request: AnalysisRequest) -> Dict[str, Any]:
    """Analyze a document via the pipeline."""
    # TODO: Wire up hive.pipeline.Pipeline
    return {"status": "queued", "id": "temp-id-123"}

@app.get("/report/{id}")
async def get_report(id: str) -> Dict[str, Any]:
    """Retrieve analysis report by ID."""
    # TODO: Fetch from database
    return {"id": id, "report": "Analysis complete", "status": "done"}

@app.post("/compare")
async def compare_filings(request: Dict[str, Any]) -> Dict[str, Any]:
    """Compare two filings for material changes."""
    # TODO: Wire up frady-sec-review/comparator.py
    return {"status": "queued", "comparison_id": "comp-456"}

@app.get("/status/{id}")
async def get_status(id: str) -> Dict[str, Any]:
    """Check status of an analysis or comparison."""
    return {"id": id, "status": "in_progress"}
