"""Tests for is_adjacent."""

from typing import Iterable

from aoc.grid import is_adjacent


def test_single_coordinate_cross_adjacent():
    """
    Test adjacency for a single coordinate with cross_sides=True and diagonal_sides=False.

    Verifies that a coordinate adjacent via cardinal directions is correctly identified.
    """
    coord = (5, 5)
    adjacent_coords = [(5, 6), (6, 5), (5, 4), (4, 5)]
    for other in adjacent_coords:
        assert (
            is_adjacent(coord, other) is True
        ), f"Coordinate {other} should be adjacent to {coord}."


def test_single_coordinate_not_adjacent():
    """
    Test that non-adjacent coordinates are correctly identified.

    Ensures that coordinates not adjacent via any direction are not falsely identified as adjacent.
    """
    coord = (5, 5)
    non_adjacent_coords = [(7, 5), (5, 8), (3, 3), (10, 10)]
    for other in non_adjacent_coords:
        assert (
            is_adjacent(coord, other) is False
        ), f"Coordinate {other} should not be adjacent to {coord}."


def test_single_coordinate_diagonal_adjacent():
    """
    Test adjacency for a single coordinate including diagonals.

    Verifies that diagonal adjacency is correctly identified when diagonal_sides=True.
    """
    coord = (5, 5)
    diagonal_coords = [(6, 6), (4, 6), (6, 4), (4, 4)]
    for other in diagonal_coords:
        # Should be False when diagonal_sides=False
        assert (
            is_adjacent(coord, other) is False
        ), f"Coordinate {other} should not be adjacent without diagonals."

        # Should be True when diagonal_sides=True
        assert (
            is_adjacent(coord, other, diagonal_sides=True) is True
        ), f"Coordinate {other} should be adjacent with diagonals."


def test_iterable_coordinates_some_adjacent():
    """
    Test adjacency when provided with an iterable containing both adjacent and non-adjacent coordinates.

    Ensures that the function returns True if any coordinate in the iterable is adjacent.
    """
    coord = (5, 5)
    test_coords = [(7, 5), (5, 6), (10, 10)]
    assert is_adjacent(coord, test_coords) is True, "At least one coordinate should be adjacent."


def test_iterable_coordinates_none_adjacent():
    """
    Test adjacency when provided with an iterable containing no adjacent coordinates.

    Ensures that the function returns False when none of the coordinates are adjacent.
    """
    coord = (5, 5)
    test_coords = [(7, 5), (5, 8), (10, 10)]
    assert is_adjacent(coord, test_coords) is False, "No coordinates should be adjacent."


def test_iterable_coordinates_with_diagonals():
    """
    Test adjacency for an iterable of coordinates including diagonals.

    Verifies that the function correctly identifies adjacent coordinates when diagonals are considered.
    """
    coord = (5, 5)
    test_coords = [(7, 5), (5, 6), (6, 6)]

    # Without diagonals, only (5,6) and (6,5) would be adjacent
    assert (
        is_adjacent(coord, test_coords, diagonal_sides=False) is True
    ), "At least one coordinate should be adjacent without diagonals."

    # With diagonals, (6,6) should also be considered adjacent
    assert (
        is_adjacent(coord, test_coords, diagonal_sides=True) is True
    ), "At least one coordinate should be adjacent with diagonals."


def test_empty_iterable():
    """
    Test adjacency when provided with an empty iterable.

    Ensures that the function returns False when the iterable is empty.
    """
    coord = (5, 5)
    test_coords: Iterable[tuple[int, int]] = []
    assert is_adjacent(coord, test_coords) is False, "Empty iterable should return False."


def test_large_coordinates():
    """
    Test adjacency for coordinates with large integer values.

    Verifies that the function works correctly with large numbers.
    """
    coord = (1000000, 1000000)
    adjacent_coords = [(1000000, 1000001), (1000001, 1000000), (1000000, 999999), (999999, 1000000)]
    for other in adjacent_coords:
        assert (
            is_adjacent(coord, other) is True
        ), f"Coordinate {other} should be adjacent to {coord}."


def test_negative_coordinates():
    """
    Test adjacency for coordinates with negative integer values.

    Ensures that the function correctly identifies adjacency in negative coordinate spaces.
    """
    coord = (-5, -5)
    adjacent_coords = [(-5, -4), (-4, -5), (-5, -6), (-6, -5)]
    non_adjacent_coords = [(-7, -5), (-5, -8), (-3, -3)]

    for other in adjacent_coords:
        assert (
            is_adjacent(coord, other) is True
        ), f"Coordinate {other} should be adjacent to {coord}."

    for other in non_adjacent_coords:
        assert (
            is_adjacent(coord, other) is False
        ), f"Coordinate {other} should not be adjacent to {coord}."


def test_coordinate_same_as_test():
    """
    Test behavior when the coordinate being tested is the same as the target coordinate.

    Ensures that a coordinate is not considered adjacent to itself.
    """
    coord = (5, 5)
    assert is_adjacent(coord, coord) is False, "A coordinate should not be adjacent to itself."


def test_multiple_adjacent_coordinates():
    """
    Test adjacency when multiple coordinates are adjacent.

    Verifies that the function returns True when multiple coordinates are adjacent.
    """
    coord = (5, 5)
    test_coords = [(5, 6), (6, 5), (5, 4), (4, 5)]
    assert is_adjacent(coord, test_coords) is True, "Multiple coordinates should be adjacent."


def test_mixed_adjacent_and_non_adjacent():
    """
    Test adjacency with a mix of adjacent and non-adjacent coordinates.

    Ensures that the presence of at least one adjacent coordinate results in a True return value.
    """
    coord = (5, 5)
    test_coords = [(7, 5), (5, 6), (10, 10), (4, 5)]
    assert is_adjacent(coord, test_coords) is True, "At least one coordinate should be adjacent."


def test_only_diagonal_adjacent():
    """
    Test adjacency when only diagonal coordinates are adjacent.

    Ensures that without enabling diagonal_sides, diagonal adjacents are not considered.
    """
    coord = (5, 5)
    diagonal_coords = [(6, 6), (4, 6), (6, 4), (4, 4)]
    for other in diagonal_coords:
        assert (
            is_adjacent(coord, other) is False
        ), f"Diagonal coordinate {other} should not be adjacent without diagonals."


def test_boundary_conditions():
    """
    Test adjacency at boundary conditions (e.g., origin).

    Ensures that the function correctly identifies adjacency when coordinates are at or near boundaries.
    """
    coord = (0, 0)
    adjacent_coords = [(0, 1), (1, 0)]
    non_adjacent_coords = [(1, 1), (-2, 0), (0, -2)]

    for other in adjacent_coords:
        assert (
            is_adjacent(coord, other) is True
        ), f"Coordinate {other} should be adjacent to {coord}."

    for other in non_adjacent_coords:
        assert (
            is_adjacent(coord, other) is False
        ), f"Coordinate {other} should not be adjacent to {coord}."


def test_multiple_adjacent_with_diagonals():
    """
    Test adjacency with multiple adjacent coordinates including diagonals.

    Verifies that the function correctly identifies multiple adjacents when diagonals are enabled.
    """
    coord = (5, 5)
    test_coords = [(5, 6), (6, 6), (6, 5), (5, 4), (4, 5), (4, 4)]
    assert (
        is_adjacent(coord, test_coords, diagonal_sides=True) is True
    ), "Multiple coordinates should be adjacent with diagonals."
