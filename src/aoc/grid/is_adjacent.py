"""Functions for determining adjacency between coordinates in a grid."""

from typing import Iterable

from ..types import Coordinate


def is_adjacent(
    coordinate: Coordinate,
    other_coordinates: Coordinate | Iterable[Coordinate],
    diagonal_sides: bool = False,
) -> bool:
    """
    Determine if a coordinate is adjacent to another coordinate or any coordinate in a list.

    Adjacency can be defined based on cardinal directions (left, right, above, below)
    and optionally including diagonal directions.

    Parameters
    ----------
    coordinate : Coordinate | int
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
    adjacent_candidates = (
        coordinate.adjacent_with_diagonal if diagonal_sides else coordinate.adjacent
    )

    if isinstance(other_coordinates, tuple) and isinstance(other_coordinates[0], int):
        return other_coordinates in adjacent_candidates
    else:
        return any(other in adjacent_candidates for other in other_coordinates)
