"""Tests for Direction class."""

import pytest

from aoc.grid import Direction


def test_turn_left():
    """Test that the turn_left method returns the correct direction."""
    assert Direction.NORTH.turn_left() == Direction.WEST
    assert Direction.EAST.turn_left() == Direction.NORTH
    assert Direction.UP.turn_left() == Direction.WEST


def test_turn_right():
    """Test that the turn_right method returns the correct direction."""
    assert Direction.NORTH.turn_right() == Direction.EAST
    assert Direction.WEST.turn_right() == Direction.NORTH
    assert Direction.DOWN.turn_right() == Direction.WEST


@pytest.mark.parametrize(
    "direction,start_x,start_y,expected_x,expected_y",
    [
        (Direction.NORTH, 2, 2, 2, 1),
        (Direction.SOUTH, 2, 2, 2, 3),
        (Direction.WEST, 2, 2, 1, 2),
        (Direction.EAST, 2, 2, 3, 2),
    ],
)
def test_move(direction, start_x, start_y, expected_x, expected_y):
    """Test that the move method returns the correct coordinates for all directions."""
    assert direction.move(start_x, start_y) == (expected_x, expected_y)


@pytest.mark.parametrize(
    "direction,start_x,start_y,expected_x,expected_y",
    [
        (Direction.NORTH, 2, 2, 2, 3),
        (Direction.SOUTH, 2, 2, 2, 1),
        (Direction.WEST, 2, 2, 3, 2),
        (Direction.EAST, 2, 2, 1, 2),
    ],
)
def test_before(direction, start_x, start_y, expected_x, expected_y):
    """
    Test the before method for all directions.

    Test that the before method returns the correct coordinates
    that would have led to the current position.
    """
    assert direction.before(start_x, start_y) == (expected_x, expected_y)


@pytest.mark.parametrize(
    "direction,start_x,start_y,width,height,expected",
    [
        (Direction.NORTH, 1, 1, 3, 3, False),
        (Direction.NORTH, 0, 0, 1, 1, True),
        (Direction.SOUTH, 1, 1, 3, 3, False),
        (Direction.SOUTH, 2, 2, 3, 3, True),  # Moving south out of bottom boundary
        (Direction.WEST, 1, 1, 3, 3, False),
        (Direction.WEST, 0, 1, 3, 1, True),  # Moving west out of left boundary
        (Direction.EAST, 1, 1, 3, 3, False),
        (Direction.EAST, 2, 2, 1, 3, True),  # Moving east out of right boundary
    ],
)
def test_next_move_out_of_bounds(direction, start_x, start_y, width, height, expected):
    """Test that the next_move_out_of_bounds method correctly identifies out-of-bound moves for all directions."""
    assert direction.next_move_out_of_bounds(start_x, start_y, width, height) == expected


def test_synonyms():
    """Test that compass synonyms reference the same directions as UP, DOWN, LEFT, RIGHT."""
    assert Direction.NORTH is Direction.UP
    assert Direction.SOUTH is Direction.DOWN
    assert Direction.WEST is Direction.LEFT
    assert Direction.EAST is Direction.RIGHT


def test_synonyms_behave_same():
    """Test that synonyms behave the same as their main directions for move and before."""
    # Check move
    assert Direction.NORTH.move(2, 2) == Direction.UP.move(2, 2)
    assert Direction.SOUTH.move(2, 2) == Direction.DOWN.move(2, 2)
    assert Direction.WEST.move(2, 2) == Direction.LEFT.move(2, 2)
    assert Direction.EAST.move(2, 2) == Direction.RIGHT.move(2, 2)

    # Check before
    assert Direction.NORTH.before(2, 2) == Direction.UP.before(2, 2)
    assert Direction.SOUTH.before(2, 2) == Direction.DOWN.before(2, 2)
    assert Direction.WEST.before(2, 2) == Direction.LEFT.before(2, 2)
    assert Direction.EAST.before(2, 2) == Direction.RIGHT.before(2, 2)


def test_turn_left_synonyms():
    """Test that synonyms turn left correctly, matching their main directions."""
    assert Direction.NORTH.turn_left() == Direction.UP.turn_left()
    assert Direction.SOUTH.turn_left() == Direction.DOWN.turn_left()
    assert Direction.WEST.turn_left() == Direction.LEFT.turn_left()
    assert Direction.EAST.turn_left() == Direction.RIGHT.turn_left()


def test_turn_right_synonyms():
    """Test that synonyms turn right correctly, matching their main directions."""
    assert Direction.NORTH.turn_right() == Direction.UP.turn_right()
    assert Direction.SOUTH.turn_right() == Direction.DOWN.turn_right()
    assert Direction.WEST.turn_right() == Direction.LEFT.turn_right()
    assert Direction.EAST.turn_right() == Direction.RIGHT.turn_right()
