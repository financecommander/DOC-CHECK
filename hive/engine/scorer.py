"""
Scorer – computes composite risk scores for Hive detection results.

Normalizes scores to a 0–100 scale and applies convergence weighting
when signals appear across multiple tell dimensions.
"""

from __future__ import annotations

from hive.models.risk_profile import FirmRiskProfile, RiskTier
from hive.models.tell import Tell, TellDimension

# Default convergence bonus applied when >= 2 dimensions are active.
CONVERGENCE_BONUS = 10.0

TIER_THRESHOLDS = {
    RiskTier.CRITICAL: 80.0,
    RiskTier.HIGH: 60.0,
    RiskTier.ELEVATED: 40.0,
    RiskTier.MODERATE: 20.0,
    RiskTier.LOW: 0.0,
}


def compute_risk_score(tells: list[Tell], data_completeness: float) -> float:
    """
    Compute a normalized 0–100 composite risk score from detected tells.

    Applies a convergence bonus when signals span multiple tell dimensions.
    Scales raw score by data_completeness to penalize incomplete evidence sets.
    """
    if not tells:
        return 0.0

    raw = sum(t.confidence for t in tells)
    active_dimensions = {t.dimension for t in tells}
    if len(active_dimensions) >= 2:
        raw += CONVERGENCE_BONUS

    # Each tell contributes its confidence score (expected range 0.0–10.0 per tell).
    # Multiplying by 10.0 maps a maximum raw score of 10.0 (one perfect tell)
    # to the 0–100 normalized scale.  Scores above 100 are capped.
    normalized = min(raw * 10.0, 100.0)
    return round(normalized * data_completeness, 2)


def assign_risk_tier(score: float) -> RiskTier:
    """Map a numeric risk score to its corresponding RiskTier."""
    for tier in (RiskTier.CRITICAL, RiskTier.HIGH, RiskTier.ELEVATED, RiskTier.MODERATE):
        if score >= TIER_THRESHOLDS[tier]:
            return tier
    return RiskTier.LOW


def build_risk_profile(
    firm_id: str,
    firm_name: str,
    tells: list[Tell],
    data_completeness: float,
) -> FirmRiskProfile:
    """Build a FirmRiskProfile from detected tells and completeness score."""
    score = compute_risk_score(tells, data_completeness)
    tier = assign_risk_tier(score)
    active_dims = sorted({t.dimension.value for t in tells})
    return FirmRiskProfile(
        firm_id=firm_id,
        firm_name=firm_name,
        risk_score=score,
        risk_tier=tier,
        active_dimensions=active_dims,
        tell_summary=[
            {"tell_id": t.tell_id, "dimension": t.dimension.value, "confidence": t.confidence}
            for t in tells
        ],
        data_completeness=data_completeness,
    )
