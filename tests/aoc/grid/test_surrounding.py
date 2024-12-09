"""Tests for the surrounding module."""

from aoc.grid import surrounding


def test_single_coordinate_cross_only():
    """Test a single coordinate with only cross sides."""
    result = surrounding((1, 1))
    expected = {(0, 1), (2, 1), (1, 0), (1, 2)}
    assert result == expected


def test_single_coordinate_diagonal_only():
    """Test a single coordinate with only diagonal sides."""
    result = surrounding((1, 1), diagonal_sides=True, cross_sides=False)
    expected = {(0, 0), (2, 0), (0, 2), (2, 2)}
    assert result == expected


def test_single_coordinate_both_sides():
    """Test a single coordinate with both cross and diagonal sides."""
    result = surrounding((1, 1), diagonal_sides=True)
    expected = {(0, 1), (2, 1), (1, 0), (1, 2), (0, 0), (2, 0), (0, 2), (2, 2)}
    assert result == expected


def test_multiple_coordinates_cross_only():
    """Test multiple coordinates with only cross sides."""
    coordinates = [(1, 1), (2, 2)]
    result = surrounding(coordinates)
    expected = {(0, 1), (2, 1), (1, 0), (1, 2), (1, 2), (3, 2), (2, 1), (2, 3)}
    assert result == expected


def test_multiple_coordinates_diagonal_only():
    """Test multiple coordinates with only diagonal sides."""
    coordinates = [(1, 1), (2, 2)]
    result = surrounding(coordinates, cross_sides=False, diagonal_sides=True)
    assert result == {(0, 0), (2, 0), (0, 2), (2, 2), (1, 1), (3, 1), (1, 3), (3, 3)}


def test_multiple_coordinates_both_sides():
    """Test multiple coordinates with both cross and diagonal sides."""
    coordinates = [(1, 1), (2, 2)]
    result = surrounding(coordinates, diagonal_sides=True)

    expected = {
        (0, 1),
        (2, 1),
        (1, 0),
        (1, 2),
        (1, 1),
        (0, 0),
        (2, 0),
        (0, 2),
        (2, 2),
        (3, 2),
        (2, 3),
        (3, 1),
        (1, 3),
        (3, 3),
    }
    assert result == expected


def test_boundaries_min_edge():
    """Test coordinates on the minimum boundary."""
    result = surrounding((0, 0))
    expected = {(1, 0), (0, 1), (-1, 0), (0, -1)}
    assert result == expected


def test_boundaries_max_edge():
    """Test coordinates on the maximum boundary."""
    bounds = (0, 0, 5, 5)
    result = surrounding((5, 5), bounds=bounds)
    expected = {(4, 5), (5, 4)}
    assert result == expected


def test_boundaries_corner():
    """Test coordinates on a corner with diagonals."""
    bounds = (0, 0, 5, 5)
    result = surrounding((0, 0), diagonal_sides=True, bounds=bounds)
    expected = {(1, 0), (0, 1), (1, 1)}
    assert result == expected


def test_multiple_coordinates_with_overlapping_surroundings():
    """Test multiple coordinates where surrounding areas overlap."""
    coordinates = [(1, 1), (1, 2)]
    result = surrounding(coordinates)
    expected = {
        (0, 1),
        (2, 1),
        (1, 0),
        (1, 2),
        (0, 2),
        (2, 2),
        (1, 3),
        (1, 1),
    }
    assert result == expected


def test_custom_bounds():
    """Test with custom bounds that restrict some surrounding coordinates."""
    coordinates = [(1, 1)]
    bounds = (0, 0, 1, 1)
    result = surrounding(coordinates, bounds=bounds)
    expected = {(0, 1), (1, 0)}
    assert result == expected


def test_empty_coordinates():
    """Test that an empty list of coordinates returns an empty set."""
    result = surrounding([])
    expected = set()
    assert result == expected


def test_large_bounds():
    """Test with very large bounds to ensure no unexpected restrictions."""
    coordinates = [(1000, 1000)]
    result = surrounding(coordinates, bounds=(0, 0, 2000, 2000))
    expected = {(999, 1000), (1001, 1000), (1000, 999), (1000, 1001)}
    assert result == expected


def test_negative_coordinates():
    """Test coordinates with negative values within bounds."""
    coordinates = [(-1, -1)]
    bounds = (-5, -5, 0, 0)
    result = surrounding(coordinates, bounds=bounds, diagonal_sides=True)
    expected = {(-2, -1), (0, -1), (-1, -2), (-1, 0), (-2, -2), (0, -2), (-2, 0), (0, 0)}
    assert result == expected


def test_multiple_coordinates_outside_bounds():
    """Test multiple coordinates with some outside the bounds."""
    coordinates = [(1, 1), (10, 10)]
    bounds = (0, 0, 5, 5)
    result = surrounding(coordinates, bounds=bounds)
    expected = {(0, 1), (2, 1), (1, 0), (1, 2), (9, 10), (11, 10), (10, 9), (10, 11)}
    # However, (9,10), (11,10), (10,9), (10,11) are outside bounds (0,0,5,5), so only from (1,1):
    expected = {(0, 1), (2, 1), (1, 0), (1, 2)}
    assert result == expected
