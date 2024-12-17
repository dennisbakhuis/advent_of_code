"""Find adjacent coordinates in a list of coordinates."""

from typing import Iterable

from ..constants import ADJACENCY_DELTAS, ADJACENCY_DELTAS_WITH_DIAGONALS
from ..types import Coordinate


def find_adjacent(
    coordinate: Coordinate,
    coordinates: Iterable[Coordinate],
    diagonal_sides: bool = False,
) -> set[Coordinate]:
    """
    Find adjacent coordinates in a list of coordinates.

    Parameters
    ----------
    coordinate : Coordinate
        The coordinate to find adjacent coordinates for.
    coordinates : Iterable[Coordinate]
        The list of coordinates to search for adjacent coordinates.
    diagonal_sides : bool, optional
        Whether to include diagonal sides, by default False

    Returns
    -------
    set[Coordinate]
        The set of adjacent coordinates.
    """
    x, y = coordinate

    deltas = ADJACENCY_DELTAS_WITH_DIAGONALS if diagonal_sides else ADJACENCY_DELTAS

    adjacent = {(x + dx, y + dy) for dx, dy in deltas if (x + dx, y + dy) in coordinates}

    return adjacent
