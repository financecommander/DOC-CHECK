"""
Risk profile data model for the Hive detection engine.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class RiskTier(str, Enum):
    LOW = "low"
    MODERATE = "moderate"
    ELEVATED = "elevated"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class FirmRiskProfile:
    """
    Normalized risk profile for a PE firm produced by Hive scoring.

    risk_score is normalized to a 0–100 scale with convergence weighting
    when signals appear across multiple tell dimensions.
    """

    firm_id: str
    firm_name: str
    risk_score: float = 0.0
    risk_tier: RiskTier = RiskTier.LOW
    active_dimensions: list[str] = field(default_factory=list)
    tell_summary: list[dict[str, Any]] = field(default_factory=list)
    data_completeness: float = 0.0
