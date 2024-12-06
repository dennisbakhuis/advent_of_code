"""Data loader class."""
from pathlib import Path

from .textmap import TextMap


class Loader:
    """Data loader class."""

    def __init__(self, path: Path):
        """Initialize loader."""
        self.path = path

    def as_string(self) -> str:
        """Load data as string."""
        with open(self.path, "r") as file:
            return file.read()

    def as_lines(self) -> list:
        """Load data as list of lines."""
        with open(self.path, "r") as file:
            return [line.strip() for line in file.readlines() if line.strip()]

    def as_2dlist(self) -> list:
        """Load data as 2D list."""
        with open(self.path, "r") as file:
            return [list(line.strip()) for line in file.readlines()]

    def as_textmap(self) -> TextMap:
        """Load data as TextMap object."""
        return TextMap(self.as_lines())
