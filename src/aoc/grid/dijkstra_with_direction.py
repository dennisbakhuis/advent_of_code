"""Dijkstra algorithm to find the shortest path to all coordinates."""

import heapq
from typing import Iterable

from ..types import (
    Coordinate,
    Direction,
    DijkstraDirectionScoringFunction,
    DijkstraDirectionPathTree,
)
from ..constants import UNREACHABLE
from .adjacency_map import adjacency_map
from .scoring_functions import manhatten_scoring


def dijkstra_with_direction(
    coordinates: Iterable[Coordinate],
    start: Coordinate,
    start_direction: Direction = Direction.EAST,
    scoring_function: DijkstraDirectionScoringFunction = manhatten_scoring,
) -> DijkstraDirectionPathTree:
    """
    Dijkstra algorithm to find the shortest path to all coordinates with additional direction weighting.

    Parameters
    ----------
    coordinates : Iterable[Coordinate]
        The coordinates to search.
    start : Coordinate
        The starting coordinate.
    start_direction : Direction, optional
        The starting direction, by default Direction.EAST
    scoring_function : Dijkstra_Scoring_Function, optional
        The scoring function, by default manhatten_scoring

    Returns
    -------
    dijkstra_path_tree : DijkstraDirectionPathTree
    """
    seen_states: DijkstraDirectionPathTree = {
        coordinate: {
            direction: {"score": UNREACHABLE, "tiles": set(), "parent": None}
            for direction in Direction
        }
        for coordinate in coordinates
    }
    seen_states[start][start_direction]["score"] = 0
    queue = [(0, start, set(), start_direction)]

    adjacency_lookup_table = adjacency_map(coordinates)

    while queue:
        score, location, tiles, direction = heapq.heappop(queue)
        adjacent = adjacency_lookup_table[location] - tiles

        for new_location in adjacent:
            new_direction = Direction.from_coordinates(location, new_location)

            state = seen_states[new_location][new_direction]
            new_score = score + scoring_function(location, new_location, direction, new_direction)

            if new_score > state["score"]:
                continue
            state["score"] = new_score

            new_tiles = tiles | {new_location}

            if new_score < state["score"]:  # pragma: no cover
                state["parent"] = location
                state["tiles"] = new_tiles
            elif new_score == state["score"]:
                if state["parent"] is None:
                    state["parent"] = location
                state["tiles"] |= new_tiles

            heapq.heappush(queue, (new_score, new_location, state["tiles"], new_direction))

    return seen_states
