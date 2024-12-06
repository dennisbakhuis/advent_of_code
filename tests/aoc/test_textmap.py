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
    return [
        "ABC",
        "DEF",
        "GHI"
    ]

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

def test_get(tm):
    """
    Test the get method.

    Ensures correct characters are retrieved at given coordinates.
    """
    assert tm.get(0, 0) == "A"
    assert tm.get(2, 2) == "I"

def test_set(tm):
    """
    Test the set method.

    Modifies a character and verifies it's updated correctly.
    """
    tm.set(1, 1, "X")
    assert tm.get(1, 1) == "X"

def test_find(tm):
    """
    Test the find method.

    Ensures the first occurrence of a character is located correctly.
    """
    assert tm.find("A") == (0, 0)
    assert tm.find("I") == (2, 2)

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

def test_as_lines(tm):
    """
    Test the as_lines method.

    Ensures the internal string is correctly split back into lines.
    """
    lines = tm.as_lines()
    assert len(lines) == tm._n_rows
    assert lines[0] == "ABC"

def test_show(tm):
    """
    Test the show method.

    Ensures the printed output matches the map.
    """
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        tm.show()
        output = mock_stdout.getvalue().strip()
    assert output == "ABC\nDEF\nGHI"
