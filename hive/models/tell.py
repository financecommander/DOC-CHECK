"""
Tell data model for the Hive detection engine.

Tells are classified along three dimensions:
  A / Structural
  B / Behavioral
  C / Timing
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class TellDimension(str, Enum):
    STRUCTURAL = "A"
    BEHAVIORAL = "B"
    TIMING = "C"


@dataclass
class Tell:
    """A single detected indicator of potential misconduct."""

    tell_id: str
    dimension: TellDimension
    description: str
    evidence_refs: list[str] = field(default_factory=list)
    confidence: float = 0.0
    attributes: dict[str, Any] = field(default_factory=dict)
