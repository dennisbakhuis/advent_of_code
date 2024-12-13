"""Function to find the corners of a set of coordinates."""

from typing import Iterable
from collections import defaultdict


def count_corners(
    coordinates: Iterable[tuple[int, int]],
    style: str = "minecraft",
) -> int:
    """
    Count the number of corners in the polygon formed by a connected set of filled unit squares.

    There are different styles of corner counting, depending on the context.

    Styles implemented:
    - "minecraft": Only corners formed by horizontal and vertical sides are counted.

    Parameters
    ----------
    coordinates : Iterable[tuple[int, int]]
        The coordinates of the filled unit squares.
    style : str, optional
        The style of the grid (default "minecraft").

    Returns
    -------
    int
        The number of corners in the resulting polygon.
    """
    coordinates = set(coordinates)
    if not coordinates:
        return 0

    if style == "minecraft":
        cell_edges = []
        for x, y in coordinates:
            edges = [
                ((x, y), (x + 1, y)),
                ((x + 1, y), (x + 1, y + 1)),
                ((x, y + 1), (x + 1, y + 1)),
                ((x, y), (x, y + 1)),
            ]
            cell_edges.extend(tuple(sorted(edges)))

        edge_count = defaultdict(int)
        for e in cell_edges:
            edge_count[e] += 1
        boundary_edges = [e for e, c in edge_count.items() if c == 1]

        adjacency = defaultdict(list)
        for (x1, y1), (x2, y2) in boundary_edges:
            adjacency[(x1, y1)].append((x2, y2))
            adjacency[(x2, y2)].append((x1, y1))

        start = min(adjacency.keys(), key=lambda p: (p[1], p[0]))
        polygon = [start]
        current = start
        prev = None

        while True:
            neighbors = adjacency[current]
            nxt = (
                neighbors[0]
                if prev != neighbors[0]
                else neighbors[1]
                if len(neighbors) > 1
                else None
            )
            if nxt == start and len(polygon) > 1:
                break
            polygon.append(nxt)
            prev, current = current, nxt

        corners = 0
        for i in range(len(polygon)):
            A = polygon[i - 2]
            B = polygon[i - 1]
            C = polygon[i]
            AB = (B[0] - A[0], B[1] - A[1])
            BC = (C[0] - B[0], C[1] - B[1])
            if (AB[0] == 0 and BC[1] == 0) or (AB[1] == 0 and BC[0] == 0):
                corners += 1
    else:
        raise ValueError(f"Unknown style: {style}")

    return corners
