"""Function for grouping adjacent coordinates."""

from typing import Iterable

from ..types import Coordinate
from ..constants import ADJACENCY_DELTAS, ADJACENCY_DELTAS_ONLY_DIAGONALS


def group_adjacent(
    coordinates: Iterable[Coordinate],
    cross_sides: bool = True,
    diagonal_sides: bool = False,
) -> set[frozenset[Coordinate]]:
    """
    Group coordinates by adjacency.

    Parameters
    ----------
    coords : iterable of Coordinate
        The coordinates to group.
    cross_sides : bool, optional
        If True, consider horizontal and vertical adjacency (default True).
    diagonal_sides : bool, optional
        If True, consider diagonal adjacency (default False).

    Returns
    -------
    set of frozenset[Coordinate]
        A set of frozensets, each containing connected coordinates.
    """
    coordinates = set(coordinates)

    deltas = ADJACENCY_DELTAS if cross_sides else set()
    if diagonal_sides:
        deltas |= ADJACENCY_DELTAS_ONLY_DIAGONALS

    visited = set()
    groups = set()
    for c in coordinates:
        if c not in visited:
            stack = [c]
            group = set()
            while stack:
                cur = stack.pop()
                if cur in visited:
                    continue
                visited.add(cur)
                group.add(cur)
                for dx, dy in deltas:
                    n = (cur[0] + dx, cur[1] + dy)
                    if n in coordinates and n not in visited:
                        stack.append(n)
            groups.add(frozenset(group))
    return groups
