"""Dijkstra algorithm to find the shortest path to all coordinates."""

import heapq
from typing import Iterable

from ..types import Coordinate, DijkstraScoringFunction, DijkstraPathTree
from ..constants import UNREACHABLE
from .scoring_functions import manhatten_scoring


def dijkstra(
    coordinates: Iterable[Coordinate],
    start: Coordinate,
    scoring_function: DijkstraScoringFunction = manhatten_scoring,
) -> DijkstraPathTree:
    """
    Dijkstra algorithm to find the shortest path to all coordinates.

    Parameters
    ----------
    coordinates : Iterable[Coordinate]
        The coordinates to search.
    start : Coordinate
        The starting coordinate.
    scoring_function : DijkstraScoringFunction, optional
        The scoring function, by default default_scoring_func

    Returns
    -------
    dijkstra_path_tree : DijkstraPathTree
    """
    coords = set(coordinates)
    path_tree: DijkstraPathTree = {c: {"score": UNREACHABLE, "tiles": []} for c in coords}
    path_tree[start]["score"] = 0
    prev = {c: None for c in coords}

    queue = [(0, start)]
    while queue:
        score, location = heapq.heappop(queue)
        if score > path_tree[location]["score"]:
            continue

        x, y = location
        for new_location in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if new_location in coords:
                new_score = score + scoring_function(location, new_location)
                if new_score < path_tree[new_location]["score"]:
                    path_tree[new_location]["score"] = new_score
                    prev[new_location] = location
                    heapq.heappush(queue, (new_score, new_location))

    # Reconstruct paths
    for c in coords:
        if path_tree[c]["score"] != UNREACHABLE and c != start:
            path = []
            curr = c
            while curr is not None and curr != start:
                path.append(curr)
                curr = prev[curr]
            path.reverse()
            path_tree[c]["tiles"] = path

    return path_tree
