"""Tests for the `Loader` class."""

import pytest
from pathlib import Path
from aoc import Loader
from aoc import TextMap


@pytest.fixture
def sample_file(tmp_path: Path):
    """
    Create a temporary file with several lines and a trailing empty line.

    Returns
    -------
    Path
        Path to the created sample file.
    """
    p = tmp_path / "sample.txt"
    p.write_text("line1\nline2\n\nline3\n")
    return p


@pytest.fixture
def empty_file(tmp_path: Path):
    """
    Create an empty temporary file.

    Returns
    -------
    Path
        Path to the created empty file.
    """
    p = tmp_path / "empty.txt"
    p.write_text("")
    return p


def test_as_string(sample_file: Path):
    """
    Test that `as_string` returns the entire file contents as a single string, stripping trailing whitespace.

    Ensures that final newlines are removed. The `sample_file` ends with a
    trailing newline, and the returned string should not.
    """
    loader = Loader(sample_file)
    assert loader.as_string() == "line1\nline2\n\nline3"


def test_as_string_empty(empty_file: Path):
    """Test that `as_string` on an empty file returns an empty string."""
    loader = Loader(empty_file)
    assert loader.as_string() == ""


def test_as_lines_single_part(sample_file: Path):
    """
    Test that `as_lines` with `multiple_parts=False` returns a list of non-empty lines.

    Empty lines should be filtered out.
    """
    loader = Loader(sample_file)
    assert loader.as_lines(multiple_parts=False) == ["line1", "line2", "line3"]


def test_as_lines_multiple_parts(sample_file: Path):
    """
    Test for as_lines with multiple_parts=True.

    Test that `as_lines` with `multiple_parts=True` returns a list of lists,
    each representing a block of lines separated by empty lines.
    """
    loader = Loader(sample_file)
    assert loader.as_lines(multiple_parts=True) == [["line1", "line2"], ["line3"]]


def test_as_lines_empty(empty_file: Path):
    """
    Tests for as_lines with empty files.

    Test that `as_lines` returns an empty list for empty files, regardless of
    the `multiple_parts` parameter.
    """
    loader = Loader(empty_file)
    assert loader.as_lines(multiple_parts=False) == []
    assert loader.as_lines(multiple_parts=True) == []


def test_as_lines_no_empty_lines(tmp_path: Path):
    """
    Test `as_lines` behavior when the file has no empty lines.

    Checks both single-part and multiple-parts modes. In multiple-parts mode,
    the entire file should be one single block.
    """
    p = tmp_path / "no_empty_lines.txt"
    p.write_text("a\nb\nc\n")
    loader = Loader(p)
    assert loader.as_lines(multiple_parts=False) == ["a", "b", "c"]
    assert loader.as_lines(multiple_parts=True) == [["a", "b", "c"]]


def test_as_lines_trailing_empty_lines(tmp_path: Path):
    """
    Test `as_lines` with trailing empty lines only.

    Ensures that when the file contains only empty lines (or trailing empty
    lines after non-empty ones), `as_lines` handles them correctly.
    """
    p = tmp_path / "trailing_empty_lines.txt"
    p.write_text("x\n\n\n")
    loader = Loader(p)
    assert loader.as_lines(multiple_parts=False) == ["x"]
    assert loader.as_lines(multiple_parts=True) == [["x"]]


def test_as_textmap(sample_file: Path):
    """
    Test that `as_textmap` returns a `TextMap` object containing lines from the file.

    Verifies that the `TextMap` object receives lines from `as_lines` with
    `multiple_parts=False`.
    """
    loader = Loader(sample_file)
    result = loader.as_textmap()
    assert isinstance(result, TextMap)
    assert result.as_lines() == ["line1", "line2", "line3"]


def test_as_textmap_empty(empty_file: Path):
    """
    Tests for as_textmap with empty files.

    Test that `as_textmap` returns a `TextMap` object with an empty lines list
    for an empty file.
    """
    loader = Loader(empty_file)
    result = loader.as_textmap()

    assert isinstance(result, TextMap)
    assert result.as_lines() == []
