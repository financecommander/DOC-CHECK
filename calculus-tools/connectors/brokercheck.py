"""
FINRA BrokerCheck connector – retrieves registration and disciplinary records.

Exposes raw source records with provenance metadata.
"""

from __future__ import annotations

from typing import Any


def search_firm(firm_name: str) -> list[dict[str, Any]]:
    """
    Search FINRA BrokerCheck for a registered investment adviser or broker-dealer.

    Returns a list of firm records with provenance metadata.
    """
    raise NotImplementedError("brokercheck.search_firm() not yet implemented")


def search_individual(full_name: str) -> list[dict[str, Any]]:
    """
    Search FINRA BrokerCheck for an individual registered person.

    Returns a list of individual records with provenance metadata.
    """
    raise NotImplementedError("brokercheck.search_individual() not yet implemented")
