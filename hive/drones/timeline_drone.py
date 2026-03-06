"""Timeline drone – assembles a chronological event timeline for an entity."""

from hive.drones.base import DroneTask, DroneResult


def run(task: DroneTask) -> DroneResult:
    """
    Build a timeline of key events for task.target_entity from available records.

    Returns a DroneResult with ordered event records and provenance metadata.
    """
    raise NotImplementedError("timeline_drone.run() not yet implemented")
