"""Module for working with ASCII maps."""

import re
from typing import Iterable

from .coordinate import Coordinate
from .general_types import Bounds
from ..grid.within_bounds import within_bounds


class TextMap:
    """Holds and manipulates an ASCII map."""

    def __init__(self, map_as_lines: list[str], padding_char: str = " ") -> None:
        """
        Initialize the map from a list of strings.

        Ensure that all lines are of equal length
        by padding shorter lines with the specified padding character.

        Parameters
        ----------
        map_as_lines : list of str
            Lines representing the ASCII map.
        padding_char : str, optional
            Character to use for padding shorter lines (default is space).
        """
        if map_as_lines:
            self._n_rows = len(map_as_lines)
            self._n_columns = max(len(line) for line in map_as_lines)

            # Pad each line to the maximum length with the padding character
            padded_lines = [line.ljust(self._n_columns, padding_char) for line in map_as_lines]
            self._map_string = "".join(padded_lines)
        else:
            self._n_rows = 0
            self._n_columns = 0
            self._map_string = ""

    @classmethod
    def from_string(cls, map_string: str) -> "TextMap":
        """
        Create a TextMap from a string.

        Parameters
        ----------
        map_string : str
            ASCII map as a single string.

        Returns
        -------
        TextMap
            A new map object.
        """
        return cls(map_string.splitlines())

    @classmethod
    def new(cls, width: int, height: int, fill: str = " ") -> "TextMap":
        """
        Create an new map with the specified dimensions.

        Parameters
        ----------
        width : int
            Width of the map.
        height : int
            Height of the map.
        fill : str, optional
            Character to fill the map with (default is space).

        Returns
        -------
        TextMap
            A new map object.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")

        return cls([fill * width for _ in range(height)])

    def empty(self, fill: str = " ") -> "TextMap":
        """
        Create an empty map with the same dimensions as original map.

        Parameters
        ----------
        fill : str, optional
            Character to fill the map with (default is space).

        Returns
        -------
        TextMap
            A new map object.
        """
        return self.new(self._n_columns, self._n_rows, fill)

    @property
    def width(self) -> int:
        """Width of the map."""
        return self._n_columns

    @property
    def height(self) -> int:
        """Height of the map."""
        return self._n_rows

    @property
    def bounds(self) -> Bounds:
        """Bounds of the map as (min_x, min_y, max_x, max_y)."""
        return 0, 0, self._n_columns - 1, self._n_rows - 1

    def get(self, x: int | Coordinate, y: int = None, out_of_bounds_character: str = "") -> str:
        """
        Get the character at the given coordinates.

        Parameters
        ----------
        x : int | Coordinate
            X-coordinate (column) as an integer or a tuple containing (x, y).
        y : int, optional
            Y-coordinate (row). Required if `x` is an integer.
        out_of_bounds_character : str, optional
            Character to return if coordinates are out of bounds. Defaults to "".

        Returns
        -------
        str
            Character at the specified coordinates.

        Raises
        ------
        TypeError
            If `x` is a tuple and `y` is also provided, or if `x` is an integer and `y` is not provided.
        ValueError
            If the coordinates are out of bounds and no `out_of_bounds_character` is provided.
        """
        if isinstance(x, tuple):
            x, y = x

        if not self.within_bounds((x, y)):
            if out_of_bounds_character:
                return out_of_bounds_character
            raise ValueError(f"Coordinates ({x}, {y}) are out of bounds.")

        return self._map_string[y * self._n_columns + x]

    def get_many(
        self, coordinates: Iterable[Coordinate], out_of_bounds_character: str = ""
    ) -> tuple[str, ...]:
        """
        Get characters at the given coordinates.

        Parameters
        ----------
        coordinates : list of (x, y)
            Coordinates to fetch.

        Returns
        -------
        tuple of str
            Characters at the given coordinates.
        """
        return tuple(
            self.get(x, y, out_of_bounds_character=out_of_bounds_character) for x, y in coordinates
        )

    def __eq__(self, other: "TextMap") -> bool:
        """Check if two TextMap objects are equal based on _map_string."""
        if not isinstance(other, TextMap):
            raise NotImplementedError
        return self._map_string == other._map_string

    def __ne__(self, other: "TextMap") -> bool:
        """Check if two TextMap objects are not equal based on _map_string."""
        return not self.__eq__(other)

    def set(self, x: int | Coordinate, y: int | None = None, value: str = ...) -> None:
        """
        Set the character at the given coordinates.

        Parameters
        ----------
        x : int or Coordinate
            X-coordinate (column) or a tuple of (x, y) coordinates.
        y : int, optional
            Y-coordinate (row). Required if `x` is an integer.
        value : str
            Character to place at the specified coordinates.

        Raises
        ------
        TypeError
            If arguments do not match expected types.
        ValueError
            If y is not provided when x is an integer or if the tuple does not have exactly two elements.
        IndexError
            If the coordinates are out of bounds.
        """
        if isinstance(x, tuple):
            if not isinstance(y, str):
                raise TypeError("When providing a tuple for coordinates, do not provide 'y'.")
            if len(x) != 2:
                raise ValueError("Tuple must have exactly two elements (x, y).")
            current_x, current_y = x
            value = y
        elif isinstance(x, int) and isinstance(y, int):
            current_x, current_y = x, y
        else:
            raise TypeError("set() expects either two integers (x, y) or a single tuple (x, y).")

        if not (0 <= current_x < self._n_columns) or not (0 <= current_y < self._n_rows):
            raise IndexError("Coordinates are out of bounds.")

        ix = current_y * self._n_columns + current_x

        self._map_string = self._map_string[:ix] + value + self._map_string[ix + 1 :]

    def set_many(self, coordinates: Iterable[Coordinate], value: str) -> None:
        """
        Set the character at the given coordinates.

        Parameters
        ----------
        coordinates : list of (x, y)
            Coordinates to set.
        value : str
            Character to place at the coordinates.
        """
        for x, y in coordinates:
            self.set(x, y, value)

    def find(self, value: str) -> Coordinate:
        """
        Find the first occurrence of a character.

        Parameters
        ----------
        value : str
            Character to find.

        Returns
        -------
        tuple of int
            Coordinates (x, y) of the character.
        """
        i = self._map_string.index(value)
        return Coordinate(i % self._n_columns, i // self._n_columns)

    def find_all(self, value: str) -> list[Coordinate]:
        """
        Find all occurrences of a character.

        Parameters
        ----------
        value : str
            Character to find.

        Returns
        -------
        list of tuple of int
            All coordinates (x, y) of the character.
        """
        return [
            Coordinate(ix % self._n_columns, ix // self._n_columns)
            for ix, c in enumerate(self._map_string)
            if c == value
        ]

    def as_lines(self) -> list[str]:
        """
        Convert the internal string back into a list of lines.

        Returns
        -------
        list of str
            Each line of the ASCII map.
        """
        if not self._map_string:
            return []

        return [
            self._map_string[i : i + self._n_columns]
            for i in range(0, len(self._map_string), self._n_columns)
        ]

    def show(self) -> None:
        """Show the map."""
        for line in self.as_lines():
            print(line)

    def copy(self) -> "TextMap":
        """
        Create a deep copy of the map.

        Returns
        -------
        TextMap
            A new map with the same content.
        """
        return TextMap(self.as_lines())

    def pad(self, pading_size: int | tuple[int, int, int, int], fill: str = " ") -> "TextMap":
        """
        Add padding to the ASCII map on specified sides.

        Parameters
        ----------
        padding_size : int or list of int
            Amount of padding to add. If an integer, it is applied to all sides.
            If a list, specify [top, bottom, left, right].
        fill : str
            Character to use for padding.

        Returns
        -------
        TextMap
            A new map with the padding applied.
        """
        if isinstance(pading_size, int):
            top = bottom = left = right = pading_size
        elif isinstance(pading_size, list) and len(pading_size) == 4:
            top, bottom, left, right = pading_size
        else:
            raise ValueError(
                "Padding must be an integer or a list of 4 integers [top, bottom, left, right]."
            )

        lines = self.as_lines()

        # Add padding at the top and bottom
        lines = (
            [fill * (self._n_columns + left + right)] * top
            + [fill * left + line + fill * right for line in lines]
            + [fill * (self._n_columns + left + right)] * bottom
        )

        return TextMap(lines)

    def as_string(self) -> str:
        """Return the map as a string."""
        return self._map_string

    def within_bounds(self, coordinates: Coordinate | Iterable[Coordinate]) -> bool:
        """
        Check if the coordinates are inside the map.

        Parameters
        ----------
        x : int
            X-coordinate (column).
        y : int
            Y-coordinate (row).

        Returns
        -------
        bool
            True if the coordinates are outside the map, False otherwise.
        """
        return within_bounds(coordinates, self.bounds)

    def find_horizontal_numbers(self) -> list[tuple[int, Coordinate, Coordinate]]:
        """
        Identify and locate all horizontal numbers (sequences of consecutive digits) in the ASCII map.

        Returns
        -------
        list of tuple[int, tuple[int, int], tuple[int, int]]
            A list where each dictionary contains:
                - 'number' (int): The numeric value of the sequence.
                - 'start' (tuple of int): The starting position as (row, column).
                - 'end' (tuple of int): The ending position as (row, column).
        """
        horizontal_numbers = []
        lines = self.as_lines()

        for row_idx, line in enumerate(lines):
            for match in re.finditer(r"\d+", line):
                number_str = match.group()
                start_col = match.start()
                end_col = match.end() - 1  # inclusive end index
                number = int(number_str)
                horizontal_numbers.append(
                    (
                        number,
                        (start_col, row_idx),
                        (end_col, row_idx),
                    )
                )

        return horizontal_numbers

    def switch_tiles(
        self,
        coordinate_pairs: Iterable[tuple[Coordinate, Coordinate]],
    ) -> None:
        """
        Switch tiles in the map.

        Parameters
        ----------
        coordinate_pairs : list of tuple of tuple of int
            List of coordinate pairs to switch.
        """
        for (x1, y1), (x2, y2) in coordinate_pairs:
            if self.within_bounds((x1, y1)) and self.within_bounds((x2, y2)):
                tile1 = self.get(x1, y1)
                tile2 = self.get(x2, y2)
                self.set(x1, y1, tile2)
                self.set(x2, y2, tile1)
