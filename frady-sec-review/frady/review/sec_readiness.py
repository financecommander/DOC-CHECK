"""
SEC-readiness scorer – assesses whether a case meets evidentiary standards
sufficient to support a whistleblower or regulatory filing.
"""

from __future__ import annotations

from typing import Any

# Minimum validated-tell count and score to be considered SEC-ready.
SEC_READY_MIN_TELLS = 2
SEC_READY_MIN_SCORE = 0.65


def score_sec_readiness(
    validated_tells: list[dict[str, Any]],
    evidence_bundle: list[dict[str, Any]],
    missing_evidence: list[str],
) -> float:
    """
    Compute a 0.0–1.0 SEC-readiness score.

    Considers validated tell count, evidence quality, and missing evidence gaps.
    Returns 0.0 if the case does not meet minimum readiness thresholds.
    """
    raise NotImplementedError("score_sec_readiness() not yet implemented")
