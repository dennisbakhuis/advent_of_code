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
