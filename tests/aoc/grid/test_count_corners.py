"""
Test module for the count_corners function.

This module tests various input configurations for the `count_corners` function,
ensuring that it returns the correct number of corners for polygons formed by
connected unit squares under the "minecraft" style.
"""

import pytest
from aoc.grid import count_corners


def test_empty_coordinates():
    """
    Test that no coordinates return zero corners.

    Ensures that an empty input results in zero corners.
    """
    assert count_corners([]) == 0


def test_single_square():
    """
    Test a single square.

    A single unit square forms a polygon with 4 corners.
    """
    coords = [(0, 0)]
    assert count_corners(coords) == 4


def test_two_squares_horizontal():
    """
    Test two squares in a horizontal line.

    Two adjacent squares along the x-axis form a rectangular shape with 4 corners.
    """
    coords = [(0, 0), (1, 0)]
    assert count_corners(coords) == 4


def test_two_squares_vertical():
    """
    Test two squares in a vertical line.

    Two adjacent squares along the y-axis form a rectangular shape with 4 corners.
    """
    coords = [(0, 0), (0, 1)]
    assert count_corners(coords) == 4


def test_three_squares_in_a_line():
    """
    Test three squares in a horizontal line.

    Three adjacent squares horizontally form a polygon with 4 corners (ends only).
    """
    coords = [(0, 0), (1, 0), (2, 0)]
    assert count_corners(coords) == 4


def test_l_shaped_figure():
    """
    Test an L-shaped configuration.

    This shape (like coordinates for squares at (0,0), (1,0), (0,1)) forms a cornered polygon
    with 6 corners.
    """
    coords = [(0, 0), (1, 0), (0, 1)]
    assert count_corners(coords) == 6


def test_square_block_2x2():
    """
    Test a 2x2 block of squares.

    A 2x2 block forms a larger square with 4 corners.
    """
    coords = [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert count_corners(coords) == 4


def test_plus_shaped_figure():
    """
    Test a plus (+) shaped figure.

    Coordinates arranged in a plus shape form a polygon with 12 corners.
    For example:
      (0,0)
      (0,1)
    (-1,0) (0,0) (1,0)
      (0,-1)

    The outline is an eight-pointed shape with concave areas resulting in 12 corners.
    """
    coords = [(-1, 0), (0, 0), (1, 0), (0, 1), (0, -1)]
    assert count_corners(coords) == 12


def test_unknown_style():
    """
    Test passing an unknown style.

    Passing an unknown style should raise a ValueError.
    """
    with pytest.raises(ValueError):
        count_corners([(0, 0)], style="unknown")
