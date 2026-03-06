"""
News and court connector – retrieves PACER filings and news records.

Exposes raw source records with provenance metadata.
"""

from __future__ import annotations

from typing import Any


def search_court_filings(entity_name: str) -> list[dict[str, Any]]:
    """
    Search PACER for court filings involving the named entity.

    Returns a list of docket records with provenance metadata.
    """
    raise NotImplementedError("news_court.search_court_filings() not yet implemented")


def search_news(entity_name: str, date_from: str = "", date_to: str = "") -> list[dict[str, Any]]:
    """
    Search news sources for coverage of the named entity.

    Returns a list of news article records with provenance metadata.
    """
    raise NotImplementedError("news_court.search_news() not yet implemented")
