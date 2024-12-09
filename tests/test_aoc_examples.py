"""Test examples from all Advent of Code puzzles."""

from pathlib import Path
import importlib.util
import os

import pytest


python_puzzles = list(sorted(Path("src").glob("20*/python/day*.py")))


def import_file_as_module(path):
    """Import a Python file as a module."""
    filename = os.path.basename(path)
    module_name = os.path.splitext(filename)[0]  # Extract the filename without extension
    spec = importlib.util.spec_from_file_location(module_name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("puzzle_path", python_puzzles)
def test_puzzle(puzzle_path: Path) -> None:
    """Test all AoC puzzles."""
    module = import_file_as_module(puzzle_path)

    if hasattr(module, "example_file"):
        assert module.part1(module.example_file) == module.ANSWER_EXAMPLE_PART_1
        assert module.part2(module.example_file) == module.ANSWER_EXAMPLE_PART_2

    elif hasattr(module, "example_file_1"):
        assert module.part1(module.example_file_1) == module.ANSWER_EXAMPLE_PART_1
        assert module.part2(module.example_file_2) == module.ANSWER_EXAMPLE_PART_2
