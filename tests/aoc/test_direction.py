"""Tests for Direction class."""
import pytest

from aoc import Direction


def test_turn_left():
    """Test that the turn_left method returns the correct direction."""
    assert Direction.NORTH.turn_left() == Direction.WEST
    assert Direction.EAST.turn_left() == Direction.NORTH
    assert Direction.UP.turn_left() == Direction.WEST


def test_turn_right():
    """Test that the turn_right method returns the correct direction."""
    assert Direction.NORTH.turn_right() == Direction.EAST
    assert Direction.WEST.turn_right() == Direction.NORTH


@pytest.mark.parametrize("direction,start_x,start_y,expected_x,expected_y", [
    (Direction.NORTH, 2, 2, 2, 1),
    (Direction.SOUTH, 2, 2, 2, 3),
    (Direction.WEST,  2, 2, 1, 2),
    (Direction.EAST,  2, 2, 3, 2),
])
def test_move(direction, start_x, start_y, expected_x, expected_y):
    """Test that the move method returns the correct coordinates for all directions."""
    assert direction.move(start_x, start_y) == (expected_x, expected_y)


@pytest.mark.parametrize("direction,start_x,start_y,width,height,expected", [
    (Direction.NORTH, 1, 1, 3, 3, False),
    (Direction.NORTH, 0, 0, 1, 1, True),
    (Direction.SOUTH, 1, 1, 3, 3, False),
    (Direction.SOUTH, 2, 2, 3, 3, True),   # Moving south out of bottom boundary
    (Direction.WEST,  1, 1, 3, 3, False),
    (Direction.WEST,  0, 1, 3, 1, True),    # Moving west out of left boundary
    (Direction.EAST,  1, 1, 3, 3, False),
    (Direction.EAST,  2, 2, 1, 3, True),    # Moving east out of right boundary
])
def test_next_move_out_of_bounds(direction, start_x, start_y, width, height, expected):
    """Test that the next_move_out_of_bounds method correctly identifies out-of-bound moves for all directions."""
    assert direction.next_move_out_of_bounds(start_x, start_y, width, height) == expected
