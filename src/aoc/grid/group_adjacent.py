"""Function for grouping adjacent coordinates."""

from typing import Iterable


def group_adjacent(
    coordinates: Iterable[tuple[int, int]],
    cross_sides: bool = True,
    diagonal_sides: bool = False,
) -> set[frozenset[tuple[int, int]]]:
    """
    Group coordinates by adjacency.

    Parameters
    ----------
    coords : iterable of (int, int)
        The coordinates to group.
    cross_sides : bool, optional
        If True, consider horizontal/vertical adjacency (default True).
    diagonal_sides : bool, optional
        If True, consider diagonal adjacency (default False).

    Returns
    -------
    set of frozenset
        A set of frozensets, each containing connected coordinates.
    """
    coordinates = set(coordinates)
    adj = []
    if cross_sides:
        adj += [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if diagonal_sides:
        adj += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

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
                for dx, dy in adj:
                    n = (cur[0] + dx, cur[1] + dy)
                    if n in coordinates and n not in visited:
                        stack.append(n)
            groups.add(frozenset(group))
    return groups
