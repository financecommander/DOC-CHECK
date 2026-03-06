"""
Enforcement connector – retrieves DOJ, FDA, and state enforcement actions.

Exposes raw source records with provenance metadata.
"""

from __future__ import annotations

from typing import Any


def search_actions(entity_name: str, sources: list[str] | None = None) -> list[dict[str, Any]]:
    """
    Search enforcement databases for actions involving the named entity.

    Args:
        entity_name: Target entity or individual name.
        sources: Optional list of source IDs to query (default: all configured).

    Returns:
        List of enforcement action records with provenance metadata.
    """
    raise NotImplementedError("enforcement.search_actions() not yet implemented")
