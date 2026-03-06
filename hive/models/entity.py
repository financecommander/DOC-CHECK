"""
Entity data model for the Hive detection engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Entity:
    """Represents a firm, fund, or related legal entity."""

    entity_id: str
    name: str
    entity_type: str = ""
    aliases: list[str] = field(default_factory=list)
    jurisdiction: str = ""
    attributes: dict[str, Any] = field(default_factory=dict)
