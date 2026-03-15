from pydantic import BaseModel
from typing import Dict, Any, Optional

class DocumentMetadata(BaseModel):
    page_count: Optional[int] = None
    paragraph_count: Optional[int] = None
    title: Optional[str] = None

class Document(BaseModel):
    content: str
    metadata: DocumentMetadata
    doc_type: str

class AnalysisReport(BaseModel):
    analysis_id: str
    document: Document
    classification: Dict[str, Any]
    red_flags: Optional[Dict[str, Any]] = None
    risk_factors: Optional[Dict[str, Any]] = None
