"""
Rate-limit utilities – retry helpers and per-source rate-limit enforcement.

All source adapters should use rate_limited() to respect API rate limits
and avoid service bans.
"""

from __future__ import annotations

import threading
import time
from functools import wraps
from typing import Any, Callable


def rate_limited(calls_per_second: float = 1.0) -> Callable:
    """
    Decorator that enforces a minimum interval between successive calls.

    Thread-safe: uses a lock to protect the last-called timestamp so that
    concurrent callers cannot bypass the rate limit.

    Args:
        calls_per_second: Maximum allowed calls per second (default: 1.0).
    """
    min_interval = 1.0 / calls_per_second
    lock = threading.Lock()
    last_called: list[float] = [0.0]

    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            with lock:
                elapsed = time.monotonic() - last_called[0]
                wait = min_interval - elapsed
                if wait > 0:
                    time.sleep(wait)
                last_called[0] = time.monotonic()
            return fn(*args, **kwargs)

        return wrapper

    return decorator


def retry(
    max_attempts: int = 3,
    backoff_seconds: float = 2.0,
    exceptions: tuple[type[Exception], ...] = (Exception,),
) -> Callable:
    """
    Decorator that retries a function on transient failures.

    Args:
        max_attempts: Total number of attempts (including the first).
        backoff_seconds: Initial wait time, doubled on each subsequent retry.
        exceptions: Tuple of exception types that trigger a retry.
    """

    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            wait = backoff_seconds
            for attempt in range(1, max_attempts + 1):
                try:
                    return fn(*args, **kwargs)
                except exceptions as exc:
                    if attempt == max_attempts:
                        raise
                    time.sleep(wait)
                    wait *= 2

        return wrapper

    return decorator
