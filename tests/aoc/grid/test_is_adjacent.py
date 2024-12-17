"""Tests for is_adjacent."""

from typing import Iterable

import pytest

from aoc.grid import is_adjacent
from aoc.types import Coordinate


@pytest.fixture(scope="function")
def base_coordinate() -> Coordinate:
    """
    Fixture providing a base coordinate for adjacency tests.

    Returns
    -------
    Coordinate
        A base coordinate (1, 1).
    """
    return (1, 1)


@pytest.fixture(scope="function")
def adjacent_coordinates_with_diagonals() -> Iterable[Coordinate]:
    """
    Fixture providing coordinates adjacent to (1, 1).

    Returns
    -------
    Iterable[Coordinate]
        A list of coordinates adjacent to (1, 1) both orthogonally and diagonally.
    """
    return [
        (0, 0),  # Bottom-left
        (0, 2),  # Top-left
        (2, 0),  # Bottom-right
        (2, 2),  # Top-right
    ]


@pytest.fixture(scope="function")
def adjacent_coordinates() -> Iterable[Coordinate]:
    """
    Fixture providing coordinates adjacent to (1, 1) without diagonals.

    Returns
    -------
    Iterable[Coordinate]
        A list of coordinates adjacent to (1, 1) orthogonally.
    """
    return [
        (0, 1),  # Left
        (2, 1),  # Right
        (1, 0),  # Below
        (1, 2),  # Above
    ]


@pytest.fixture(scope="function")
def non_adjacent_coordinates() -> Iterable[Coordinate]:
    """
    Fixture providing coordinates that are not adjacent to (1, 1).

    Returns
    -------
    Iterable[Coordinate]
        A list of coordinates not adjacent to (1, 1).
    """
    return [
        (0, 3),
        (3, 0),
        (3, 3),
        (-1, -1),
        (1, 3),
        (3, 1),
    ]


def test_is_adjacent_single_coordinate_adjacent(base_coordinate, adjacent_coordinates):
    """
    Test is_adjacent with a single adjacent coordinate.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of adjacent coordinates.

    Expected behavior:
    - Returns True when the other coordinate is adjacent.
    """
    for adj in adjacent_coordinates:
        result = is_adjacent(base_coordinate, adj)
        assert result, f"Coordinate {adj} should be adjacent to {base_coordinate}."


def test_is_adjacent_single_coordinate_non_adjacent(base_coordinate, non_adjacent_coordinates):
    """
    Test is_adjacent with a single non-adjacent coordinate.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of non-adjacent coordinates.

    Expected behavior:
    - Returns False when the other coordinate is not adjacent.
    """
    for non_adj in non_adjacent_coordinates:
        result = is_adjacent(base_coordinate, non_adj)
        assert not result, f"Coordinate {non_adj} should not be adjacent to {base_coordinate}."


def test_is_adjacent_multiple_coordinates_some_adjacent(
    base_coordinate, adjacent_coordinates, non_adjacent_coordinates
):
    """
    Test is_adjacent with multiple coordinates where some are adjacent.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of adjacent coordinates.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of non-adjacent coordinates.

    Expected behavior:
    - Returns True if at least one coordinate is adjacent.
    """
    test_coords = list(adjacent_coordinates) + list(non_adjacent_coordinates)
    result = is_adjacent(base_coordinate, test_coords)
    assert result, "At least one coordinate in the list should be adjacent."


def test_is_adjacent_multiple_coordinates_none_adjacent(base_coordinate, non_adjacent_coordinates):
    """
    Test is_adjacent with multiple coordinates where none are adjacent.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of non-adjacent coordinates.

    Expected behavior:
    - Returns False if no coordinates are adjacent.
    """
    result = is_adjacent(base_coordinate, non_adjacent_coordinates)
    assert not result, "No coordinates in the list should be adjacent."


