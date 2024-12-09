"""Tests for the get_coordinates_from_line module."""

import pytest
from unittest.mock import patch

# Import the functions from the aoc.grid module
from aoc.grid import get_coordinates_from_line


def within_bounds_mock(x, y, bounds):
    """
    Mock implementation of the within_bounds function.

    Parameters
    ----------
    x : int
        The x-coordinate.
    y : int
        The y-coordinate.
    bounds : tuple of int or None
        The boundaries as (min_x, min_y, max_x, max_y). If None, all coordinates are considered valid.

    Returns
    -------
    bool
        True if (x, y) is within bounds, False otherwise.
    """
    if bounds is None:
        return True
    min_x, min_y, max_x, max_y = bounds
    return min_x <= x <= max_x and min_y <= y <= max_y


@pytest.fixture
def mock_within_bounds_fixture():
    """
    Fixture to mock the within_bounds function in the aoc.grid module.

    Yields
    ------
    None
    """
    with patch("aoc.grid.within_bounds", side_effect=within_bounds_mock):
        yield


def test_same_start_end_within_bounds(mock_within_bounds_fixture):
    """
    Test when start and end points are the same and within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinate.
    """
    start = (5, 5)
    end = (5, 5)
    bounds = (0, 0, 10, 10)
    expected = {(5, 5)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_same_start_end_out_of_bounds(mock_within_bounds_fixture):
    """
    Test when start and end points are the same and out of bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the coordinate is out of bounds.
    """
    start = (15, 5)
    end = (15, 5)
    bounds = (0, 0, 10, 10)
    with pytest.raises(ValueError) as exc_info:
        get_coordinates_from_line(start, end, bounds)
    assert "out of bounds" in str(exc_info.value)


def test_horizontal_line_within_bounds(mock_within_bounds_fixture):
    """
    Test a horizontal line within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (2, 3)
    end = (5, 3)
    bounds = (0, 0, 10, 10)
    expected = {(2, 3), (3, 3), (4, 3), (5, 3)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_vertical_line_within_bounds(mock_within_bounds_fixture):
    """
    Test a vertical line within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (4, 1)
    end = (4, 4)
    bounds = (0, 0, 10, 10)
    expected = {(4, 1), (4, 2), (4, 3), (4, 4)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_diagonal_line_positive_slope_within_bounds(mock_within_bounds_fixture):
    """
    Test a diagonal line with positive slope within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (1, 1)
    end = (4, 4)
    bounds = (0, 0, 10, 10)
    expected = {(1, 1), (2, 2), (3, 3), (4, 4)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_diagonal_line_negative_slope_within_bounds(mock_within_bounds_fixture):
    """
    Test a diagonal line with negative slope within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (5, 5)
    end = (2, 2)
    bounds = (0, 0, 10, 10)
    expected = {(5, 5), (4, 4), (3, 3), (2, 2)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_out_of_bounds_middle_point(mock_within_bounds_fixture):
    """
    Test a line where a middle point is out of bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If any coordinate on the line is out of bounds.
    """
    start = (1, 1)
    end = (4, 4)
    bounds = (0, 0, 3, 3)  # (4,4) is out of bounds
    with pytest.raises(ValueError):
        get_coordinates_from_line(start, end, bounds)


def test_line_out_of_bounds_middle_point2(mock_within_bounds_fixture):
    """
    Test a line where a middle point is out of bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If any coordinate on the line is out of bounds.
    """
    start = (1, 4)
    end = (4, 4)
    bounds = (0, 0, 3, 3)  # (4,4) is out of bounds
    with pytest.raises(ValueError):
        get_coordinates_from_line(start, end, bounds)


def test_line_on_boundary(mock_within_bounds_fixture):
    """
    Test a line that lies exactly on the boundary.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    None
        No exceptions should be raised.
    """
    start = (0, 0)
    end = (5, 5)
    bounds = (0, 0, 5, 5)
    expected = {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_exceeding_bounds_end_point(mock_within_bounds_fixture):
    """
    Test a line where the end point exceeds the bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the end coordinate is out of bounds.
    """
    start = (2, 2)
    end = (6, 6)
    bounds = (0, 0, 5, 5)
    with pytest.raises(ValueError) as exc_info:
        get_coordinates_from_line(start, end, bounds)
    assert "out of bounds" in str(exc_info.value)


def test_steep_slope_line_within_bounds(mock_within_bounds_fixture):
    """
    Test a line with a steep slope within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (2, 2)
    end = (3, 5)
    bounds = (0, 0, 10, 10)
    expected = {(2, 2), (2, 3), (3, 4), (3, 5)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_shallow_slope_line_within_bounds(mock_within_bounds_fixture):
    """
    Test a line with a shallow slope within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (2, 2)
    end = (5, 3)
    bounds = (0, 0, 10, 10)
    expected = {(2, 2), (3, 2), (4, 3), (5, 3)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_negative_direction_line_within_bounds(mock_within_bounds_fixture):
    """
    Test a line moving in negative x and y directions within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (5, 5)
    end = (2, 2)
    bounds = (0, 0, 10, 10)
    expected = {(5, 5), (4, 4), (3, 3), (2, 2)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_with_zero_length_axis_horizontal(mock_within_bounds_fixture):
    """
    Test a horizontal line where y-coordinate does not change.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (1, 2)
    end = (4, 2)
    bounds = (0, 0, 5, 5)
    expected = {(1, 2), (2, 2), (3, 2), (4, 2)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_with_zero_length_axis_vertical(mock_within_bounds_fixture):
    """
    Test a vertical line where x-coordinate does not change.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (3, 1)
    end = (3, 4)
    bounds = (0, 0, 5, 5)
    expected = {(3, 1), (3, 2), (3, 3), (3, 4)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_touching_bounds(mock_within_bounds_fixture):
    """
    Test a line that touches the boundary but does not exceed it.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (0, 5)
    end = (5, 0)
    bounds = (0, 0, 5, 5)
    expected = {(0, 5), (1, 4), (2, 3), (3, 2), (4, 1), (5, 0)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_long_line_within_large_bounds(mock_within_bounds_fixture):
    """
    Test a long line within large bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (0, 0)
    end = (10, 10)
    bounds = (0, 0, 10, 10)
    expected = {(i, i) for i in range(0, 11)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_with_negative_bounds(mock_within_bounds_fixture):
    """
    Test a line within negative bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (-3, -3)
    end = (-1, -1)
    bounds = (-5, -5, 0, 0)
    expected = {(-3, -3), (-2, -2), (-1, -1)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_partially_out_of_bounds(mock_within_bounds_fixture):
    """
    Test a line where some points are within bounds and others are out.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If any coordinate on the line is out of bounds.
    """
    start = (1, 1)
    end = (4, 4)
    bounds = (2, 2, 5, 5)
    with pytest.raises(ValueError):
        get_coordinates_from_line(start, end, bounds)


def test_line_with_large_coordinates_within_bounds(mock_within_bounds_fixture):
    """
    Test a line with large coordinate values within bounds.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (100, 100)
    end = (105, 105)
    bounds = (50, 50, 150, 150)
    expected = {(100, 100), (101, 101), (102, 102), (103, 103), (104, 104), (105, 105)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected


def test_line_with_single_step(mock_within_bounds_fixture):
    """
    Test a line that consists of a single step.

    Parameters
    ----------
    mock_within_bounds_fixture : fixture
        Mocked within_bounds function.

    Returns
    -------
    None

    Raises
    ------
    AssertionError
        If the returned set does not match the expected coordinates.
    """
    start = (2, 2)
    end = (3, 3)
    bounds = (0, 0, 5, 5)
    expected = {(2, 2), (3, 3)}
    result = get_coordinates_from_line(start, end, bounds)
    assert result == expected
