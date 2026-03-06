"""
SEC EDGAR connector – retrieves filings and entity data from SEC EDGAR.

Exposes raw source records with provenance metadata.
All responses include retrieved_at timestamp and confidence fields.
"""

from __future__ import annotations

from typing import Any


def get_filings(entity_name: str, cik: str = "") -> list[dict[str, Any]]:
    """
    Retrieve SEC EDGAR filings for the specified entity.

    Args:
        entity_name: Registered name of the entity.
        cik: Optional CIK number to target retrieval directly.

    Returns:
        List of filing records with provenance metadata attached.
    """
    raise NotImplementedError("sec_edgar.get_filings() not yet implemented")


def search_entity(query: str) -> list[dict[str, Any]]:
    """
    Search EDGAR full-text search for the given query string.

    Returns a list of matching entity and filing summary records.
    """
    raise NotImplementedError("sec_edgar.search_entity() not yet implemented")
