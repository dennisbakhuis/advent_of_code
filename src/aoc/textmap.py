"""Module for working with ASCII maps."""


class TextMap:
    """Holds and manipulates an ASCII map."""

    def __init__(self, map_as_lines: list[str]) -> None:
        """
        Initialize the map from a list of strings.

        Parameters
        ----------
        map_as_lines : list of str
            Lines representing the ASCII map.
        """
        self._n_rows = len(map_as_lines)
        self._n_columns = len(map_as_lines[0])
        self._map_string = "".join(map_as_lines)

    @property
    def width(self) -> int:
        """Width of the map."""
        return self._n_columns

    @property
    def height(self) -> int:
        """Height of the map."""
        return self._n_rows

    def get(self, x: int, y: int) -> str:
        """
        Get the character at the given coordinates.

        Parameters
        ----------
        x : int
            X-coordinate (column).
        y : int
            Y-coordinate (row).

        Returns
        -------
        str
            Character at (x, y).
        """
        return self._map_string[y * self._n_columns + x]

    def get_many(self, coords: list[tuple[int, int]]) -> tuple[str]:
        """
        Get characters at the given coordinates.

        Parameters
        ----------
        coords : list of (x, y)
            Coordinates to fetch.

        Returns
        -------
        tuple of str
            Characters at the given coordinates.
        """
        return tuple(self._map_string[y * self._n_columns + x] for x, y in coords)

    def set(self, x: int, y: int, value: str) -> None:
        """
        Set the character at the given coordinates.

        Parameters
        ----------
        x : int
            X-coordinate (column).
        y : int
            Y-coordinate (row).
        value : str
            Character to place at (x, y).
        """
        if (0 <= x < self._n_columns and 0 <= y < self._n_rows):
            ix = y * self._n_columns + x
            self._map_string = self._map_string[:ix] + value + self._map_string[ix + 1:]

    def find(self, value: str) -> tuple[int, int]:
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
        return i % self._n_columns, i // self._n_columns

    def find_all(self, value: str) -> list[tuple[int, int]]:
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
        return [(ix % self._n_columns, ix // self._n_columns)
                for ix, c in enumerate(self._map_string) if c == value]

    def as_lines(self) -> list[str]:
        """
        Convert the internal string back into a list of lines.

        Returns
        -------
        list of str
            Each line of the ASCII map.
        """
        return [self._map_string[i:i + self._n_columns] for i in range(0, len(self._map_string), self._n_columns)]

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

    def pad(self, pading_size: int | list[int], fill: str = " ") -> "TextMap":
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
            raise ValueError("Padding must be an integer or a list of 4 integers [top, bottom, left, right].")

        lines = self.as_lines()

        # Add padding at the top and bottom
        lines = [fill * (self._n_columns + left + right)] * top + \
                [fill * left + line + fill * right for line in lines] + \
                [fill * (self._n_columns + left + right)] * bottom

        return TextMap(lines)

    def as_string(self) -> str:
        """Return the map as a string."""
        return self._map_string

    def within_bounds(self, x: int, y: int) -> bool:
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
        return  0 <= x < self._n_columns and 0 <= y < self._n_rows
