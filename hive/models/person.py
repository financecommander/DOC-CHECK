"""
Person data model for the Hive detection engine.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Person:
    """Represents an individual associated with one or more entities."""

    person_id: str
    full_name: str
    roles: list[str] = field(default_factory=list)
    affiliated_entities: list[str] = field(default_factory=list)
    attributes: dict[str, Any] = field(default_factory=dict)
