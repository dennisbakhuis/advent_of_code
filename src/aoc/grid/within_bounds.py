"""Test if coordinates or a list of coordinates are within bounds of a grid."""

from typing import Iterable


def within_bounds(
    coordinates: tuple[int, int] | Iterable[tuple[int, int]],
    bounds: tuple[int, int, int, int],
) -> bool:
    """
    Test if coordinates or a list of coordinates are within bounds of a grid.

    Parameters
    ----------
    coordinates : tuple[int, int] or list/set/tuple of (int, int)
        Coordinates to test.
    bounds : tuple[int, int, int, int]
        Bounds of the grid (left, top, right, bottom).

    Returns
    -------
    bool
        True if all coordinates are within bounds, False otherwise.
    """
    left, top, right, bottom = bounds

    if not coordinates:
        return True

    if isinstance(coordinates, tuple) and isinstance(coordinates[0], int):
        return left <= coordinates[0] <= right and top <= coordinates[1] <= bottom

    return all(left <= x <= right and top <= y <= bottom for x, y in coordinates)
