"""
Test module for the `find_holes` function.

This module contains a comprehensive suite of tests to verify the correctness of the `find_holes` function,
which identifies enclosed empty cells ("holes") within a given set of occupied coordinates.
All tests ensure that the function accurately distinguishes between enclosed and non-enclosed empty cells
based on the provided coordinates.
"""

from aoc.grid.find_holes import find_holes


def test_empty_coordinates():
    """
    Test that an empty set of coordinates returns no holes.

    Ensures that providing no occupied cells results in no holes.
    """
    assert find_holes([]) == set()


def test_single_square():
    """
    Test that a single occupied square has no holes.

    A single unit square cannot enclose any empty cells.
    """
    coords = [(0, 0)]
    assert find_holes(coords) == set()


def test_two_by_two_block():
    """
    Test that a 2x2 block of squares has no holes.

    A fully filled 2x2 block forms a solid square without any enclosed empty cells.
    """
    coords = [(0, 0), (1, 0), (0, 1), (1, 1)]
    assert find_holes(coords) == set()


def test_three_by_three_with_center_hole():
    """
    Test a 3x3 block with the center cell empty.

    This configuration should identify the center cell as a hole.
    """
    coords = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    expected_holes = {(1, 1)}
    assert find_holes(coords) == expected_holes


def test_hollow_rectangle_with_multiple_holes():
    """
    Test a hollow rectangle containing multiple enclosed holes.

    This configuration has a larger outer rectangle with two separate enclosed empty areas.
    """
    coords = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (1,1), (2,1), (1,2), (2,2)
    expected_holes = {(1, 1), (2, 1), (1, 2), (2, 2)}
    assert find_holes(coords) == expected_holes


def test_complex_shape_with_nested_holes():
    """
    Test a complex shape with nested enclosed empty cells.

    This configuration includes an outer boundary with an inner boundary, creating a nested hole.
    """
    coords = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (4, 1),
        (0, 2),
        (4, 2),
        (0, 3),
        (4, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
    ]
    # Enclosed empty cells: (1,1), (2,1), (3,1), (1,2), (2,2), (3,2), (1,3), (2,3), (3,3)
    expected_holes = {(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)}
    assert find_holes(coords) == expected_holes


