"""
Tell detector – identifies structural, behavioral, and timing tells.

Operates on the aggregated evidence collected by Hive drones.
"""

from __future__ import annotations

from typing import Any

from hive.models.tell import Tell, TellDimension


class TellDetector:
    """
    Detects tells across the three Hive dimensions:
      A / Structural
      B / Behavioral
      C / Timing

    Receives drone results and emits a list of Tell objects.
    """

    def detect(self, evidence: list[dict[str, Any]]) -> list[Tell]:
        """
        Run all tell detectors over the supplied evidence records.

        Returns a deduplicated list of Tell objects with confidence scores.
        """
        tells: list[Tell] = []
        tells.extend(self._detect_structural(evidence))
        tells.extend(self._detect_behavioral(evidence))
        tells.extend(self._detect_timing(evidence))
        return tells

    def _detect_structural(self, evidence: list[dict[str, Any]]) -> list[Tell]:
        """Detect Dimension A / Structural tells."""
        raise NotImplementedError

    def _detect_behavioral(self, evidence: list[dict[str, Any]]) -> list[Tell]:
        """Detect Dimension B / Behavioral tells."""
        raise NotImplementedError

    def _detect_timing(self, evidence: list[dict[str, Any]]) -> list[Tell]:
        """Detect Dimension C / Timing tells."""
        raise NotImplementedError
