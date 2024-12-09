"""
Test suite for the `within_bounds` function.

This module contains exhaustive tests for the `within_bounds` function using pytest.
Each test is documented with numpy-style docstrings.
"""

from typing import Iterable

from aoc.grid import within_bounds


def test_within_bounds_single_coordinate_within():
    """
    Test that a single coordinate within the bounds returns True.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinate = (5, 5)
    assert within_bounds(coordinate, bounds) is True


def test_within_bounds_single_coordinate_on_edge():
    """
    Test that a single coordinate on the edge of the bounds returns True.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    edge_coordinates = [
        (0, 5),  # Left edge
        (10, 5),  # Right edge
        (5, 0),  # Top edge
        (5, 10),  # Bottom edge
    ]
    for coord in edge_coordinates:
        assert within_bounds(coord, bounds) is True


def test_within_bounds_single_coordinate_out_of_bounds_left():
    """
    Test that a single coordinate left of the bounds returns False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinate = (-1, 5)
    assert within_bounds(coordinate, bounds) is False


def test_within_bounds_single_coordinate_out_of_bounds_right():
    """
    Test that a single coordinate right of the bounds returns False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinate = (11, 5)
    assert within_bounds(coordinate, bounds) is False


def test_within_bounds_single_coordinate_out_of_bounds_top():
    """
    Test that a single coordinate above the bounds returns False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinate = (5, -1)
    assert within_bounds(coordinate, bounds) is False


def test_within_bounds_single_coordinate_out_of_bounds_bottom():
    """
    Test that a single coordinate below the bounds returns False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinate = (5, 11)
    assert within_bounds(coordinate, bounds) is False


def test_within_bounds_iterable_all_within():
    """
    Test that all coordinates in an iterable within the bounds return True.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinates = [(1, 1), (5, 5), (10, 10), (0, 0)]
    assert within_bounds(coordinates, bounds) is True


def test_within_bounds_iterable_some_out_of_bounds():
    """
    Test that if any coordinate in an iterable is out of bounds, the function returns False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinates = [(1, 1), (5, 5), (11, 10), (0, 0)]
    assert within_bounds(coordinates, bounds) is False


def test_within_bounds_iterable_all_out_of_bounds():
    """
    Test that all coordinates in an iterable out of bounds return False.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinates = [(-1, -1), (11, 11), (15, 5)]
    assert within_bounds(coordinates, bounds) is False


def test_within_bounds_iterable_empty():
    """
    Test that an empty iterable returns True as there are no coordinates out of bounds.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    coordinates: Iterable[tuple[int, int]] = []
    assert within_bounds(coordinates, bounds) is True


def test_within_bounds_iterable_different_iterables():
    """
    Test that the function correctly handles different types of iterables (list, tuple, generator).

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)
    list_coords = [(1, 1), (2, 2)]
    tuple_coords = ((3, 3), (4, 4))
    generator_coords = ((x, x) for x in range(5, 7))

    assert within_bounds(list_coords, bounds) is True
    assert within_bounds(tuple_coords, bounds) is True
    assert within_bounds(generator_coords, bounds) is True


def test_within_bounds_negative_coordinates():
    """
    Test that coordinates with negative values are correctly evaluated against bounds.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (-5, -5, 5, 5)
    coordinates_within = [(-5, -5), (0, 0), (5, 5)]
    coordinates_out = [(-6, 0), (0, -6), (6, 0), (0, 6)]

    assert within_bounds(coordinates_within, bounds) is True
    for coord in coordinates_out:
        assert within_bounds(coord, bounds) is False


def test_within_bounds_large_coordinates():
    """
    Test that the function handles large coordinate values correctly.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 1_000_000, 1_000_000)
    coordinates_within = [(0, 0), (500_000, 500_000), (1_000_000, 1_000_000)]
    coordinates_out = [(-1, 500_000), (500_000, -1), (1_000_001, 500_000), (500_000, 1_000_001)]

    assert within_bounds(coordinates_within, bounds) is True
    for coord in coordinates_out:
        assert within_bounds(coord, bounds) is False


def test_within_bounds_mixed_coordinate_types():
    """
    Test that the function correctly handles coordinates provided as different iterable types.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    bounds = (0, 0, 10, 10)

    # List of tuples
    list_coords = [(1, 1), (2, 2)]
    assert within_bounds(list_coords, bounds) is True

    # Tuple of tuples
    tuple_coords = ((3, 3), (4, 4))
    assert within_bounds(tuple_coords, bounds) is True

    # Set of tuples
    set_coords = {(5, 5), (6, 6)}
    assert within_bounds(set_coords, bounds) is True

    # Generator of tuples
    generator_coords = ((x, x) for x in range(7, 9))
    assert within_bounds(generator_coords, bounds) is True
