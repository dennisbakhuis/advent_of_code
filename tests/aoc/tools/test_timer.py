"""Tests for timer function."""

import logging
import time
from aoc.tools import timer


@timer
def sample_function():
    """Create nothing and return None."""
    pass


@timer
def add(a, b):
    """Add two numbers."""
    return a + b


@timer
def sleep_function(duration):
    """Sleeps for the specified duration."""
    time.sleep(duration)
    return duration


def test_timer_returns_correct_result():
    """Test that the decorated function returns the correct result."""
    result = add(2, 3)
    assert result == 5, "The add function should return the sum of its arguments."


def test_timer_does_not_alter_function_behavior():
    """Ensure the decorator does not alter the original function's behavior."""
    result = sample_function()
    assert result is None, "The sample_function should return None."


def test_timer_with_arguments():
    """Test that the decorator works with functions that accept arguments."""
    duration = 0.5
    start = time.perf_counter()
    result = sleep_function(duration)
    end = time.perf_counter()
    assert result == duration, "sleep_function should return the duration it slept."
    assert (
        end - start >= duration
    ), "sleep_function should sleep for at least the specified duration."


def test_timer_logs_execution_time(caplog):
    """Verify that the decorator logs the execution time of the function."""
    with caplog.at_level(logging.INFO):
        add(1, 2)
    # Check that a log message was created
    assert len(caplog.records) == 1, "There should be one log record."
    log_message = caplog.records[0].message
    assert (
        "Function 'add' executed in" in log_message
    ), "Log message should contain the function name and execution time."
    # Optionally, check the format of the elapsed time
    import re

    pattern = r"Function 'add' executed in \d+\.\d{4} seconds\."
    assert re.match(pattern, log_message), "Log message should match the expected format."


def test_timer_multiple_calls(caplog):
    """Ensure that multiple calls to the decorated function each log their execution time."""
    with caplog.at_level(logging.INFO):
        add(1, 2)
        add(3, 4)
    # There should be two log records
    assert len(caplog.records) == 2, "There should be two log records for two function calls."
    for record in caplog.records:
        assert (
            "Function 'add' executed in" in record.message
        ), "Each log message should contain the function name and execution time."


def test_timer_decorator_preserves_function_metadata():
    """Check that the decorator preserves the original function's metadata."""
    assert (
        sample_function.__name__ == "sample_function"
    ), "The decorated function should retain its original name."
    assert (
        sample_function.__doc__ == "Create nothing and return None."
    ), "The decorated function should retain its original docstring."
