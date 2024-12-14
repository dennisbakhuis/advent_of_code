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


@pytest.fixture
def large_map():
    """
    Create a large 100x100 TextMap filled with '.' characters.

    Returns
    -------
    TextMap
        A large TextMap instance for testing.
    """
    width, height = 100, 100
    lines = ["." * width for _ in range(height)]
    return TextMap(lines)


@pytest.fixture
def uneven_map_string():
    """
    Create a string representing an ASCII map with uneven line lengths.

    Returns
    -------
    str
        An ASCII map string with lines of varying lengths.
    """
    return "ABCDE\nFGH\nIJKL"


@pytest.fixture
def single_line_map_string():
    """
    Create a string representing an ASCII map with a single line.

    Returns
    -------
    str
        An ASCII map string with a single line.
    """
    return "ONLYONELINE"


@pytest.fixture
def empty_map_string():
    """
    Create an empty string for testing from_string with no content.

    Returns
    -------
    str
        An empty string.
    """
    return ""


@pytest.fixture
def map_string_with_unicode():
    """
    Create a string representing an ASCII map with Unicode characters.

    Returns
    -------
    str
        An ASCII map string containing Unicode characters.
    """
    return "A😊C\nD😊F\nG😊I"


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

    assert tm.get((0, 0)) == "A"
    assert tm.get((2, 2)) == "I"


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
    with pytest.raises(ValueError):
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
    assert tm.within_bounds((0, 0)) is True
    assert tm.within_bounds((2, 2)) is True
    assert tm.within_bounds((-1, 0)) is False
    assert tm.within_bounds((3, 0)) is False
    assert tm.within_bounds((0, 3)) is False


def test_within_bounds_empty():
    """
    Test within_bounds on an empty map.

    Should always return False.
    """
    empty_tm = TextMap([])
    assert empty_tm.within_bounds((0, 0)) is False


def test_find_horizontal_numbers_empty_map():
    """
    Test find_horizontal_numbers on an empty TextMap.

    Should return an empty list.
    """
    empty_tm = TextMap([])
    assert empty_tm.find_horizontal_numbers() == []


def test_find_horizontal_numbers_single_line_no_numbers():
    """
    Test find_horizontal_numbers on a single line with no numbers.

    Should return an empty list.
    """
    tm = TextMap(["ABCDE"])
    assert tm.find_horizontal_numbers() == []


