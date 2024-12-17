"""Tests for find_adjacent function."""

from aoc.grid import find_adjacent


def test_no_adjacent_coordinates():
    """Test when there are no adjacent coordinates."""
    coordinate = (5, 5)
    coordinates = [(1, 1), (2, 2), (3, 3)]
    result = find_adjacent(coordinate, coordinates)
    assert result == set(), "Expected no adjacent coordinates"


def test_adjacent_coordinates_without_diagonals():
    """Test finding adjacent coordinates without including diagonals."""
    coordinate = (2, 2)
    coordinates = [(1, 2), (3, 2), (2, 1), (2, 3), (1, 1)]
    expected = {(1, 2), (3, 2), (2, 1), (2, 3)}
    result = find_adjacent(coordinate, coordinates)
    assert result == expected, "Adjacent coordinates without diagonals do not match"


def test_adjacent_coordinates_with_diagonals():
    """Test finding adjacent coordinates including diagonals."""
    coordinate = (2, 2)
    coordinates = [(1, 2), (3, 2), (2, 1), (2, 3), (1, 1), (1, 3), (3, 1), (3, 3)]
    expected = {(1, 2), (3, 2), (2, 1), (2, 3), (1, 1), (1, 3), (3, 1), (3, 3)}
    result = find_adjacent(coordinate, coordinates, diagonal_sides=True)
    assert result == expected, "Adjacent coordinates with diagonals do not match"


def test_edge_coordinate_without_diagonals():
    """Test finding adjacent coordinates for a coordinate on the edge without diagonals."""
    coordinate = (0, 0)
    coordinates = [(0, 1), (1, 0), (1, 1)]
    expected = {(0, 1), (1, 0)}
    result = find_adjacent(coordinate, coordinates)
    assert result == expected, "Adjacent edge coordinates without diagonals do not match"


def test_empty_coordinates_list():
    """Test when the coordinates list is empty."""
    coordinate = (2, 2)
    coordinates = []
    result = find_adjacent(coordinate, coordinates)
    assert result == set(), "Expected no adjacent coordinates for empty coordinates list"


def test_duplicate_coordinates():
    """Test handling of duplicate coordinates in the input list."""
    coordinate = (2, 2)
    coordinates = [(1, 2), (1, 2), (3, 2), (2, 1), (2, 1)]
    expected = {(1, 2), (3, 2), (2, 1)}
    result = find_adjacent(coordinate, coordinates)
    assert result == expected, "Duplicate coordinates should not affect the result"


def test_coordinate_not_in_list():
    """Test when the main coordinate is not present in the coordinates list."""
    coordinate = (4, 4)
    coordinates = [(3, 4), (4, 3), (5, 4), (4, 5)]
    expected = {(3, 4), (4, 3), (5, 4), (4, 5)}
    result = find_adjacent(coordinate, coordinates)
    assert (
        result == expected
    ), "Adjacent coordinates should be found even if the main coordinate is not in the list"
