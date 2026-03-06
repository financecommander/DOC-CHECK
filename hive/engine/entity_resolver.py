"""
Entity resolver – deduplicates and normalizes entities across drone results.

Merges records referring to the same firm or person, assigns canonical IDs,
and builds the entity map and alias index.
"""

from __future__ import annotations

from typing import Any

from hive.models.entity import Entity


class EntityResolver:
    """
    Deduplicates entity records collected from multiple drones.

    Outputs a canonical entity map keyed by entity_id.
    """

    def resolve(self, raw_records: list[dict[str, Any]]) -> dict[str, Entity]:
        """
        Merge and deduplicate raw entity records into a canonical map.

        Returns a dict mapping entity_id → Entity.
        """
        raise NotImplementedError("EntityResolver.resolve() not yet implemented")
