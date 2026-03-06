"""BrokerCheck drone – retrieves FINRA BrokerCheck records."""

from hive.drones.base import DroneTask, DroneResult


def run(task: DroneTask) -> DroneResult:
    """
    Query FINRA BrokerCheck for the entity or individual in task.target_entity.

    Returns a DroneResult with registration and disciplinary records.
    Delegates HTTP retrieval to calculus-tools BrokerCheck connector.
    """
    raise NotImplementedError("brokercheck_drone.run() not yet implemented")
