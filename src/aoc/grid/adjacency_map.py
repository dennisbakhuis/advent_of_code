"""Build an adjacency map from coordinates."""

from typing import Iterable


from ..types import AdjacencyMap, Coordinate
from ..constants import ADJACENCY_DELTAS, ADJACENCY_DELTAS_WITH_DIAGONALS


def adjacency_map(
    coordinates: Iterable[Coordinate],
    diagonal_sides: bool = False,
) -> AdjacencyMap:
    """
    Precompute the adjacency map for a given set of coordinates.

    Parameters
    ----------
    coordinates : Iterable[Coordinate]
        The list of coordinates to build the adjacency map for.
    diagonal_sides : bool, optional
        Whether to include diagonal adjacency, by default False

    Returns
    -------
    AdjacencyMap
        A dictionary mapping each coordinate to its set of adjacent coordinates.
    """
    coord_set = set(coordinates)
    deltas = ADJACENCY_DELTAS_WITH_DIAGONALS if diagonal_sides else ADJACENCY_DELTAS
    adjacency_map: AdjacencyMap = {coord: set() for coord in coord_set}

    for x, y in coord_set:
        for dx, dy in deltas:
            adjacent = (x + dx, y + dy)
            if adjacent in coord_set:
                adjacency_map[(x, y)].add(adjacent)

    return adjacency_map
