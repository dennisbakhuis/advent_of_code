"""Tests for Dijkstra's algorithm."""

from aoc.types import Direction
from aoc.grid import dijkstra_with_direction
from aoc.constants import UNREACHABLE


def test_dijkstra_multiple_steps():
    """Test Dijkstra with multiple steps in a straight line."""
    coordinates = [(0, 0), (1, 0), (2, 0), (3, 0)]
    start = (0, 0)
    result = dijkstra_with_direction(coordinates, start)

    assert result[(3, 0)][Direction.EAST]["score"] == 3, "Score should be 3 for three steps"
    assert result[(2, 0)][Direction.EAST]["score"] == 2, "Score should be 2 for two steps"


def test_dijkstra_with_obstacle():
    """Test Dijkstra when there is an obstacle blocking the direct path."""
    coordinates = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    # Remove (1,1) to create an obstacle
    coordinates.remove((1, 1))
    start = (0, 0)
    result = dijkstra_with_direction(coordinates, start)

    # Path should go around the obstacle
    assert (
        result[(2, 2)][Direction.EAST]["score"] == 4
    ), "Score should account for detour around obstacle"


def test_dijkstra_unreachable():
    """Test Dijkstra when some coordinates are unreachable."""
    coordinates = [(0, 0), (1, 0), (2, 0), (10, 10)]
    start = (0, 0)
    result = dijkstra_with_direction(coordinates, start)

    assert (
        result[(10, 10)][Direction.EAST]["score"] == UNREACHABLE
    ), "Unreachable coordinate should have score as UNREACHABLE"


def test_dijkstra_with_custom_scoring():
    """Test Dijkstra with a custom scoring function."""

    def custom_scoring(prev, current, prev_dir, current_dir):
        # Prefer horizontal movement by giving lower cost
        if current_dir in [Direction.EAST, Direction.WEST]:
            return 1
        else:
            return 2

    coordinates = [(0, 0), (1, 0), (1, 1), (2, 1)]
    start = (0, 0)
    result = dijkstra_with_direction(coordinates, start, scoring_function=custom_scoring)

    assert (
        result[(2, 1)][Direction.EAST]["score"] == 4
    ), "Custom scoring should calculate scores correctly"
