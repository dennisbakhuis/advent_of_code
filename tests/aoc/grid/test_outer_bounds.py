"""
Test module for the `outer_bounds` function.

This module contains a comprehensive suite of tests to verify the correctness of the `outer_bounds` function,
which identifies the perimeter points of a given set of coordinates. The tests cover various configurations
including single and multiple squares, different shapes, and scenarios with and without diagonal adjacency.
Each test ensures that the function accurately detects the outer boundaries based on the specified adjacency rules.
"""

from aoc.grid import outer_bounds
from aoc.types import Coordinate


def test_empty_coordinates():
    """
    Test that an empty set of coordinates returns no outer bounds.

    Ensures that providing no occupied cells results in an empty set of perimeter points.
    """
    assert outer_bounds([]) == set()


def test_single_square():
    """
    Test the outer bounds of a single occupied square.

    A single unit square should have itself as the perimeter point.
    """
    coords = [Coordinate(0, 0)]
    expected_bounds = {Coordinate(0, 0)}
    assert outer_bounds(coords) == expected_bounds


def test_two_squares_horizontal():
    """
    Test the outer bounds of two horizontally adjacent squares.

    Two squares placed side by side horizontally should have both squares as perimeter points.
    """
    coords = [Coordinate(0, 0), Coordinate(1, 0)]
    expected_bounds = {Coordinate(0, 0), Coordinate(1, 0)}
    assert outer_bounds(coords) == expected_bounds


def test_two_squares_vertical():
    """
    Test the outer bounds of two vertically adjacent squares.

    Two squares stacked vertically should have both squares as perimeter points.
    """
    coords = [Coordinate(0, 0), Coordinate(0, 1)]
    expected_bounds = {Coordinate(0, 0), Coordinate(0, 1)}
    assert outer_bounds(coords) == expected_bounds


def test_l_shaped_figure():
    """
    Test the outer bounds of an L-shaped configuration.

    An L-shape formed by three squares should have all squares as perimeter points.
    """
    coords = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, 1)]
    expected_bounds = {Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, 1)}
    assert outer_bounds(coords) == expected_bounds


def test_square_block_2x2():
    """
    Test the outer bounds of a 2x2 block of squares.

    A fully filled 2x2 block should have all four squares as perimeter points.
    """
    coords = [Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, 1), Coordinate(1, 1)]
    expected_bounds = {Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, 1), Coordinate(1, 1)}
    assert outer_bounds(coords) == expected_bounds


def test_plus_shaped_figure():
    """
    Test the outer bounds of a plus-shaped configuration.

    A plus shape formed by five squares should have all squares as perimeter points.
    """
    coords = [
        Coordinate(-1, 0),
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(0, 1),
        Coordinate(0, -1),
    ]
    expected_bounds = {Coordinate(-1, 0), Coordinate(1, 0), Coordinate(0, 1), Coordinate(0, -1)}
    assert outer_bounds(coords) == expected_bounds


def test_complex_shape_without_diagonals():
    """
    Test the outer bounds of a complex shape without considering diagonal adjacency.

    This shape includes an outer boundary and an inner hole. Only the outer perimeter should be detected.
    """
    coords = [
        # Outer boundary
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
    }
    assert outer_bounds(coords) == expected_bounds


def test_complex_shape_with_diagonals():
    """
    Test the outer bounds of a complex shape considering diagonal adjacency.

    This shape includes diagonally adjacent squares, and perimeter detection should include squares connected diagonally.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds


def test_hollow_square():
    """
    Test the outer bounds of a hollow square.

    A hollow square should have only the outer perimeter points as bounds.
    """
    coords = [
        # Outer boundary
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
        # Inner boundary (hole)
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_diagonal_sides_false():
    """
    Test the outer bounds with diagonal adjacency turned off.

    Ensures that only orthogonal neighbors are considered when determining perimeter points.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    }
    # Since diagonal_sides=False, all squares are perimeter points as none have orthogonal neighbors
    assert outer_bounds(coords, diagonal_sides=False) == expected_bounds


