"""EDGAR drone – retrieves SEC filings for a target entity."""

from hive.drones.base import DroneTask, DroneResult


def run(task: DroneTask) -> DroneResult:
    """
    Fetch EDGAR filings for the entity specified in task.target_entity.

    Returns a DroneResult with raw filing records and provenance metadata.
    Delegates HTTP retrieval to calculus-tools SEC EDGAR connector.
    """
    raise NotImplementedError("edgar_drone.run() not yet implemented")
