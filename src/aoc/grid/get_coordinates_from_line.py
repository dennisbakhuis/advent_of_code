"""Get coordinates from a straight line between two points."""

from .within_bounds import within_bounds
from ..types import Coordinate


def get_coordinates_from_line(
    start: Coordinate,
    end: Coordinate,
    bounds: tuple[int, int, int, int] | None = None,
) -> set[Coordinate]:
    """
    Retrieve all coordinates on a straight line between start and end positions.

    This method approximates any straight line between two points using Bresenham's algorithm.

    Parameters
    ----------
    start : Coordinate
        The starting coordinate as (x, y).
    end : Coordinate
        The ending coordinate as (x, y).
    bounds : tuple of int, optional
        The boundaries as (min_x, min_y, max_x, max_y). If None, all coordinates are considered valid.

    Returns
    -------
    set[Coordinate]
        A set containing all coordinates on the line from start to end, inclusive (x, y).

    Raises
    ------
    ValueError
        If any coordinate on the line is out of the specified bounds.
    """
    start_x, start_y = start
    end_x, end_y = end

    if start == end:
        if bounds is not None and not within_bounds((start_x, start_y), bounds):
            raise ValueError(f"Coordinate {start} is out of bounds.")
        else:
            return {(start_x, start_y)}

    coordinates_on_line = set()

    dx = abs(end_x - start_x)
    dy = abs(end_y - start_y)
    x, y = start_x, start_y

    sx = 1 if end_x > start_x else -1
    sy = 1 if end_y > start_y else -1

    if dx > dy:
        err = dx / 2.0
        while x != end_x:
            if bounds is not None and not within_bounds((x, y), bounds):
                raise ValueError(f"Coordinate ({x}, {y}) is out of bounds.")
            coordinates_on_line.add((x, y))
            err -= dy
            if err < 0:
                y += sy
                err += dx
            x += sx
    else:
        err = dy / 2.0
        while y != end_y:
            if bounds is not None and not within_bounds((x, y), bounds):
                raise ValueError(f"Coordinate ({x}, {y}) is out of bounds.")
            coordinates_on_line.add((x, y))
            err -= dx
            if err < 0:
                x += sx
                err += dy
            y += sy

    if bounds is not None and not within_bounds((end_x, end_y), bounds):
        raise ValueError(f"Coordinate ({end_x}, {end_y}) is out of bounds.")
    coordinates_on_line.add((end_x, end_y))

    return coordinates_on_line