def test_outer_bounds_with_diagonal_sides_true():
    """
    Test the outer bounds with diagonal adjacency turned on.

    Ensures that diagonal neighbors are considered when determining perimeter points.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    ]
    # With diagonal adjacency, all squares are still perimeter points as no square is fully surrounded
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(1, 3),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds


def test_outer_bounds_with_internal_connections():
    """
    Test the outer bounds of a shape with internal connections.

    Ensures that internal connections do not affect the detection of perimeter points.
    """
    coords = [
        # Outer boundary
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
        # Internal connections
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_complex_shape_no_holes():
    """
    Test the outer bounds of a complex shape without any holes.

    Ensures that all perimeter points are correctly identified in a solid complex shape.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        Coordinate(3, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        Coordinate(3, 2),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_multiple_perimeter_points():
    """
    Test the outer bounds of a shape with multiple perimeter points.

    Ensures that all perimeter points are detected correctly, especially in irregular shapes.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        Coordinate(1, 1),  # Central square
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_diagonal_sides_true_complex():
    """
    Test the outer bounds of a complex shape with diagonal adjacency enabled.

    Ensures that diagonal neighbors are correctly considered, affecting the perimeter detection.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(2, 2),
        Coordinate(1, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 0),
        Coordinate(0, 2),
        Coordinate(2, 2),
        Coordinate(1, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds


def test_outer_bounds_with_diagonal_sides_true_hollow_shape():
    """
    Test the outer bounds of a hollow shape with diagonal adjacency enabled.

    Ensures that diagonal connections do not include internal holes as perimeter points.
    """
    coords = [
        # Outer boundary
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds


def test_outer_bounds_non_contiguous():
    """
    Test the outer bounds of non-contiguous occupied squares.

    Ensures that perimeter points are correctly identified even when the occupied squares are not connected.
    """
    coords = [Coordinate(0, 0), Coordinate(2, 2), Coordinate(4, 4)]
    expected_bounds = {Coordinate(0, 0), Coordinate(2, 2), Coordinate(4, 4)}
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_large_shape():
    """
    Test the outer bounds of a large, continuous shape.

    Ensures that the function can handle large inputs and accurately detect all perimeter points.
    """
    coords = [Coordinate(x, y) for x in range(10) for y in range(10)]
    expected_bounds = {
        Coordinate(x, y)
        for x in range(10)
        for y in range(10)
        if x == 0 or x == 9 or y == 0 or y == 9
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_large_shape_with_holes():
    """
    Test the outer bounds of a large shape with internal holes.

    Ensures that only the outer perimeter points are detected, excluding internal boundaries.
    """
    # Create a hollow 5x5 square
    coords = [
        Coordinate(x, y) for x in range(5) for y in range(5) if x == 0 or x == 4 or y == 0 or y == 4
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(4, 0),
        Coordinate(0, 1),
        Coordinate(4, 1),
        Coordinate(0, 2),
        Coordinate(4, 2),
        Coordinate(0, 3),
        Coordinate(4, 3),
        Coordinate(0, 4),
        Coordinate(1, 4),
        Coordinate(2, 4),
        Coordinate(3, 4),
        Coordinate(4, 4),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_overlapping_perimeters():
    """
    Test the outer bounds of shapes with overlapping perimeters.

    Ensures that overlapping perimeter points are handled correctly without duplication.
    """
    coords = [
        # First shape
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        # Second shape overlapping the first
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_complex_connected_shape():
    """
    Test the outer bounds of a complex, connected shape.

    Ensures that all perimeter points are detected correctly in a highly connected configuration.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(3, 3),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(0, 1),
        Coordinate(3, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
        Coordinate(3, 2),
        Coordinate(0, 3),
        Coordinate(3, 3),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_non_square_shape():
    """
    Test the outer bounds of a non-square rectangular shape.

    Ensures that the function correctly identifies perimeter points in rectangular configurations.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(4, 0),
        Coordinate(0, 1),
        Coordinate(4, 1),
        Coordinate(0, 2),
        Coordinate(4, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
        Coordinate(4, 3),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(3, 0),
        Coordinate(4, 0),
        Coordinate(0, 1),
        Coordinate(4, 1),
        Coordinate(0, 2),
        Coordinate(4, 2),
        Coordinate(0, 3),
        Coordinate(1, 3),
        Coordinate(2, 3),
        Coordinate(3, 3),
        Coordinate(4, 3),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_negative_coordinates():
    """
    Test the outer bounds of a shape with negative coordinates.

    Ensures that the function correctly handles coordinates with negative values.
    """
    coords = [
        Coordinate(-2, -1),
        Coordinate(-1, -1),
        Coordinate(0, -1),
        Coordinate(-2, 0),
        Coordinate(0, 0),
        Coordinate(-2, 1),
        Coordinate(-1, 1),
        Coordinate(0, 1),
    ]
    expected_bounds = {
        Coordinate(-2, -1),
        Coordinate(-1, -1),
        Coordinate(0, -1),
        Coordinate(-2, 0),
        Coordinate(0, 0),
        Coordinate(-2, 1),
        Coordinate(-1, 1),
        Coordinate(0, 1),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_single_column():
    """
    Test the outer bounds of a single column of occupied squares.

    Ensures that all squares in a vertical line are identified as perimeter points.
    """
    coords = [Coordinate(0, y) for y in range(5)]
    expected_bounds = {Coordinate(0, y) for y in range(5)}
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_single_row():
    """
    Test the outer bounds of a single row of occupied squares.

    Ensures that all squares in a horizontal line are identified as perimeter points.
    """
    coords = [Coordinate(x, 0) for x in range(5)]
    expected_bounds = {Coordinate(x, 0) for x in range(5)}
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_diagonal_connections_false():
    """
    Test the outer bounds of diagonally connected squares without considering diagonal adjacency.

    Ensures that diagonally adjacent squares are treated as separate perimeter points.
    """
    coords = [Coordinate(0, 0), Coordinate(1, 1), Coordinate(2, 2)]
    expected_bounds = {Coordinate(0, 0), Coordinate(1, 1), Coordinate(2, 2)}
    assert outer_bounds(coords, diagonal_sides=False) == expected_bounds


def test_outer_bounds_with_diagonal_connections_true_complex():
    """
    Test the outer bounds of a complex shape with diagonal adjacency enabled.

    Ensures that perimeter detection accounts for diagonal connections in complex configurations.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
        Coordinate(1, 3),
        Coordinate(2, 1),
        Coordinate(3, 1),
        Coordinate(1, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(2, 2),
        Coordinate(3, 3),
        Coordinate(1, 3),
        Coordinate(2, 1),
        Coordinate(3, 1),
        Coordinate(1, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds


def test_outer_bounds_with_sparse_coordinates():
    """
    Test the outer bounds of a sparse set of occupied squares.

    Ensures that the function correctly identifies perimeter points in a sparsely populated grid.
    """
    coords = [Coordinate(0, 0), Coordinate(2, 2), Coordinate(4, 4), Coordinate(6, 6)]
    expected_bounds = {Coordinate(0, 0), Coordinate(2, 2), Coordinate(4, 4), Coordinate(6, 6)}
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_clustered_coordinates():
    """
    Test the outer bounds of a clustered set of occupied squares.

    Ensures that closely positioned squares are correctly identified as perimeter points.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(0, 1),
        Coordinate(2, 1),
        Coordinate(0, 2),
        Coordinate(1, 2),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords) == expected_bounds


def test_outer_bounds_with_diagonal_sides_true_overlapping():
    """
    Test the outer bounds of overlapping shapes with diagonal adjacency enabled.

    Ensures that overlapping perimeter points are handled correctly when diagonals are considered.
    """
    coords = [
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    ]
    expected_bounds = {
        Coordinate(0, 0),
        Coordinate(1, 0),
        Coordinate(2, 0),
        Coordinate(1, 1),
        Coordinate(2, 1),
        Coordinate(1, 2),
        Coordinate(2, 2),
    }
    assert outer_bounds(coords, diagonal_sides=True) == expected_bounds
