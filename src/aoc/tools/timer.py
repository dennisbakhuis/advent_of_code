"""Module for measuring execution time of functions."""

import time
import logging
from functools import wraps


logging.basicConfig(level=logging.INFO, format="%(message)s")


def timer(func):
    """Measure execution time of a function."""

    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        """Measure execution time of a function."""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        logging.info(f"Function '{func.__name__}' executed in {elapsed_time:.4f} seconds.")
        return result

    return wrapper_timer
