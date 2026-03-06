"""
Base drone task/result contract.

All Hive drones must implement this interface so the Queen Bee can
dispatch and collect results uniformly.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class DroneTask:
    """Describes work to be performed by a single drone."""

    task_id: str
    drone_name: str
    target_entity: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass
class DroneResult:
    """Result returned by a drone after completing a task."""

    task_id: str
    drone_name: str
    success: bool
    records: list[dict[str, Any]] = field(default_factory=list)
    confidence: float = 0.0
    error: str = ""
    provenance: dict[str, Any] = field(default_factory=dict)
