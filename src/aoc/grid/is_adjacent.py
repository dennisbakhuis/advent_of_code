"""Functions for determining adjacency between coordinates in a grid."""

from typing import Iterable

_CROSS_OFFSETS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
_DIAGONAL_OFFSETS = [(-1, -1), (1, -1), (-1, 1), (1, 1)]


def is_adjacent(
    coordinate: tuple[int, int],
    test_coordinates: tuple[int, int] | Iterable[tuple[int, int]],
    cross_sides: bool = True,
    diagonal_sides: bool = False,
) -> bool:
    """
    Determine if a coordinate is adjacent to another coordinate or any coordinate in a list.

    Adjacency can be defined based on cardinal directions (left, right, above, below)
    and optionally including diagonal directions.

    Parameters
    ----------
    coordinate : tuple of int
        The coordinate to test, represented as a tuple (x, y).
    test_coordinates : tuple of int or iterable of tuples of int
        A single coordinate or an iterable of coordinates to check adjacency against.
    cross_sides : bool, optional
        If `True`, considers adjacency on the four cardinal directions
        (left, right, above, below). Default is `True`.
    diagonal_sides : bool, optional
        If `True`, also considers diagonal adjacency. Default is `False`.

    Returns
    -------
    bool
        `True` if `coord` is adjacent to any of the `other_coords` based on the specified parameters,
        `False` otherwise.
    """
    # Define the relative positions for adjacency
    deltas = []
    if cross_sides:
        deltas.extend(_CROSS_OFFSETS)
    if diagonal_sides:
        deltas.extend(_DIAGONAL_OFFSETS)

    # Generate adjacent coordinates
    adjacent = set((coordinate[0] + dx, coordinate[1] + dy) for dx, dy in deltas)

    # Check if other_coords is a single tuple or an iterable
    if (
        isinstance(test_coordinates, tuple)
        and len(test_coordinates) == 2
        and all(isinstance(n, int) for n in test_coordinates)
    ):
        return test_coordinates in adjacent
    else:
        # Assume other_coords is an iterable of tuples
        return any(other in adjacent for other in test_coordinates)
