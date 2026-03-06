"""
Source provenance schema for tracking where data originated.

All source adapters must attach provenance to every retrieved record.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class SourceProvenance:
    """
    Records the origin and retrieval context for a data record.

    Required fields for all source adapters:
    - source: adapter name (e.g. "sec_edgar", "delaware_sos")
    - retrieved_at: ISO-8601 timestamp of retrieval
    - confidence: adapter-level confidence in the record (0.0–1.0)
    - error: non-empty string if retrieval encountered an error
    """

    source: str
    retrieved_at: str
    confidence: float = 1.0
    error: str = ""
    raw_response_ref: str = ""
    extra: dict[str, Any] = field(default_factory=dict)
