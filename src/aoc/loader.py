"""Data loader class."""

from pathlib import Path
import re

from .types import TextMap


REGEX_ALL_NUMBERS = re.compile(r"-?\d+")


class Loader:
    """Data loader class."""

    def __init__(self, path: Path):
        """Initialize loader."""
        self.path = path

    def as_string(self) -> str:
        """Load data as string."""
        with open(self.path, "r") as file:
            return file.read().strip()

    def as_lines(self) -> list[str]:
        """Load data as a list of lines."""
        with open(self.path, "r") as file:
            lines = [line.strip() for line in file.readlines() if line.strip()]

        return lines

    def as_multiple_parts_of_lines(self) -> list[list[str]]:
        """Load data as a list of lists of lines which are separated by a blank line."""
        with open(self.path, "r") as file:
            lines = [line.strip() for line in file.readlines()]

        blocks, current_block = [], []
        for line in lines:
            if line:
                current_block.append(line)
            else:
                if current_block:
                    blocks.append(current_block)
                    current_block = []
        if current_block:
            blocks.append(current_block)

        return blocks

    def as_list_of_integers(self) -> tuple[tuple[int, ...]]:
        """Load data as a tuple of tuples of integers."""
        return tuple(tuple(map(int, REGEX_ALL_NUMBERS.findall(line))) for line in self.as_lines())

    def as_textmap(self) -> TextMap:
        """Load data as TextMap object."""
        return TextMap(self.as_lines())  # type: ignore
