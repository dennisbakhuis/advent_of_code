"""Function to identify groups of coordinates that form lines in a grid."""

from collections import defaultdict
from math import gcd
from itertools import combinations
from typing import Iterable

from ..types import Coordinate


def find_lines(
    coordinates: Iterable[Coordinate], minimal_line_length: int, diagonal_sides: bool = False
) -> set[frozenset[Coordinate]]:
    """
    Identify groups of coordinates that form horizontal, vertical, and optionally diagonal lines.

    Lines have at least a specified minimal length in a grid.

    Parameters
    ----------
    coordinates : Tuple[Coordinate, ...]
        A tuple of (x, y) tuples representing coordinates on a grid.
    minimal_line_length : int
        The minimal number of points required to form a line.
    diagonal_sides : bool, optional
        If True, includes diagonal lines (arbitrary straight lines) in addition to horizontal
        and vertical lines. Default is False.

    Returns
    -------
    Tuple[Set[Coordinate], ...]
        A tuple where each element is a set of (x, y) tuples representing a line that meets
        the criteria.
    """
    points_set = set(coordinates)
    lines = []

    # Horizontal lines
    y_to_x = defaultdict(list)
    for x, y in points_set:
        y_to_x[y].append(x)

    for y, x_coords in y_to_x.items():
        sorted_x = sorted(x_coords)
        current_line = [sorted_x[0]]
        for x in sorted_x[1:]:
            if x == current_line[-1] + 1:
                current_line.append(x)
            else:
                if len(current_line) >= minimal_line_length:
                    line = {(x_val, y) for x_val in current_line}
                    lines.append(line)
                current_line = [x]
        if len(current_line) >= minimal_line_length:
            line = {(x_val, y) for x_val in current_line}
            lines.append(line)

    # Vertical lines
    x_to_y = defaultdict(list)
    for x, y in points_set:
        x_to_y[x].append(y)

    for x, y_coords in x_to_y.items():
        sorted_y = sorted(y_coords)
        current_line = [sorted_y[0]]
        for y in sorted_y[1:]:
            if y == current_line[-1] + 1:
                current_line.append(y)
            else:
                if len(current_line) >= minimal_line_length:
                    line = {(x, y_val) for y_val in current_line}
                    lines.append(line)
                current_line = [y]
        if len(current_line) >= minimal_line_length:
            line = {(x, y_val) for y_val in current_line}
            lines.append(line)

    if diagonal_sides:
        # Function to normalize line representation
        def normalize_line(x1, y1, x2, y2):
            A = y2 - y1
            B = x1 - x2
            C = x2 * y1 - x1 * y2
            divisor = gcd(gcd(abs(A), abs(B)), abs(C))
            if divisor != 0:
                A //= divisor
                B //= divisor
                C //= divisor
            # Ensure consistent representation
            if A < 0 or (A == 0 and B < 0):
                A, B, C = -A, -B, -C
            return (A, B, C)

        lines_dict = defaultdict(set)
        points = list(points_set)
        for (x1, y1), (x2, y2) in combinations(points, 2):
            # if x1 == x2 and y1 == y2:
            #     continue  # Same point
            line_key = normalize_line(x1, y1, x2, y2)
            lines_dict[line_key].add((x1, y1))
            lines_dict[line_key].add((x2, y2))

        for line_points in lines_dict.values():
            if len(line_points) >= minimal_line_length:
                # To ensure lines are maximal, we need to check if all points lie on the same line
                # Already ensured by grouping, so add as a set
                lines.append(set(line_points))

    # Remove duplicate lines by converting list of sets to list of frozensets
    unique_lines = set(frozenset(line) for line in lines if len(line) >= minimal_line_length)

    # Convert back to tuple of sets
    return unique_lines
