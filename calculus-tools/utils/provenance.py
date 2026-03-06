"""
Provenance utilities – attach and validate source provenance metadata.

All source adapters must call attach_provenance() before returning records.
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any


def attach_provenance(
    record: dict[str, Any],
    source: str,
    confidence: float = 1.0,
    raw_response_ref: str = "",
    error: str = "",
) -> dict[str, Any]:
    """
    Attach provenance metadata to a raw source record in-place.

    Adds:
    - _provenance.source
    - _provenance.retrieved_at (UTC ISO-8601)
    - _provenance.confidence
    - _provenance.raw_response_ref (when available)
    - _provenance.error (when retrieval encountered an error)
    """
    record["_provenance"] = {
        "source": source,
        "retrieved_at": datetime.now(tz=timezone.utc).isoformat(),
        "confidence": confidence,
        "raw_response_ref": raw_response_ref,
        "error": error,
    }
    return record


def validate_provenance(record: dict[str, Any]) -> bool:
    """Return True if the record carries valid provenance metadata."""
    prov = record.get("_provenance", {})
    return bool(prov.get("source") and prov.get("retrieved_at"))
