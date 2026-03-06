"""Personnel drone – maps individuals affiliated with a target entity."""

from hive.drones.base import DroneTask, DroneResult


def run(task: DroneTask) -> DroneResult:
    """
    Discover and graph personnel associated with task.target_entity.

    Returns a DroneResult with person records and relationship metadata.
    """
    raise NotImplementedError("personnel_drone.run() not yet implemented")
