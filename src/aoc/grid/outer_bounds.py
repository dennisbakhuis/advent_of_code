"""Function for finding the outer bounds of a set of coordinates."""

from typing import Iterable

from ..types import Coordinate


def outer_bounds(
    coordinates: Iterable[Coordinate],
    diagonal_sides: bool = False,
) -> set[Coordinate]:
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

    bounds = set()
    for coordinate in coords:
        candidates = coordinate.adjacent_with_diagonal if diagonal_sides else coordinate.adjacent
        for candidate in candidates:
            if candidate not in coords:
                bounds.add(coordinate)
                break

    return bounds

    # if diagonal_sides:
    #     directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
    # else:
    #     directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    # bounds = set()
    # for x, y in coords:
    #     for dx, dy in directions:
    #         if (x + dx, y + dy) not in coords:
    #             bounds.add((x, y))
    #             break
    # return bounds
