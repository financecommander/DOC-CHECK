"""
Review memo generator – produces a structured narrative review memo.
"""

from __future__ import annotations

from typing import Any


def generate_review_memo(review_result: dict[str, Any]) -> str:
    """
    Produce a prose review memo from a FradyReviewResult dict.

    The memo includes:
    - summary of validated and rejected tells
    - evidence gaps and litigation risk notes
    - SEC-readiness assessment
    - recommended next steps
    """
    raise NotImplementedError("generate_review_memo() not yet implemented")
