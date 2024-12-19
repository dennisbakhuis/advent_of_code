"""Find adjacent coordinates in a list of coordinates."""

from typing import Iterable

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
    adjacent_candidates = (
        coordinate.adjacent_with_diagonal if diagonal_sides else coordinate.adjacent
    )

    return {candidate for candidate in adjacent_candidates if candidate in coordinates}
