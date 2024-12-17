"""General types used in AoC."""

from typing import NewType


Coordinate = NewType("Coordinate", tuple[int, int])
AdjacencyMap = dict[Coordinate, set[Coordinate]]
