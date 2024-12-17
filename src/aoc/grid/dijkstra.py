"""Dijkstra algorithm to find the shortest path to all coordinates."""

import heapq
from typing import Iterable, Callable

from ..types import Coordinate, Direction
from .adjacency_map import adjacency_map


UNREACHABLE = float("inf")

# Format for the scoring function
# A function that needs the following signature:
# def scoring_function(
#   previous location: Coordinate,
#   current_location: Coordinate,
#   previous_direction: Coordinate,
#   current_direction: : Coordinate,
# ) -> int:
Dijkstra_Scoring_Function = Callable[[Coordinate, Coordinate, Direction, Direction], int]


def manhatten_scoring(*args, **kwargs) -> int:
    """Manhattan scoring function, simply returning 1 for each step."""
    return 1


def dijkstra(
    coordinates: Iterable[Coordinate],
    start: Coordinate,
    scoring_function: Dijkstra_Scoring_Function = manhatten_scoring,
) -> dict:
    """Dijkstra algorithm to find the shortest path to all coordinates."""
    queue = [(0, start, set(), Direction.EAST)]

    seen_states = {
        coordinate: {direction: {"score": UNREACHABLE, "tiles": set()} for direction in Direction}
        for coordinate in coordinates
    }

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
                state["tiles"] = new_tiles
            elif new_score == state["score"]:
                state["tiles"] |= new_tiles

            heapq.heappush(queue, (new_score, new_location, state["tiles"], new_direction))
    return seen_states
