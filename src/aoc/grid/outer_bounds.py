"""Function for finding the outer bounds of a set of coordinates."""

from typing import Iterable


def outer_bounds(
    coordinates: Iterable[tuple[int, int]],
    diagonal_sides: bool = False,
) -> set[tuple[int, int]]:
    """
    Find the outer_bounds of a given set of coordinates.

    Parameters
    ----------
    coordinates : Iterable[tuple[int,int]]
        An iterable of (x,y) coordinates representing a filled area.
    diagonal_sides : bool, optional
        If True, diagonals are considered adjacent.

    Returns
    -------
    set[tuple[int,int]]
        The perimeter points.
    """
    coords = set(coordinates)
    if diagonal_sides:
        directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    else:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    bounds = set()
    for x, y in coords:
        for dx, dy in directions:
            if (x + dx, y + dy) not in coords:
                bounds.add((x, y))
                break
    return bounds
