"""
Case state machine – manages lifecycle state transitions for investigative cases.
"""

from __future__ import annotations

import sys
import os

# Allow importing from shared-contracts without installation.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "shared-contracts"))

from hive_frady_contracts.case_packet import CaseState  # noqa: E402


# Valid transitions: state → set of allowed next states
TRANSITIONS: dict[CaseState, set[CaseState]] = {
    CaseState.NEW: {CaseState.SCREENING},
    CaseState.SCREENING: {CaseState.HIVE_COMPLETE, CaseState.CLOSED},
    CaseState.HIVE_COMPLETE: {CaseState.ESCALATED, CaseState.CHALLENGE, CaseState.CLOSED},
    CaseState.CHALLENGE: {CaseState.ESCALATED, CaseState.DOWNGRADED, CaseState.CLOSED},
    CaseState.ESCALATED: {CaseState.FRADY_REVIEW},
    CaseState.FRADY_REVIEW: {CaseState.VALIDATED, CaseState.DOWNGRADED, CaseState.CLOSED},
    CaseState.VALIDATED: {CaseState.CLOSED},
    CaseState.DOWNGRADED: {CaseState.CLOSED},
    CaseState.CLOSED: set(),
}


def transition(current: CaseState, next_state: CaseState) -> CaseState:
    """
    Validate and apply a state transition.

    Raises ValueError if the transition is not permitted.
    """
    allowed = TRANSITIONS.get(current, set())
    if next_state not in allowed:
        raise ValueError(
            f"Invalid state transition: {current!r} → {next_state!r}. "
            f"Allowed: {sorted(s.value for s in allowed)}"
        )
    return next_state
