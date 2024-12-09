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
            return file.read().strip()

    def as_lines(self, multiple_parts: bool = False) -> list[str] | list[list[str]]:
        """
        Load data as a list of lines.

        Parameters
        ----------
        multiple_parts : bool, optional
            If True, return a list of lists, where each inner list represents a
            block of lines separated by one or more empty lines. If False, return
            a flat list of all non-empty lines.

        Returns
        -------
        list[str] | list[list[str]]
            A list of lines (if multiple_parts=False) or a list of lists of lines (if multiple_parts=True).
        """
        with open(self.path, "r") as file:
            lines = [line.strip() for line in file.readlines()]

        if not multiple_parts:
            return [line for line in lines if line]

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

    def as_2dlist(self) -> list:
        """Load data as 2D list."""
        with open(self.path, "r") as file:
            return [list(line.strip()) for line in file.readlines()]

    def as_textmap(self) -> TextMap:
        """Load data as TextMap object."""
        return TextMap(self.as_lines())  # type: ignore
