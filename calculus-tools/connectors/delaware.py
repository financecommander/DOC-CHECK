"""
Delaware SOS connector – retrieves entity registration data from Delaware.

Exposes raw source records with provenance metadata.
"""

from __future__ import annotations

from typing import Any


def lookup_entity(entity_name: str) -> list[dict[str, Any]]:
    """
    Look up Delaware Secretary of State registration records for an entity.

    Returns a list of registration records with provenance metadata.
    """
    raise NotImplementedError("delaware.lookup_entity() not yet implemented")