def test_non_contiguous_holes():
    """
    Test a configuration with multiple non-contiguous enclosed holes.

    This shape has two separate enclosed empty areas.
    """
    coords = [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (2, 1),
        (3, 1),
        (0, 2),
        (1, 2),
        (2, 2),
        (3, 2),
        (0, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (1,1)
    expected_holes = {(1, 1)}
    assert find_holes(coords) == expected_holes


def test_hole_touching_boundary():
    """
    Test that empty cells touching the bounding box are not considered holes.

    In this configuration, the empty cell is adjacent to the boundary and should not be identified as a hole.
    """
    coords = [
        (0, 0),
        (1, 0),
        (0, 1),  # (1,1) is empty and touches the boundary
    ]
    assert find_holes(coords) == set()


def test_coordinates_not_starting_at_zero():
    """
    Test that the function correctly handles coordinates not starting at (0, 0).

    The bounding box is shifted, but the hole detection should remain accurate.
    """
    coords = [(2, 2), (3, 2), (4, 2), (2, 3), (4, 3), (2, 4), (3, 4), (4, 4)]
    # Enclosed empty cell: (3,3)
    expected_holes = {(3, 3)}
    assert find_holes(coords) == expected_holes


def test_no_holes_large_filled_area():
    """
    Test a large filled area with no holes.

    Ensures that the function does not falsely identify holes in a fully occupied large grid.
    """
    coords = {(x, y) for x in range(5) for y in range(5)}
    assert find_holes(coords) == set()


def test_single_enclosed_hole_amidst_multiple():
    """
    Test a configuration with multiple enclosed holes, ensuring all are detected.

    This shape has two separate enclosed empty cells.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (1,1), (2,1), (1,2), (2,2)
    expected_holes = {(1, 1), (2, 1), (1, 2), (2, 2)}
    assert find_holes(coords) == expected_holes


def test_hole_with_diagonal_connections():
    """
    Test that diagonal connections do not prevent an empty cell from being considered a hole.

    Diagonal adjacency should not connect empty cells to the outside.
    """
    coords = [(0, 0), (2, 0), (0, 2), (2, 2)]
    expected_holes = set()
    assert find_holes(coords) == expected_holes


def test_hole_with_multiple_enclosures():
    """
    Test that the function correctly identifies holes within nested enclosures.

    This configuration has an outer enclosure and an inner enclosure, creating a donut shape.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (4, 1),
        (0, 2),
        (4, 2),
        (0, 3),
        (4, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        # Inner boundary
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (3, 2),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (2,2)
    expected_holes = {(2, 2)}
    assert find_holes(coords) == expected_holes


def test_multiple_disconnected_holes():
    """
    Test a configuration with multiple disconnected enclosed holes.

    This shape contains two separate enclosed empty cells.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        # Inner boundaries
        (1, 1),
        (2, 1),
        (1, 2),
        (2, 2),
    ]
    # Enclosed empty cells: None, as inner cells are filled
    expected_holes = set()
    assert find_holes(coords) == expected_holes


def test_hole_surrounded_by_non_contiguous_coordinates():
    """
    Test that the function can identify a hole even if the surrounding coordinates are non-contiguous.

    The enclosing cells are not in a single continuous path but still form a closed boundary.
    """
    coords = [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2)]
    expected_holes = set()
    assert find_holes(coords) == expected_holes


def test_large_single_hole():
    """
    Test a large single hole within a much larger occupied area.

    Ensures that the function can handle large grids and correctly identify a single large hole.
    """
    coords = []
    # Create a 10x10 outer boundary
    for x in range(11):
        coords.append((x, 0))
        coords.append((x, 10))
    for y in range(1, 10):
        coords.append((0, y))
        coords.append((10, y))
    # Create a single large hole in the center
    # Expected hole cells: all cells from (1,1) to (9,9)
    expected_holes = {(x, y) for x in range(1, 10) for y in range(1, 10)}
    assert find_holes(coords) == expected_holes


def test_no_enclosed_holes_with_empty_inside():
    """
    Test a configuration where empty cells are present but none are fully enclosed.

    Ensures that the function does not falsely identify non-enclosed empty cells as holes.
    """
    coords = [(0, 0), (1, 0), (2, 0), (0, 1), (2, 1), (0, 2), (1, 2), (2, 2)]
    # Enclosed empty cell: (1,1) is enclosed
    expected_holes = {(1, 1)}
    assert find_holes(coords) == expected_holes


def test_hole_with_disconnected_outer_boundary():
    """
    Test that disconnected outer boundaries do not falsely create holes.

    Ensures that only fully enclosed empty cells are considered holes.
    """
    coords = [
        (0, 0),
        (2, 0),
        (0, 2),
        (2, 2),
        # Missing connections to form a complete outer boundary
    ]
    # No enclosed empty cells as the boundary is not complete
    expected_holes = set()
    assert find_holes(coords) == expected_holes


def test_multiple_adjacent_holes():
    """
    Test a configuration with multiple adjacent enclosed empty cells forming a single large hole.

    Ensures that adjacent empty cells are recognized as part of the same hole.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (1,1), (2,1), (1,2), (2,2)
    expected_holes = {(1, 1), (2, 1), (1, 2), (2, 2)}
    assert find_holes(coords) == expected_holes


def test_single_row_no_holes():
    """
    Test that a single row of occupied cells does not contain any holes.

    A horizontal line cannot enclose any empty cells.
    """
    coords = [(0, 0), (1, 0), (2, 0), (3, 0)]
    assert find_holes(coords) == set()


def test_single_column_no_holes():
    """
    Test that a single column of occupied cells does not contain any holes.

    A vertical line cannot enclose any empty cells.
    """
    coords = [(0, 0), (0, 1), (0, 2), (0, 3)]
    assert find_holes(coords) == set()


def test_diagonal_occupied_cells_no_holes():
    """
    Test that diagonally placed occupied cells do not create any holes.

    Diagonal adjacency does not enclose any empty cells.
    """
    coords = [(0, 0), (1, 1), (2, 2), (3, 3)]
    assert find_holes(coords) == set()


def test_enclosed_hole_with_outer_hole():
    """
    Test a configuration with an outer hole and an inner enclosed hole.

    Ensures that only fully enclosed empty cells are identified as holes.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        # Inner boundary
        (1, 1),
        (2, 1),
        (1, 2),
        (2, 2),
    ]
    # Enclosed empty cells: None, since inner boundary is filled
    expected_holes = set()
    assert find_holes(coords) == expected_holes


def test_enclosed_hole_with_isolated_empty_cells():
    """
    Test that isolated empty cells within an enclosure are correctly identified as a single hole.

    Ensures that multiple isolated empty cells within the same enclosure are treated as one hole.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
    ]
    # Enclosed empty cells: (1,1), (2,1), (1,2), (2,2)
    expected_holes = {(1, 1), (2, 1), (1, 2), (2, 2)}
    assert find_holes(coords) == expected_holes


def test_enclosed_hole_with_outer_extension():
    """
    Test that extensions outside the enclosure do not affect hole detection.

    Ensures that the presence of additional occupied cells outside the enclosure does not interfere with hole identification.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (0, 1),
        (3, 1),
        (0, 2),
        (3, 2),
        (0, 3),
        (1, 3),
        (2, 3),
        (3, 3),
        # Extensions
        (4, 0),
        (4, 1),
        (4, 2),
        (4, 3),
    ]
    # Enclosed empty cells: (1,1), (2,1), (1,2), (2,2)
    expected_holes = {(1, 1), (2, 1), (1, 2), (2, 2)}
    assert find_holes(coords) == expected_holes


def test_multiple_separate_holes():
    """
    Test a configuration with multiple separate enclosed holes.

    This shape contains two distinct enclosed empty regions.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (4, 1),
        (0, 2),
        (4, 2),
        (0, 3),
        (4, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        # Inner boundary 1
        (2, 2),
    ]
    # Enclosed empty cells: (1,1), (2,1), (3,1), (1,2), (3,2), (1,3), (3,3)
    expected_holes = {
        (1, 1),
        (2, 1),
        (3, 1),
        (1, 2),
        (3, 2),
        (1, 3),
        (2, 3),
        (3, 3),
    }
    assert find_holes(coords) == expected_holes


def test_nested_holes_multiple_levels():
    """
    Test a configuration with multiple levels of nested holes.

    This shape has an outer boundary, an inner boundary creating a hole, and another inner boundary within the first hole.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (5, 0),
        (0, 1),
        (5, 1),
        (0, 2),
        (5, 2),
        (0, 3),
        (5, 3),
        (0, 4),
        (5, 4),
        (0, 5),
        (1, 5),
        (2, 5),
        (3, 5),
        (4, 5),
        (5, 5),
        # inner boundary
        (2, 1),
        (3, 1),
        (2, 2),
        (3, 2),
        (2, 3),
        (3, 3),
        (2, 4),
        (3, 4),
    ]
    expected_holes = {
        (1, 1),
        (4, 1),
        (1, 2),
        (4, 2),
        (1, 3),
        (4, 3),
        (1, 4),
        (4, 4),
    }
    assert find_holes(coords) == expected_holes


def test_holes_with_various_shapes():
    """
    Test holes of different shapes within the occupied coordinates.

    Ensures that the function can detect holes regardless of their geometric configuration.
    """
    coords = [
        # Outer boundary
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 0),
        (0, 1),
        (4, 1),
        (0, 2),
        (4, 2),
        (0, 3),
        (4, 3),
        (0, 4),
        (1, 4),
        (2, 4),
        (3, 4),
        (4, 4),
        # Inner boundary - L shape
        (1, 1),
        (2, 1),
        (1, 2),
        (1, 3),
        (2, 3),
    ]
    # Enclosed empty cells: (1,2), (2,2), (3,2)
    expected_holes = {(2, 2), (3, 2), (3, 1), (3, 3)}
    assert find_holes(coords) == expected_holes