def test_is_adjacent_cross_sides_only(base_coordinate):
    """
    Test is_adjacent with cross_sides=True and diagonal_sides=False.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Returns True only for orthogonally adjacent coordinates.
    """
    orthogonal_adjacents = {(0, 1), (2, 1), (1, 0), (1, 2)}
    diagonals = {(0, 0), (0, 2), (2, 0), (2, 2)}

    # Test orthogonal adjacents
    for adj in orthogonal_adjacents:
        result = is_adjacent(base_coordinate, adj, cross_sides=True, diagonal_sides=False)
        assert result, f"Orthogonal coordinate {adj} should be adjacent."

    # Test diagonals
    for diag in diagonals:
        result = is_adjacent(base_coordinate, diag, cross_sides=True, diagonal_sides=False)
        assert (
            not result
        ), f"Diagonal coordinate {diag} should not be adjacent when diagonals are disabled."


def test_is_adjacent_diagonals_only(base_coordinate):
    """
    Test is_adjacent with cross_sides=False and diagonal_sides=True.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Returns True only for diagonally adjacent coordinates.
    """
    orthogonal_adjacents = {(0, 1), (2, 1), (1, 0), (1, 2)}
    diagonals = {(0, 0), (0, 2), (2, 0), (2, 2)}

    # Test orthogonal adjacents
    for adj in orthogonal_adjacents:
        result = is_adjacent(base_coordinate, adj, cross_sides=False, diagonal_sides=True)
        assert (
            not result
        ), f"Orthogonal coordinate {adj} should not be adjacent when cross_sides is disabled."

    # Test diagonals
    for diag in diagonals:
        result = is_adjacent(base_coordinate, diag, cross_sides=False, diagonal_sides=True)
        assert result, f"Diagonal coordinate {diag} should be adjacent."


def test_is_adjacent_all_sides(base_coordinate, adjacent_coordinates):
    """
    Test is_adjacent with cross_sides=True and diagonal_sides=True.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Returns True for both orthogonally and diagonally adjacent coordinates.
    """
    for adj in adjacent_coordinates:
        result = is_adjacent(base_coordinate, adj, cross_sides=True, diagonal_sides=True)
        assert (
            result
        ), f"Coordinate {adj} should be adjacent with both cross and diagonal sides enabled."


def test_is_adjacent_no_sides(base_coordinate, adjacent_coordinates, non_adjacent_coordinates):
    """
    Test is_adjacent with cross_sides=False and diagonal_sides=False.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of non-adjacent coordinates.

    Expected behavior:
    - Returns False for all coordinates as no adjacency sides are enabled.
    """
    test_coords = list(adjacent_coordinates) + list(non_adjacent_coordinates)
    result = is_adjacent(base_coordinate, test_coords, cross_sides=False, diagonal_sides=False)
    assert not result, "No adjacency sides enabled should result in no adjacents."


def test_is_adjacent_empty_other_coordinates(base_coordinate):
    """
    Test is_adjacent with an empty iterable of other_coordinates.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.

    Expected behavior:
    - Returns False as there are no coordinates to be adjacent.
    """
    result = is_adjacent(base_coordinate, [], cross_sides=True, diagonal_sides=False)
    assert not result, "Empty other_coordinates should result in no adjacents."


def test_is_adjacent_same_coordinate(base_coordinate):
    """
    Test is_adjacent where the other coordinate is the same as the base.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.

    Expected behavior:
    - Returns False as a coordinate is not adjacent to itself.
    """
    result = is_adjacent(base_coordinate, base_coordinate)
    assert not result, "A coordinate should not be adjacent to itself."


def test_is_adjacent_multiple_calls_consistency(base_coordinate, adjacent_coordinates):
    """
    Test is_adjacent with multiple calls to ensure consistency.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Each call to is_adjacent should consistently return the correct result.
    """
    # First with cross_sides=True, diagonal_sides=False
    orthogonal_adjacents = {(0, 1), (2, 1), (1, 0), (1, 2)}
    for adj in adjacent_coordinates:
        expected = adj in orthogonal_adjacents
        result = is_adjacent(base_coordinate, adj, cross_sides=True, diagonal_sides=False)
        assert result == expected, f"Adjacency result inconsistent for {adj}."


