"""Tests for the TextMap class."""

import pytest
from io import StringIO
from unittest.mock import patch
from aoc import TextMap


@pytest.fixture
def sample_map():
    """
    Create a sample map.

    Returns
    -------
    list of str
        A sample 3x3 ASCII map for testing.
    """
    return ["ABC", "DEF", "GHI"]


@pytest.fixture
def tm(sample_map):
    """
    Create a TextMap instance.

    Returns
    -------
    TextMap
        A TextMap instance initialized with sample_map.
    """
    return TextMap(sample_map)


def test_init(tm, sample_map):
    """
    Test TextMap initialization.

    Checks if rows, columns, and internal string match expectations.
    """
    assert tm._n_rows == len(sample_map)
    assert tm._n_columns == len(sample_map[0])
    assert "".join(sample_map) == tm._map_string


def test_init_empty():
    """
    Test initialization with an empty map.

    Ensures rows, columns, and internal string are zero or empty.
    """
    empty_tm = TextMap([])
    assert empty_tm.height == 0
    assert empty_tm.width == 0
    assert empty_tm.as_string() == ""


def test_width_height(tm):
    """
    Test width and height properties.

    Ensures width and height match the given map dimensions.
    """
    assert tm.width == 3
    assert tm.height == 3


def test_get(tm):
    """
    Test the get method.

    Ensures correct characters are retrieved at given coordinates.
    """
    assert tm.get(0, 0) == "A"
    assert tm.get(2, 2) == "I"


def test_get_out_of_bounds(tm):
    """
    Test get method with out-of-bounds coordinates.

    Expecting an IndexError since the map doesn't handle bounds internally.
    """
    with pytest.raises(ValueError):
        tm.get(-1, 0)
    with pytest.raises(ValueError):
        tm.get(3, 0)
    with pytest.raises(ValueError):
        tm.get(0, 3)

    assert tm.get(-1, -1, "%") == "%"
    assert tm.get(0, 0, "%") == "A"


def test_get_many(tm):
    """
    Test the get_many method.

    Ensures multiple characters are retrieved correctly.
    """
    coords = [(0, 0), (1, 1), (2, 2)]
    assert tm.get_many(coords) == ("A", "E", "I")


def test_get_many_empty(tm):
    """
    Test get_many with empty coordinates list.

    Should return an empty tuple.
    """
    assert tm.get_many([]) == ()


def test_get_many_out_of_bounds(tm):
    """
    Test get_many with some coordinates out of bounds.

    Expecting an IndexError for invalid coordinates.
    """
    coords = [(0, 0), (10, 10)]
    with pytest.raises(IndexError):
        tm.get_many(coords)


def test_set(tm):
    """
    Test the set method.

    Modifies a character and verifies it's updated correctly.
    """
    tm.set(1, 1, "X")
    assert tm.get(1, 1) == "X"
    # Ensure other characters remain unchanged
    assert tm.get(0, 0) == "A"
    assert tm.get(2, 2) == "I"


def test_set_out_of_bounds(tm):
    """
    Test set method with out-of-bounds coordinates.

    Should not raise errors, but also should not modify the map.
    """
    original = tm.as_string()
    tm.set(-1, 0, "Z")
    tm.set(3, 3, "Z")
    assert tm.as_string() == original


def test_find(tm):
    """
    Test the find method.

    Ensures the first occurrence of a character is located correctly.
    """
    assert tm.find("A") == (0, 0)
    assert tm.find("I") == (2, 2)


def test_find_not_found(tm):
    """
    Test find method when character is not found.

    Expecting a ValueError.
    """
    with pytest.raises(ValueError):
        tm.find("Z")


def test_find_all(tm):
    """
    Test the find_all method.

    Ensures all occurrences of a character are returned.
    """
    tm.set(2, 0, "A")
    positions = tm.find_all("A")
    assert (0, 0) in positions
    assert (2, 0) in positions
    assert len(positions) == 2


def test_find_all_not_found(tm):
    """
    Test find_all method when character is not present.

    Should return an empty list.
    """
    assert tm.find_all("Z") == []


def test_as_lines(tm):
    """
    Test the as_lines method.

    Ensures the internal string is correctly split back into lines.
    """
    lines = tm.as_lines()
    assert len(lines) == tm._n_rows
    assert lines[0] == "ABC"
    assert lines[1] == "DEF"
    assert lines[2] == "GHI"


def test_as_lines_empty():
    """
    Test as_lines on an empty TextMap.

    Should return an empty list.
    """
    empty_tm = TextMap([])
    assert empty_tm.as_lines() == []


def test_show(tm):
    """
    Test the show method.

    Ensures the printed output matches the map.
    """
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        tm.show()
        output = mock_stdout.getvalue().strip()
    assert output == "ABC\nDEF\nGHI"


def test_copy(tm):
    """
    Test the copy method.

    Ensure the returned TextMap is a deep copy.
    """
    tm_copy = tm.copy()
    assert tm_copy is not tm
    assert tm_copy.as_string() == tm.as_string()
    tm_copy.set(0, 0, "Z")
    # Original should remain unchanged
    assert tm.get(0, 0) == "A"
    assert tm_copy.get(0, 0) == "Z"


def test_pad_all_sides(tm):
    """
    Test pad with an integer for all sides.

    Ensures map is padded evenly.
    """
    padded = tm.pad(1, fill="-")
    lines = padded.as_lines()
    # Original is 3x3, padding 1 all around -> 5x5
    assert padded.width == 5
    assert padded.height == 5
    assert lines[0] == "-----"
    assert lines[2] == "-DEF-"
    assert lines[4] == "-----"


def test_pad_custom_sides(tm):
    """
    Test pad with a list of four integers [top, bottom, left, right].

    Ensures correct padding on each side.
    """
    padded = tm.pad([1, 2, 3, 4], fill=".")
    lines = padded.as_lines()
    # Original is 3x3
    # Top=1, Bottom=2, Left=3, Right=4
    # New width = 3+3+4 = 10
    # New height = 3+1+2 = 6
    assert padded.width == 10
    assert padded.height == 6
    assert lines[0] == "." * 10
    # Middle lines: 3 chars map + 3 left pads + 4 right pads
    # Should look like: '...' + 'ABC' + '....' = '...ABC....'
    assert lines[1] == "...ABC...."
    assert lines[-1] == "." * 10


def test_pad_invalid_input(tm):
    """
    Test pad with invalid padding input.

    Should raise ValueError.
    """
    with pytest.raises(ValueError):
        tm.pad([1, 2, 3])  # not four elements


def test_pad_zero_padding(tm):
    """
    Test pad with zero padding.

    Ensures no change to the map.
    """
    padded = tm.pad(0)
    assert padded.as_lines() == tm.as_lines()


def test_as_string(tm):
    """
    Test as_string method.

    Ensures the returned string matches the internal representation.
    """
    expected = "ABCDEFGHI"
    assert tm.as_string() == expected


def test_within_bounds(tm):
    """
    Test within_bounds method.

    Ensures correct boolean return for various coordinates.
    """
    assert tm.within_bounds(0, 0) is True
    assert tm.within_bounds(2, 2) is True
    assert tm.within_bounds(-1, 0) is False
    assert tm.within_bounds(3, 0) is False
    assert tm.within_bounds(0, 3) is False


def test_within_bounds_empty():
    """
    Test within_bounds on an empty map.

    Should always return False.
    """
    empty_tm = TextMap([])
    assert empty_tm.within_bounds(0, 0) is False
