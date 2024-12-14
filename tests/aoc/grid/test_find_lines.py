"""Test cases for the find_lines function."""

from aoc.grid import find_lines


def test_empty_input():
    """Returns empty set when input coordinates are empty."""
    coordinates = []
    minimal_line_length = 2
    expected = set()
    assert find_lines(coordinates, minimal_line_length) == expected


def test_single_point():
    """Does not return lines when only one point is provided."""
    coordinates = [(0, 0)]
    minimal_line_length = 2
    expected = set()
    assert find_lines(coordinates, minimal_line_length) == expected


def test_horizontal_lines():
    """Identifies horizontal lines correctly."""
    coordinates = [(1, 2), (2, 2), (3, 2), (5, 2)]
    minimal_line_length = 3
    expected = {frozenset({(1, 2), (2, 2), (3, 2)})}
    assert find_lines(coordinates, minimal_line_length) == expected


def test_vertical_lines():
    """Identifies vertical lines correctly."""
    coordinates = [(4, 1), (4, 2), (4, 3), (4, 5)]
    minimal_line_length = 3
    expected = {frozenset({(4, 1), (4, 2), (4, 3)})}
    assert find_lines(coordinates, minimal_line_length) == expected


def test_diagonal_lines():
    """Identifies diagonal lines when enabled."""
    coordinates = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 5)]
    minimal_line_length = 3
    expected = {frozenset({(0, 0), (1, 1), (2, 2), (3, 3)})}
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=True) == expected


def test_no_diagonal_lines():
    """Does not identify diagonal lines when disabled."""
    coordinates = [(0, 0), (1, 1), (2, 2), (3, 3)]
    minimal_line_length = 2
    expected = set()
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=False) == expected


def test_mixed_lines():
    """Identifies mixed horizontal, vertical, and diagonal lines."""
    coordinates = [
        (0, 0),
        (1, 0),
        (2, 0),  # Horizontal
        (5, 1),
        (5, 2),
        (5, 3),  # Vertical
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (3, 3),  # Diagonal
    ]
    minimal_line_length = 3
    expected = {
        frozenset({(0, 0), (1, 0), (2, 0)}),
        frozenset({(5, 1), (5, 2), (5, 3)}),
        frozenset({(0, 0), (1, 1), (2, 2), (3, 3)}),
    }
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=True) == expected


def test_minimal_length():
    """Respects the minimal line length parameter."""
    coordinates = [(0, 0), (1, 0), (2, 0), (4, 0)]
    minimal_line_length = 4
    expected = set()
    assert find_lines(coordinates, minimal_line_length) == expected


def test_overlapping_lines():
    """Handles overlapping lines without duplication."""
    coordinates = [(0, 0), (1, 0), (2, 0), (3, 0), (1, 0), (2, 0), (3, 0), (4, 0)]
    minimal_line_length = 3
    expected = {frozenset({(0, 0), (1, 0), (2, 0), (3, 0), (4, 0)})}
    assert find_lines(coordinates, minimal_line_length) == expected


def test_duplicate_points():
    """Ignores duplicate points in the input."""
    coordinates = [(0, 0), (1, 1), (1, 1), (2, 2), (3, 3)]
    minimal_line_length = 3
    expected = {frozenset({(0, 0), (1, 1), (2, 2), (3, 3)})}
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=True) == expected


def test_non_consecutive_points():
    """Identifies lines with non-consecutive points correctly."""
    coordinates = [(0, 0), (2, 2), (4, 4), (6, 6)]
    minimal_line_length = 2
    expected = {frozenset({(0, 0), (2, 2), (4, 4), (6, 6)})}
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=True) == expected


def test_multiple_diagonal_lines():
    """Identifies multiple diagonal lines correctly."""
    coordinates = [(0, 0), (1, 1), (2, 2), (0, 2), (1, 1), (2, 0)]
    minimal_line_length = 2
    expected = {
        frozenset({(0, 0), (1, 1), (2, 2)}),
        frozenset({(0, 2), (1, 1), (2, 0)}),
        frozenset({(0, 0), (2, 0)}),
        frozenset({(0, 2), (2, 2)}),
        frozenset({(2, 0), (2, 2)}),
        frozenset({(0, 0), (0, 2)}),
    }
    assert find_lines(coordinates, minimal_line_length, diagonal_sides=True) == expected
