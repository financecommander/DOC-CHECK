"""
Tell validator – validates or downgrades tells from a HiveCasePacket.
"""

from __future__ import annotations

from typing import Any


def validate_tells(
    tells: list[dict[str, Any]],
    evidence_bundle: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """
    Classify each tell as validated or rejected based on available evidence.

    Returns:
        (validated_tells, rejected_tells)
    """
    raise NotImplementedError("validate_tells() not yet implemented")
