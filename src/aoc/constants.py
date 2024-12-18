"""Constants for grid module."""

ADJACENCY_DELTAS = frozenset(
    {
        (0, -1),
        (-1, 0),
        (1, 0),
        (0, 1),
    }
)

ADJACENCY_DELTAS_ONLY_DIAGONALS = frozenset(
    {
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1),
    }
)

ADJACENCY_DELTAS_WITH_DIAGONALS = ADJACENCY_DELTAS | ADJACENCY_DELTAS_ONLY_DIAGONALS

UNREACHABLE = float("inf")
