"""General types used in AoC."""

from typing import Callable

from .coordinate import Coordinate
from .direction import Direction


AdjacencyMap = dict[Coordinate, set[Coordinate]]

Bounds = tuple[int, int, int, int]  # (min_x, min_y, max_x, max_y)

DijkstraScoringFunction = Callable[[Coordinate, Coordinate], int]
DijkstraPathTree = dict[Coordinate, dict[str, int | list]]

DijkstraDirectionScoringFunction = Callable[[Coordinate, Coordinate, Direction, Direction], int]
DijkstraDirectionPathTree = dict[
    Coordinate, dict[Direction, dict[str, int | list | Coordinate | None]]
]
