"""Tests for the group_adjacent function."""

import pytest

from aoc.grid import group_adjacent


@pytest.mark.parametrize(
    "coordinates,cross_sides,diagonal_sides,expected",
    [
        # No coordinates
        ([], True, False, set()),
        # Single coordinate
        ([(0, 0)], True, False, {frozenset({(0, 0)})}),
        # Two separate coordinates with no adjacency
        ([(0, 0), (2, 2)], True, False, {frozenset({(0, 0)}), frozenset({(2, 2)})}),
        # Horizontal adjacency
        ([(0, 0), (0, 1)], True, False, {frozenset({(0, 0), (0, 1)})}),
        # Vertical adjacency
        ([(0, 0), (1, 0)], True, False, {frozenset({(0, 0), (1, 0)})}),
        # Diagonal adjacency not considered by default
        ([(0, 0), (1, 1)], True, False, {frozenset({(0, 0)}), frozenset({(1, 1)})}),
        # Diagonal adjacency considered
        ([(0, 0), (1, 1)], True, True, {frozenset({(0, 0), (1, 1)})}),
        # Mixed adjacency (some diagonal, some straight)
        ([(0, 0), (0, 1), (1, 1)], True, True, {frozenset({(0, 0), (0, 1), (1, 1)})}),
        # Multiple separate groups
        (
            [(0, 0), (0, 1), (2, 2), (2, 3)],
            True,
            False,
            {frozenset({(0, 0), (0, 1)}), frozenset({(2, 2), (2, 3)})},
        ),
        # Example from docstring
        (
            [(1, 1), (1, 2), (5, 5), (4, 5), (10, 4)],
            True,
            False,
            {frozenset({(1, 1), (1, 2)}), frozenset({(5, 5), (4, 5)}), frozenset({(10, 4)})},
        ),
        # Large cluster forming a square
        (
            [(x, y) for x in range(3) for y in range(3)],
            True,
            False,
            {frozenset((x, y) for x in range(3) for y in range(3))},
        ),
        # Cluster connected only via diagonals when diagonal_sides=True
        ([(0, 0), (1, 1), (2, 2)], False, True, {frozenset({(0, 0), (1, 1), (2, 2)})}),
        # Same coordinates repeated in input
        ([(0, 0), (0, 0), (1, 0)], True, False, {frozenset({(0, 0), (1, 0)})}),
    ],
)
def test_group_adjacent(coordinates, cross_sides, diagonal_sides, expected):
    """Test group_adjacent function."""
    result = group_adjacent(coordinates, cross_sides=cross_sides, diagonal_sides=diagonal_sides)
    assert result == expected
