"""Find surrounding coordinates of a point or list of points."""

from typing import Iterable


_CROSS_OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
_DIAGONAL_OFFSETS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]


def surrounding(
    coordinates: tuple[int, int] | Iterable[tuple[int, int]],
    bounds: tuple[int, int, int, int] | None = None,
    cross_sides: bool = True,
    diagonal_sides: bool = False,
) -> set[tuple[int, int]]:
    """
    Retrieve surrounding coordinates for given coordinate(s) on the ASCII map.

    Parameters
    ----------
    coordinates : tuple of int or list of tuple of int
        The coordinate or list of coordinates for which to find surrounding positions.
        Each coordinate is a tuple in the form (x, y).
    bounds : tuple of int, optional
        The bounds within which the surrounding coordinates must lie, defined as
        (min_x, min_y, max_x, max_y). Default is (0, 0, 32, 32).
    cross_sides : bool, optional
        If True, include the four orthogonal (cross) surrounding coordinates:
        left, right, above, and below. Default is True.
    diagonal_sides : bool, optional
        If True, include the four diagonal surrounding coordinates:
        top-left, top-right, bottom-left, and bottom-right. Default is False.

    Returns
    -------
    set of tuple of int
        A set containing all valid surrounding coordinates as tuples (x, y).
    """
    if isinstance(coordinates, tuple):
        coordinates = [coordinates]

    min_x, min_y, max_x, max_y = bounds if bounds is not None else (0, 0, 0, 0)
    surrounding_coordinates = set()

    for x, y in coordinates:
        if cross_sides:
            for dx, dy in _CROSS_OFFSETS:
                new_x, new_y = x + dx, y + dy

                if bounds is None or (min_x <= new_x <= max_x and min_y <= new_y <= max_y):
                    surrounding_coordinates.add((new_x, new_y))

        if diagonal_sides:
            for dx, dy in _DIAGONAL_OFFSETS:
                new_x, new_y = x + dx, y + dy

                if bounds is None or (min_x <= new_x <= max_x and min_y <= new_y <= max_y):
                    surrounding_coordinates.add((new_x, new_y))

    return surrounding_coordinates