def test_find_horizontal_numbers_single_line_with_numbers():
    """
    Test find_horizontal_numbers on a single line containing multiple numbers.

    Should return a list of tuples with each number and its starting and ending positions.
    """
    tm = TextMap(["A12BC34D"])
    expected = [
        (12, (1, 0), (2, 0)),  # "12" starts at index 1 and ends at index 2 in row 0
        (34, (5, 0), (6, 0)),  # "34" starts at index 5 and ends at index 6 in row 0
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_multiple_lines_with_numbers():
    """
    Test find_horizontal_numbers on multiple lines containing various numbers.

    Should return a list of tuples for all numbers across different rows.
    """
    tm = TextMap(["A12BC34D", "12345", "NoNumbersHere", "67890", "End99"])
    expected = [
        (12, (1, 0), (2, 0)),
        (34, (5, 0), (6, 0)),
        (12345, (0, 1), (4, 1)),
        (67890, (0, 3), (4, 3)),
        (99, (3, 4), (4, 4)),
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_numbers_at_boundaries():
    """
    Test find_horizontal_numbers with numbers located at the start or end of lines.

    Should correctly identify numbers at the boundaries.
    """
    tm = TextMap(["123ABC", "DEF456", "789GHI"])
    expected = [
        (123, (0, 0), (2, 0)),  # "123" starts at index 0 and ends at index 2 in row 0
        (456, (3, 1), (5, 1)),  # "456" starts at index 3 and ends at index 5 in row 1
        (789, (0, 2), (2, 2)),  # "789" starts at index 0 and ends at index 2 in row 2
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_overlapping_numbers():
    """
    Test find_horizontal_numbers with overlapping numbers.

    Ensures that the regex correctly captures the entire number without overlaps.
    """
    tm = TextMap(["A1234B"])
    expected = [
        (1234, (1, 0), (4, 0))  # "1234" starts at index 1 and ends at index 4 in row 0
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_numbers_with_leading_zeros():
    """
    Test find_horizontal_numbers with numbers that have leading zeros.

    Should correctly parse numbers by ignoring leading zeros.
    """
    tm = TextMap(["A0012B", "003C"])
    expected = [
        (12, (1, 0), (4, 0)),  # "0012" starts at index 1 and ends at index 4 in row 0
        (3, (0, 1), (2, 1)),  # "003" starts at index 0 and ends at index 2 in row 1
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_single_digit_numbers():
    """
    Test find_horizontal_numbers with single-digit numbers.

    Should correctly identify and return single-digit numbers.
    """
    tm = TextMap(["A1B2C3"])
    expected = [
        (1, (1, 0), (1, 0)),  # "1" at index 1 in row 0
        (2, (3, 0), (3, 0)),  # "2" at index 3 in row 0
        (3, (5, 0), (5, 0)),  # "3" at index 5 in row 0
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_full_number_line():
    """
    Test find_horizontal_numbers on a line that is entirely numeric.

    Should return the full number with starting and ending positions at the ends of the line.
    """
    tm = TextMap(["1234567890"])
    expected = [
        (1234567890, (0, 0), (9, 0))  # "1234567890" starts at index 0 and ends at index 9 in row 0
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_mixed_content():
    """
    Test find_horizontal_numbers with a mix of content and numbers scattered across lines.

    Should correctly identify all numbers regardless of their position in the lines.
    """
    tm = TextMap(["Start99End", "Middle123Middle", "NoNumbersHere", "456Start", "End789"])
    expected = [
        (99, (5, 0), (6, 0)),  # "99" starts at index 5 and ends at index 6 in row 0
        (123, (6, 1), (8, 1)),  # "123" starts at index 6 and ends at index 8 in row 1
        (456, (0, 3), (2, 3)),  # "456" starts at index 0 and ends at index 2 in row 3
        (789, (3, 4), (5, 4)),  # "789" starts at index 3 and ends at index 5 in row 4
    ]
    assert tm.find_horizontal_numbers() == expected


def test_find_horizontal_numbers_no_numbers():
    """
    Test find_horizontal_numbers on a map with no numbers.

    Should return an empty list.
    """
    tm = TextMap(["ABC", "DEF", "GHI"])
    assert tm.find_horizontal_numbers() == []


def test_find_horizontal_numbers_multiple_numbers_per_line():
    """
    Test find_horizontal_numbers with multiple numbers in the same line.

    Should return all numbers with their respective starting and ending positions.
    """
    tm = TextMap(["12AB34CD56"])
    expected = [
        (12, (0, 0), (1, 0)),  # "12" starts at index 0 and ends at index 1 in row 0
        (34, (4, 0), (5, 0)),  # "34" starts at index 4 and ends at index 5 in row 0
        (56, (8, 0), (9, 0)),  # "56" starts at index 8 and ends at index 9 in row 0
    ]
    assert tm.find_horizontal_numbers() == expected


def test_set_many_normal(tm):
    """Test setting multiple in-bounds coordinates."""
    coordinates = [(0, 0), (1, 1), (2, 2)]
    tm.set_many(coordinates, "Z")
    expected_lines = ["ZBC", "DZF", "GHZ"]
    assert tm.as_lines() == expected_lines


def test_set_many_with_out_of_bounds(tm):
    """Test setting coordinates where some are out of bounds."""
    coordinates = [(-1, 0), (0, -1), (1, 1), (3, 3)]
    tm.set_many(coordinates, "X")
    expected_lines = ["ABC", "DXF", "GHI"]
    assert tm.as_lines() == expected_lines  # Only (1,1) is in bounds


def test_set_many_empty_coordinates(tm):
    """Test setting with an empty coordinates iterable."""
    coordinates = []
    tm.set_many(coordinates, "X")
    # Map should remain unchanged
    expected_lines = ["ABC", "DEF", "GHI"]
    assert tm.as_lines() == expected_lines


def test_set_many_overlapping_coordinates(tm):
    """Test setting the same coordinate multiple times."""
    coordinates = [(1, 1), (1, 1), (1, 1)]
    tm.set_many(coordinates, "Z")
    expected_lines = ["ABC", "DZF", "GHI"]
    assert tm.as_lines() == expected_lines  # Last 'Z' applied


def test_set_many_different_iterables(tm, sample_map):
    """Test set_many with different types of iterables."""
    # Using a list
    list_coords = [(0, 0), (2, 2)]
    tm.set_many(list_coords, "L")
    expected_lines = [
        "LBC",
        "DEF",
        "GHIL",  # Note: Original map is 3x3, (2,2) is 'I' -> 'L'
    ]
    # Adjusted expected_lines for 3x3 map
    expected_lines = ["LBC", "DEF", "GHL"]
    assert tm.as_lines() == expected_lines

    # Reset map
    tm_copy = TextMap(sample_map)

    # Using a set
    set_coords = {(0, 0), (2, 2)}
    tm_copy.set_many(set_coords, "S")
    expected_lines_set = ["SBC", "DEF", "GHS"]
    assert tm_copy.as_lines() == expected_lines_set

    # Using a generator
    generator_coords = ((x, y) for x, y in [(0, 0), (2, 2)])
    tm_copy_reset = TextMap(sample_map)
    tm_copy_reset.set_many(generator_coords, "G")
    expected_lines_gen = ["GBC", "DEF", "GHG"]
    assert tm_copy_reset.as_lines() == expected_lines_gen


def test_set_many_different_values(tm):
    """Test setting multiple coordinates with different values by calling set_many multiple times."""
    # First set many to "X"
    coordinates = [(0, 0), (1, 1), (2, 2)]
    tm.set_many(coordinates, "X")

    # Then set many to "Y" on some overlapping and some new coordinates
    new_coordinates = [(1, 1), (2, 0)]
    tm.set_many(new_coordinates, "Y")
    expected_lines = ["XBY", "DYF", "GHX"]
    assert tm.as_lines() == expected_lines


def test_set_many_large_number_of_coordinates(large_map):
    """Test set_many with a large number of coordinates."""
    # Set every 10th character in each row to 'X'
    coordinates = [(x, y) for y in range(large_map.height) for x in range(0, large_map.width, 10)]
    large_map.set_many(coordinates, "X")

    for y in range(large_map.height):
        line = large_map.as_lines()[y]
        for x in range(large_map.width):
            if x % 10 == 0:
                assert line[x] == "X"
            else:
                assert line[x] == "."


def test_set_many_no_side_effects(tm):
    """Ensure that only specified coordinates are modified."""
    coordinates = [(0, 0), (2, 2)]
    tm.set_many(coordinates, "Z")
    expected_lines = ["ZBC", "DEF", "GHZ"]
    assert tm.as_lines() == expected_lines


def test_set_many_unicode_characters(tm):
    """Test setting with Unicode characters."""
    coordinates = [(0, 0), (1, 1)]
    tm.set_many(coordinates, "😊")
    expected_lines = ["😊BC", "D😊F", "GHI"]
    assert tm.as_lines() == expected_lines


def test_set_many_partial_overlap(tm):
    """Test set_many with some overlapping and some non-overlapping coordinates."""
    coordinates = [(0, 0), (1, 1), (1, 1), (2, 2)]
    tm.set_many(coordinates, "P")
    expected_lines = [
        "PBC",
        "DPF",
        "GHPP",  # Note: Original map is 3x3, (2,2) is 'I' -> 'P'
    ]
    # Adjusted expected_lines for 3x3 map
    expected_lines = ["PBC", "DPF", "GHP"]
    assert tm.as_lines() == expected_lines


def test_from_string_normal():
    """Test creating TextMap from a multi-line string with equal-length lines."""
    map_str = "ABC\nDEF\nGHI"
    tm = TextMap.from_string(map_str)
    expected_lines = ["ABC", "DEF", "GHI"]
    assert tm.as_lines() == expected_lines
    assert tm.width == 3
    assert tm.height == 3


def test_from_string_with_padding(uneven_map_string):
    """Test creating TextMap from a multi-line string with uneven line lengths (padding)."""
    tm = TextMap.from_string(uneven_map_string)
    expected_lines = ["ABCDE", "FGH  ", "IJKL "]
    assert tm.as_lines() == expected_lines
    assert tm.width == 5  # Maximum line length is 5
    assert tm.height == 3


def test_from_string_empty(empty_map_string):
    """Test creating TextMap from an empty string."""
    tm = TextMap.from_string(empty_map_string)
    expected_lines = []
    assert tm.as_lines() == expected_lines
    assert tm.width == 0
    assert tm.height == 0


def test_from_string_single_line(single_line_map_string):
    """Test creating TextMap from a single-line string."""
    tm = TextMap.from_string(single_line_map_string)
    expected_lines = ["ONLYONELINE"]
    assert tm.as_lines() == expected_lines
    assert tm.width == len("ONLYONELINE")
    assert tm.height == 1


def test_from_string_with_unicode(map_string_with_unicode):
    """Test creating TextMap from a string containing Unicode characters."""
    tm = TextMap.from_string(map_string_with_unicode)
    expected_lines = ["A😊C", "D😊F", "G😊I"]
    assert tm.as_lines() == expected_lines
    assert tm.width == 3
    assert tm.height == 3


def test_empty_normal():
    """Test creating an empty TextMap with specified width and height."""
    width, height = 4, 3
    tm = TextMap.empty(width, height, fill="*")
    expected_lines = ["****", "****", "****"]
    assert tm.as_lines() == expected_lines
    assert tm.width == 4
    assert tm.height == 3


def test_empty_with_default_fill():
    """Test creating an empty TextMap with default fill character (space)."""
    width, height = 2, 2
    tm = TextMap.empty(width, height)
    expected_lines = ["  ", "  "]
    assert tm.as_lines() == expected_lines
    assert tm.width == 2
    assert tm.height == 2


def test_empty_zero_dimensions():
    """Test creating an empty TextMap with zero width and/or height."""
    with pytest.raises(ValueError):
        TextMap.empty(0, 3)

    with pytest.raises(ValueError):
        TextMap.empty(3, 0)


def test_empty_with_unicode_fill():
    """Test creating an empty TextMap with Unicode characters as fill."""
    width, height = 2, 2
    fill = "😊"
    tm = TextMap.empty(width, height, fill=fill)
    expected_lines = ["😊😊", "😊😊"]
    assert tm.as_lines() == expected_lines
    assert tm.width == 2
    assert tm.height == 2
