"""General types used in AoC."""

from typing import NewType, Callable

from .direction import Direction


Coordinate = NewType("Coordinate", tuple[int, int])
AdjacencyMap = dict[Coordinate, set[Coordinate]]

DijkstraScoringFunction = Callable[[Coordinate, Coordinate], int]
DijkstraPathTree = dict[Coordinate, dict[str, int | list]]

DijkstraDirectionScoringFunction = Callable[[Coordinate, Coordinate, Direction, Direction], int]
DijkstraDirectionPathTree = dict[
    Coordinate, dict[Direction, dict[str, int | list | Coordinate | None]]
]
