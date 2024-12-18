"""Fast way to find the shortest path to all coordinates."""

from collections import deque
from typing import Iterable

from ..types import Coordinate
from ..constants import UNREACHABLE


def find_shortest_path(
    coordinates: Iterable[Coordinate],
    start: Coordinate,
    end: Coordinate,
) -> list[Coordinate]:
    """
    Find the shortest path between two coordinates.

    Parameters
    ----------
    coordinates : Iterable[Coordinate]
        The coordinates to search.
    start : Coordinate
        The starting coordinate.
    end : Coordinate
        The ending coordinate.

    Returns
    -------
    list[Coordinate]
        The shortest path between the two coordinates.
    """
    coords_set = set(coordinates)
    prev = {}
    dist = {c: UNREACHABLE for c in coords_set}
    dist[start] = 0
    prev[start] = None

    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        d = dist[(x, y)]
        if (x, y) == end:
            path = []
            cur = end
            while cur is not None:
                path.append(cur)
                cur = prev[cur]
            return path[::-1]

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if (nx, ny) in coords_set and dist[(nx, ny)] > d + 1:
                dist[(nx, ny)] = d + 1
                prev[(nx, ny)] = (x, y)
                queue.append((nx, ny))

    return []
