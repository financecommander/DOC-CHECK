"""
Hive packet intake – validates and ingests a HiveCasePacket for Frady review.
"""

from __future__ import annotations

from typing import Any

# Minimum data completeness required before Frady will accept a packet.
MIN_DATA_COMPLETENESS = 0.70


def ingest_hive_packet(packet: dict[str, Any]) -> dict[str, Any]:
    """
    Validate a HiveCasePacket and prepare it for Frady review.

    Raises ValueError if the packet fails intake validation:
    - required fields must be present
    - data_completeness must meet minimum threshold
    - at least one tell must be present

    Returns the normalised packet ready for downstream review steps.
    """
    _validate_packet(packet)
    return packet


def _validate_packet(packet: dict[str, Any]) -> None:
    required = {"case_id", "firm_profile", "top_tells", "evidence_bundle", "data_completeness"}
    missing = required - set(packet.keys())
    if missing:
        raise ValueError(f"HiveCasePacket missing required fields: {missing}")

    if packet.get("data_completeness", 0.0) < MIN_DATA_COMPLETENESS:
        raise ValueError(
            f"data_completeness {packet['data_completeness']} below minimum {MIN_DATA_COMPLETENESS}"
        )

    if not packet.get("top_tells"):
        raise ValueError("HiveCasePacket contains no tells to review")
