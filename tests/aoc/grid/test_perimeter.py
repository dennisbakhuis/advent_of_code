"""
Test module for the `perimeter` function.

This module contains a suite of tests to verify the correctness of the `perimeter` function,
which calculates the perimeter of a group of connected coordinates based on different styles.
All tests are conducted using the "minecraft" style by default.
"""

import pytest
from aoc.grid import perimeter


def test_empty_coordinates():
    """
    Test that an empty set of coordinates returns a perimeter of zero.

    Ensures that providing no coordinates results in a perimeter of 0.
    """
    assert perimeter(set()) == 0


def test_single_square():
    """
    Test the perimeter of a single square.

    A single unit square should have a perimeter of 4.
    """
    coords = {(0, 0)}
    assert perimeter(coords) == 4


def test_two_squares_horizontal():
    """
    Test the perimeter of two horizontally adjacent squares.

    Two squares placed side by side horizontally should have a combined perimeter of 6.
    """
    coords = {(0, 0), (1, 0)}
    assert perimeter(coords) == 6


def test_two_squares_vertical():
    """
    Test the perimeter of two vertically adjacent squares.

    Two squares stacked vertically should have a combined perimeter of 6.
    """
    coords = {(0, 0), (0, 1)}
    assert perimeter(coords) == 6


def test_three_squares_horizontal():
    """
    Test the perimeter of three horizontally aligned squares.

    Three squares in a horizontal line should have a combined perimeter of 8.
    """
    coords = {(0, 0), (1, 0), (2, 0)}
    assert perimeter(coords) == 8


def test_three_squares_L_shape():
    """
    Test the perimeter of an L-shaped configuration of squares.

    An L-shape formed by three squares should have a perimeter of 8.
    """
    coords = {(0, 0), (1, 0), (0, 1)}
    assert perimeter(coords) == 8


def test_two_by_two_block():
    """
    Test the perimeter of a 2x2 block of squares.

    A 2x2 block should have a perimeter of 8.
    """
    coords = {(0, 0), (1, 0), (0, 1), (1, 1)}
    assert perimeter(coords) == 8


def test_plus_shaped_figure():
    """
    Test the perimeter of a plus-shaped configuration of squares.

    A plus shape formed by five squares should have a perimeter of 12.
    """
    coords = {(-1, 0), (0, 0), (1, 0), (0, 1), (0, -1)}
    assert perimeter(coords) == 12


def test_complex_shape():
    """
    Test the perimeter of a complex shape formed by multiple squares.

    A more intricate arrangement of squares should correctly calculate the perimeter.
    Example shape:
        (0,0), (1,0), (2,0),
        (0,1),        (2,1),
        (0,2), (1,2), (2,2)
    This forms a hollow square with a missing center, resulting in a perimeter of 16.
    """
    coords = {(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)}
    assert perimeter(coords) == 16


def test_unknown_style():
    """
    Test that providing an unknown style raises a ValueError.

    Ensures that the function correctly handles unsupported styles by raising an exception.
    """
    coords = {(0, 0)}
    with pytest.raises(ValueError, match="Unknown style: unknown"):
        perimeter(coords, style="unknown")
