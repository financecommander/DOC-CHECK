"""Delaware drone – retrieves entity registration data from Delaware SOS."""

from hive.drones.base import DroneTask, DroneResult


def run(task: DroneTask) -> DroneResult:
    """
    Look up Delaware SOS records for the entity specified in task.target_entity.

    Returns a DroneResult with registration records and provenance metadata.
    Delegates HTTP retrieval to calculus-tools Delaware connector.
    """
    raise NotImplementedError("delaware_drone.run() not yet implemented")
