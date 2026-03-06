"""
Case packet schemas and state models shared between Hive and Frady.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class CaseState(str, Enum):
    """Lifecycle states for an investigative case."""

    NEW = "new"
    SCREENING = "screening"
    HIVE_COMPLETE = "hive_complete"
    ESCALATED = "escalated"
    CHALLENGE = "challenge"
    FRADY_REVIEW = "frady_review"
    VALIDATED = "validated"
    DOWNGRADED = "downgraded"
    CLOSED = "closed"


@dataclass
class HiveCasePacket:
    """
    Output contract emitted by Hive after completing firm-level detection.

    Consumed by super-duper-spork escalation logic and by Frady intake.
    """

    case_id: str
    firm_profile: dict[str, Any] = field(default_factory=dict)
    top_tells: list[dict[str, Any]] = field(default_factory=list)
    entity_map: dict[str, Any] = field(default_factory=dict)
    personnel_graph: dict[str, Any] = field(default_factory=dict)
    timeline: list[dict[str, Any]] = field(default_factory=list)
    evidence_bundle: list[dict[str, Any]] = field(default_factory=list)
    data_completeness: float = 0.0
    open_questions: list[str] = field(default_factory=list)
    provenance_index: list[dict[str, Any]] = field(default_factory=list)
