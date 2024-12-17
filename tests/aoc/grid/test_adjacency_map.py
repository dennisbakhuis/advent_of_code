"""Build adjacency maps for coordinates in a grid."""

import pytest
from typing import Iterable

from aoc.grid import adjacency_map
from aoc.types import Coordinate, AdjacencyMap


@pytest.fixture
def sample_coordinates() -> Iterable[Coordinate]:
    """
    Sample coordinates for testing adjacency_map function.

    Returns
    -------
    Iterable[Coordinate]
        A list of coordinates forming a 3x3 grid.
    """
    return [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]


def test_adjacency_map_empty():
    """
    Test adjacency_map with an empty list of coordinates.

    Expected behavior:
    - Returns an empty adjacency map.
    """
    coordinates: Iterable[Coordinate] = []
    expected: AdjacencyMap = {}
    result = adjacency_map(coordinates)
    assert result == expected, "Adjacency map should be empty for empty coordinates."


def test_adjacency_map_single_coordinate():
    """
    Test adjacency_map with a single coordinate.

    Expected behavior:
    - The single coordinate maps to an empty set of adjacents.
    """
    coordinates: Iterable[Coordinate] = [(0, 0)]
    expected: AdjacencyMap = {(0, 0): set()}
    result = adjacency_map(coordinates)
    assert result == expected, "Single coordinate should have no adjacents."


def test_adjacency_map_no_diagonals():
    """
    Test adjacency_map without diagonal adjacencies.

    Expected behavior:
    - Only orthogonal adjacents are included.
    """
    coordinates = [(0, 0), (0, 1), (1, 0), (1, 1)]
    expected: AdjacencyMap = {
        (0, 0): {(0, 1), (1, 0)},
        (0, 1): {(0, 0), (1, 1)},
        (1, 0): {(0, 0), (1, 1)},
        (1, 1): {(0, 1), (1, 0)},
    }
    result = adjacency_map(coordinates, diagonal_sides=False)
    assert result == expected, "Adjacency map without diagonals is incorrect."


def test_adjacency_map_with_diagonals():
    """
    Test adjacency_map with diagonal adjacencies enabled.

    Expected behavior:
    - Both orthogonal and diagonal adjacents are included.
    """
    coordinates = [(0, 0), (0, 1), (1, 0), (1, 1)]
    expected: AdjacencyMap = {
        (0, 0): {(0, 1), (1, 0), (1, 1)},
        (0, 1): {(0, 0), (1, 1), (1, 0)},
        (1, 0): {(0, 0), (1, 1), (0, 1)},
        (1, 1): {(0, 1), (1, 0), (0, 0)},
    }
    result = adjacency_map(coordinates, diagonal_sides=True)
    assert result == expected, "Adjacency map with diagonals is incorrect."


def test_adjacency_map_partial_adjacents(sample_coordinates):
    """
    Test adjacency_map with a 3x3 grid and verify adjacents for edge and center coordinates.

    Parameters
    ----------
    sample_coordinates : Iterable[Coordinate]
        Fixture providing a 3x3 grid of coordinates.

    Expected behavior:
    - Each coordinate has the correct set of adjacents based on its position.
    """
    expected: AdjacencyMap = {
        (0, 0): {(0, 1), (1, 0)},
        (0, 1): {(0, 0), (0, 2), (1, 1)},
        (0, 2): {(0, 1), (1, 2)},
        (1, 0): {(0, 0), (2, 0), (1, 1)},
        (1, 1): {(1, 0), (1, 2), (0, 1), (2, 1)},
        (1, 2): {(1, 1), (0, 2), (2, 2)},
        (2, 0): {(1, 0), (2, 1)},
        (2, 1): {(2, 0), (2, 2), (1, 1)},
        (2, 2): {(2, 1), (1, 2)},
    }
    result = adjacency_map(sample_coordinates, diagonal_sides=False)
    assert result == expected, "Adjacency map for 3x3 grid without diagonals is incorrect."


def test_adjacency_map_with_diagonals_partial(sample_coordinates):
    """
    Test adjacency_map with a 3x3 grid and diagonals enabled.

    Parameters
    ----------
    sample_coordinates : Iterable[Coordinate]
        Fixture providing a 3x3 grid of coordinates.

    Expected behavior:
    - Each coordinate includes diagonal adjacents in addition to orthogonal ones.
    """
    expected: AdjacencyMap = {
        (0, 0): {(0, 1), (1, 0), (1, 1)},
        (0, 1): {(0, 0), (0, 2), (1, 1), (1, 0), (1, 2)},
        (0, 2): {(0, 1), (1, 2), (1, 1)},
        (1, 0): {(0, 0), (2, 0), (1, 1), (0, 1), (2, 1)},
        (1, 1): {(1, 0), (1, 2), (0, 1), (2, 1), (0, 0), (0, 2), (2, 0), (2, 2)},
        (1, 2): {(1, 1), (0, 2), (2, 2), (0, 1), (2, 1)},
        (2, 0): {(1, 0), (2, 1), (1, 1)},
        (2, 1): {(2, 0), (2, 2), (1, 1), (1, 0), (1, 2)},
        (2, 2): {(2, 1), (1, 2), (1, 1)},
    }
    result = adjacency_map(sample_coordinates, diagonal_sides=True)
    assert result == expected, "Adjacency map for 3x3 grid with diagonals is incorrect."


def test_adjacency_map_with_duplicates():
    """
    Test adjacency_map with duplicate coordinates.

    Expected behavior:
    - Duplicates are ignored, and each coordinate appears only once in the map.
    """
    coordinates = [(0, 0), (0, 0), (0, 1), (1, 0), (1, 1), (1, 1)]
    expected: AdjacencyMap = {
        (0, 0): {(0, 1), (1, 0)},
        (0, 1): {(0, 0), (1, 1)},
        (1, 0): {(0, 0), (1, 1)},
        (1, 1): {(0, 1), (1, 0)},
    }
    result = adjacency_map(coordinates, diagonal_sides=False)
    assert result == expected, "Adjacency map should handle duplicate coordinates correctly."