def test_is_adjacent_invalid_input(base_coordinate):
    """
    Test is_adjacent with invalid input types for other_coordinates.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.

    Expected behavior:
    - Raises a TypeError when other_coordinates is not a Coordinate or Iterable[Coordinate].
    """
    with pytest.raises(TypeError):
        is_adjacent(base_coordinate, 123)  # Invalid type


def test_is_adjacent_large_coordinates(base_coordinate):
    """
    Test is_adjacent with large coordinate values.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.

    Expected behavior:
    - Correctly identifies adjacency regardless of coordinate magnitude.
    """
    large_adjacent = (1000, 1001)  # Assuming base is (1000, 1000)
    base = (1000, 1000)
    result = is_adjacent(base, large_adjacent)
    assert result, f"Large coordinate {large_adjacent} should be adjacent to {base}."

    large_non_adjacent = (1002, 1002)
    result = is_adjacent(base, large_non_adjacent)
    assert not result, f"Large coordinate {large_non_adjacent} should not be adjacent to {base}."


def test_is_adjacent_negative_coordinates():
    """
    Test is_adjacent with negative coordinate values.

    Expected behavior:
    - Correctly identifies adjacency with negative coordinates.
    """
    base = (0, 0)
    adjacent_neg = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    non_adjacent_neg = [(-2, 0), (0, -2), (2, 2), (-2, -2)]

    for adj in adjacent_neg:
        result = is_adjacent(base, adj, diagonal_sides=True)
        assert result, f"Negative coordinate {adj} should be adjacent to {base}."

    for non_adj in non_adjacent_neg:
        result = is_adjacent(base, non_adj)
        assert not result, f"Negative coordinate {non_adj} should not be adjacent to {base}."


def test_is_adjacent_iterable_as_generator(base_coordinate, adjacent_coordinates):
    """
    Test is_adjacent with other_coordinates provided as a generator.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Correctly identifies adjacency when other_coordinates is a generator.
    """
    generator = (coord for coord in adjacent_coordinates)
    result = is_adjacent(base_coordinate, generator)
    assert result, "Generator containing adjacent coordinates should return True."


def test_is_adjacent_iterable_as_set(base_coordinate, adjacent_coordinates):
    """
    Test is_adjacent with other_coordinates provided as a set.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent both orthogonally and diagonally.

    Expected behavior:
    - Correctly identifies adjacency when other_coordinates is a set.
    """
    coord_set = set(adjacent_coordinates)
    result = is_adjacent(base_coordinate, coord_set)
    assert result, "Set containing adjacent coordinates should return True."


def test_is_adjacent_iterable_as_list_no_adjacent(base_coordinate, non_adjacent_coordinates):
    """
    Test is_adjacent with other_coordinates provided as a list with no adjacents.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates not adjacent to the base.

    Expected behavior:
    - Returns False when none of the coordinates are adjacent.
    """
    coord_list = list(non_adjacent_coordinates)
    result = is_adjacent(base_coordinate, coord_list)
    assert not result, "List with no adjacent coordinates should return False."


def test_is_adjacent_mixed_adjacent_and_non_adjacent(
    base_coordinate, adjacent_coordinates, non_adjacent_coordinates
):
    """
    Test is_adjacent with a mix of adjacent and non-adjacent coordinates.

    Parameters
    ----------
    base_coordinate : Coordinate
        The base coordinate to test against.
    adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates adjacent to the base.
    non_adjacent_coordinates : Iterable[Coordinate]
        A list of coordinates not adjacent to the base.

    Expected behavior:
    - Returns True as at least one coordinate is adjacent.
    """
    mixed_coords = list(adjacent_coordinates) + list(non_adjacent_coordinates)
    result = is_adjacent(base_coordinate, mixed_coords)
    assert result, "Mixed list with at least one adjacent coordinate should return True."
