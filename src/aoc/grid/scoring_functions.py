"""Dijkstra scoring functions."""

from ..types import Coordinate, Direction


def manhatten_scoring(
    previous_location: Coordinate = (0, 0),
    current_location: Coordinate = (0, 0),
    previous_direction: Direction = Direction.EAST,
    current_direction: Direction = Direction.EAST,
) -> int:
    """
    Manhattan scoring function, simply returning 1 for each step.

    Default scoring function for the Dijkstra algorithm.

    Parameters
    ----------
    previous_location : Coordinate
        The previous location.
    current_location : Coordinate
        The current location.
    previous_direction : Direction
        The previous direction.
    current_direction : Direction
        The current direction.

    Returns
    -------
    int
        The score for the current location.
    """
    return 1
