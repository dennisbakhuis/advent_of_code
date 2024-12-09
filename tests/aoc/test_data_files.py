"""Tests for the DataFiles class."""

import pytest
from pathlib import Path
from io import StringIO
from unittest.mock import patch
from aoc import DataFiles


@pytest.fixture
def mock_data_structure(tmp_path: Path):
    """
    Create a mock directory structure with input and example files.

    Structure:
    tmp_path/
        2022/
            data/
                day_01_input.txt
                day_01_example.txt
                day_02_input.txt
                day_02_example_1.txt
                day_02_example_2.txt
        2023/
            data/
                day_01_input.txt
                day_01_example.txt

    Returns
    -------
    Path
        The temporary base directory.
    """
    # Create year directories
    y2022 = tmp_path / "2022" / "data"
    y2022.mkdir(parents=True)
    y2023 = tmp_path / "2023" / "data"
    y2023.mkdir(parents=True)

    # Files for 2022
    (y2022 / "day_01_input.txt").write_text("Input for day 1, 2022")
    (y2022 / "day_01_example.txt").write_text("Example for day 1, 2022")
    (y2022 / "day_02_input.txt").write_text("Input for day 2, 2022")
    (y2022 / "day_02_example_1.txt").write_text("Example 1 for day 2, 2022")
    (y2022 / "day_02_example_2.txt").write_text("Example 2 for day 2, 2022")

    # Files for 2023
    (y2023 / "day_01_input.txt").write_text("Input for day 1, 2023")
    (y2023 / "day_01_example.txt").write_text("Example for day 1, 2023")

    return tmp_path


@pytest.fixture
def datafiles_instance(mock_data_structure):
    """
    Create a DataFiles instance with the provided mock base path.

    Returns
    -------
    DataFiles
        A DataFiles instance pointed to the mock directory structure.
    """
    return DataFiles(base_path=mock_data_structure)


def test_initialization(datafiles_instance):
    """
    Test DataFiles initialization.

    Ensures that input_files and example_files dictionaries are populated
    correctly upon initialization.
    """
    df = datafiles_instance
    # Check input files
    assert (2022, 1) in df.input_files
    assert (2022, 2) in df.input_files
    assert (2023, 1) in df.input_files

    # Check example files
    assert (2022, 1) in df.example_files
    assert (2022, 2) in df.example_files
    assert (2023, 1) in df.example_files


def test_input_files(datafiles_instance):
    """
    Test input_files dictionary.

    Ensures that the correct input files are found and indexed by (year, day).
    """
    df = datafiles_instance
    assert df.input_files[(2022, 1)].name == "day_01_input.txt"
    assert df.input_files[(2022, 2)].name == "day_02_input.txt"
    assert df.input_files[(2023, 1)].name == "day_01_input.txt"


def test_example_files_single(datafiles_instance):
    """
    Test example_files dictionary for cases with a single example file per day.

    Ensures that when only one example file is present, the value is a single Path.
    """
    df = datafiles_instance
    # For 2022, day 1 and for 2023, day 1 there's only one example file.
    assert isinstance(df.example_files[(2022, 1)], Path)
    assert df.example_files[(2022, 1)].name == "day_01_example.txt"
    assert isinstance(df.example_files[(2023, 1)], Path)
    assert df.example_files[(2023, 1)].name == "day_01_example.txt"


def test_example_files_multiple(datafiles_instance):
    """
    Test example_files dictionary for cases with multiple example files per day.

    Ensures that when multiple example files are present, the value is a dict mapping integers to Paths.
    """
    df = datafiles_instance
    assert isinstance(df.example_files[(2022, 2)], dict)
    example_dict = df.example_files[(2022, 2)]
    assert 1 in example_dict
    assert 2 in example_dict
    assert example_dict[1].name == "day_02_example_1.txt"
    assert example_dict[2].name == "day_02_example_2.txt"


def test_no_data_files(tmp_path):
    """
    Test initialization when no data files are found.

    Ensures that empty dictionaries are created if no matching files exist.
    """
    df = DataFiles(base_path=tmp_path)
    assert df.input_files == {}
    assert df.example_files == {}


def test_show_data_files(datafiles_instance):
    """
    Test the show_data_files method.

    Ensures that input and example files are printed correctly.
    """
    df = datafiles_instance
    with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
        df.show_data_files()
        output = mock_stdout.getvalue()
    # Just check a few strings to ensure correct printing
    assert "Input files:" in output
    assert "(2022, 1)" in output
    assert "day_01_input.txt" in output
    assert "Example files:" in output
    assert "(2022, 2)" in output
    assert "day_02_example_2.txt" in output
