"""
Evidence reference schema for linking findings to source documents.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class EvidenceRef:
    """
    Points to a single piece of evidence within a case packet or review result.

    All evidence must be provenance-linked to a source adapter retrieval.
    """

    evidence_id: str
    source: str
    document_url: str = ""
    document_title: str = ""
    excerpt: str = ""
    retrieved_at: str = ""
    confidence: float = 0.0
    tags: list[str] = field(default_factory=list)
    raw_ref: dict[str, Any] = field(default_factory=dict)
