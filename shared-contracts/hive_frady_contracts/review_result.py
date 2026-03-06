"""
Review result schema emitted by Frady after evidentiary validation.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class ReviewStatus(str, Enum):
    """Possible outcomes of a Frady review."""

    SUPPORTED = "supported"
    MIXED = "mixed"
    WEAK = "weak"
    NOT_READY = "not_ready"


@dataclass
class FradyReviewResult:
    """
    Output contract emitted by Frady after completing evidentiary review.

    Consumed by super-duper-spork for final case state transitions.
    """

    case_id: str
    review_status: ReviewStatus = ReviewStatus.NOT_READY
    validated_tells: list[dict[str, Any]] = field(default_factory=list)
    rejected_tells: list[dict[str, Any]] = field(default_factory=list)
    missing_evidence: list[str] = field(default_factory=list)
    litigation_risk_notes: list[str] = field(default_factory=list)
    sec_readiness_score: float = 0.0
    recommended_next_steps: list[str] = field(default_factory=list)
    review_provenance: list[dict[str, Any]] = field(default_factory=list)
