"""
Hive ↔ Frady router – decides escalation and routes cases between layers.
"""

from __future__ import annotations

from typing import Any

# Default escalation thresholds (configurable).
MIN_DATA_COMPLETENESS = 0.70
MIN_DIMENSIONS_ACTIVE = 2
ESCALATION_TIERS = {"elevated", "high", "critical"}


def should_escalate_to_frady(hive_packet: dict[str, Any]) -> bool:
    """
    Return True when a HiveCasePacket meets escalation criteria:

    - risk_tier is elevated, high, or critical
    - at least two tell dimensions are active
    - data_completeness >= MIN_DATA_COMPLETENESS
    - at least one documentary evidence path exists
    """
    profile = hive_packet.get("firm_profile", {})
    tier = profile.get("risk_tier", "low")
    if tier not in ESCALATION_TIERS:
        return False

    active_dims = profile.get("active_dimensions", [])
    if len(active_dims) < MIN_DIMENSIONS_ACTIVE:
        return False

    if hive_packet.get("data_completeness", 0.0) < MIN_DATA_COMPLETENESS:
        return False

    if not hive_packet.get("evidence_bundle"):
        return False

    return True


def route_hive_case(hive_packet: dict[str, Any]) -> str:
    """
    Route a completed HiveCasePacket to the appropriate next step.

    Returns:
        "escalate"  – send to Frady review
        "watchlist" – retain at elevated watch, insufficient for Frady
        "close"     – insufficient evidence, close case
    """
    if should_escalate_to_frady(hive_packet):
        return "escalate"

    profile = hive_packet.get("firm_profile", {})
    tier = profile.get("risk_tier", "low")
    if tier in {"moderate", "elevated"}:
        return "watchlist"

    return "close"


def run_challenge_swarm(hive_packet: dict[str, Any]) -> dict[str, Any]:
    """
    Invoke the challenge swarm to attempt falsification of top tells.

    Returns a challenge report dict with:
    - challenged_tells: list of tell_ids that survived challenge
    - rejected_tells: list of tell_ids invalidated by challenge
    - downgrade_recommended: bool
    """
    raise NotImplementedError("run_challenge_swarm() not yet implemented")


def finalize_case_state(
    hive_packet: dict[str, Any],
    frady_result: dict[str, Any] | None,
) -> dict[str, Any]:
    """
    Write the final auditable case state record.

    Logs all mandatory fields required by the logging policy:
    task_id, source, target_entity, drone/swarm role, confidence,
    evidence references, score delta, escalation decision, reviewer outcome.
    """
    raise NotImplementedError("finalize_case_state() not yet implemented")
