from pydantic import BaseModel
from typing import Dict, Any, List

class DocumentMetadata(BaseModel):
    page_count: int = 0
    title: str = ""
    paragraph_count: int = 0

class AnalysisResult(BaseModel):
    id: str
    status: str
    report: Dict[str, Any]

class ComparisonResult(BaseModel):
    comparison_id: str
    changes: List[Dict[str, Any]]
    status: str
