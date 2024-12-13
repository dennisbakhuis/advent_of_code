"""Functions to find holes in a set of coordinates."""

from collections import deque
from typing import Iterable


def find_holes(
    coordinates: Iterable[tuple[int, int]],
) -> set[tuple[int, int]]:
    """
    Find all "holes" (enclosed empty cells) within a given set of coordinates.

    Parameters
    ----------
    coordinates : Iterable[tuple[int, int]]
        An iterable of 2D coordinates (x, y), representing occupied cells.

    Returns
    -------
    set[tuple[int, int]]
        A set of 2D coordinates (x, y) that are "holes," i.e., enclosed empty cells
        that are completely surrounded by occupied cells.

    Notes
    -----
    - The function considers the smallest bounding box that contains all the given
      coordinates and identifies the empty cells within this box.
    - Any empty cells directly connected to the outside of the bounding box are
      not considered holes.
    """
    coordinates = set(coordinates)
    if not coordinates:
        return set()

    min_x = min(x for x, _ in coordinates)
    max_x = max(x for x, _ in coordinates)
    min_y = min(y for _, y in coordinates)
    max_y = max(y for _, y in coordinates)

    empty_cells = {
        (x, y)
        for x in range(min_x, max_x + 1)
        for y in range(min_y, max_y + 1)
        if (x, y) not in coordinates
    }

    outside_min_x, outside_max_x = min_x - 1, max_x + 1
    outside_min_y, outside_max_y = min_y - 1, max_y + 1

    visited = set()
    queue = deque()

    for x in range(outside_min_x, outside_max_x + 1):
        for y in (outside_min_y, outside_max_y):
            if (x, y) not in coordinates:
                visited.add((x, y))
                queue.append((x, y))
    for y in range(outside_min_y, outside_max_y + 1):
        for x in (outside_min_x, outside_max_x):
            if (x, y) not in coordinates:
                visited.add((x, y))
                queue.append((x, y))

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if outside_min_x <= nx <= outside_max_x and outside_min_y <= ny <= outside_max_y:
                if (nx, ny) not in coordinates and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    return empty_cells - visited
