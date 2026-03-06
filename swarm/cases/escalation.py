"""
Escalation rules – encapsulates configurable thresholds for Hive → Frady routing.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class EscalationConfig:
    """Configurable thresholds for case escalation decisions."""

    min_data_completeness: float = 0.70
    min_dimensions_active: int = 2
    escalation_tiers: frozenset[str] = frozenset({"elevated", "high", "critical"})


def meets_escalation_criteria(packet: dict[str, Any], config: EscalationConfig | None = None) -> bool:
    """
    Return True when a HiveCasePacket satisfies all escalation thresholds.

    Evaluates:
    - risk_tier against escalation_tiers
    - active tell dimension count against min_dimensions_active
    - data_completeness against min_data_completeness
    - presence of at least one evidence record
    """
    cfg = config or EscalationConfig()
    profile = packet.get("firm_profile", {})

    if profile.get("risk_tier", "low") not in cfg.escalation_tiers:
        return False

    if len(profile.get("active_dimensions", [])) < cfg.min_dimensions_active:
        return False

    if packet.get("data_completeness", 0.0) < cfg.min_data_completeness:
        return False

    if not packet.get("evidence_bundle"):
        return False

    return True
