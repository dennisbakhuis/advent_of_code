"""Class to work with direction."""

from enum import Enum


class Direction(Enum):
    """
    Enum for directions, supporting both Cartesian and compass notations.

    Each direction stores its own (dx, dy) offset.

    Attributes
    ----------
    UP, NORTH : Direction
        Up/North direction (0, -1).
    DOWN, SOUTH : Direction
        Down/South direction (0, 1).
    LEFT, WEST : Direction
        Left/West direction (-1, 0).
    RIGHT, EAST : Direction
        Right/East direction (1, 0).
    """

    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    # Compass synonyms
    NORTH = UP
    SOUTH = DOWN
    WEST = LEFT
    EAST = RIGHT

    @classmethod
    def from_label(
        cls,
        character: str,
        mapping: dict[str, "Direction"] | None = None,
    ) -> "Direction":
        """
        Get a Direction from a character ("<", "^", ">", "v").

        Parameters
        ----------
        character : str
            The character representing the direction.
        mapping : Optional[Dict[str, Direction]]
            A custom mapping from characters to Direction enum members.
            If not provided, the default mapping is used.

        Returns
        -------
        Direction
            The corresponding Direction enum member.

        Raises
        ------
        KeyError
            If the character is not found in the mapping.
        TypeError
            If the mapping does not map to Direction enum members.
        """
        if mapping is None:
            try:
                mapping = {
                    char: getattr(cls, name) for char, name in _DEFAULT_LABEL_MAPPING.items()
                }
            except AttributeError as e:  # pragma: no cover
                raise ValueError(f"Invalid direction name in _DEFAULT_CHAR_MAP: {e}") from e
        else:
            if not all(isinstance(direction, cls) for direction in mapping.values()):
                raise TypeError("All values in the custom mapping must be Direction enum members.")

        try:
            return mapping[character]
        except KeyError as e:
            raise KeyError(f"Character '{character}' not found in the provided mapping.") from e

    def __str__(self):
        """Represent the direction as a string."""
        return self.name

    def turn_left(self) -> "Direction":
        """
        Turn left relative to the current direction.

        Returns
        -------
        Direction
            The direction after turning left.
        """
        return _TURN_LEFT_MAPPING[self]

    def turn_right(self) -> "Direction":
        """
        Turn right relative to the current direction.

        Returns
        -------
        Direction
            The direction after turning right.
        """
        return _TURN_RIGHT_MAPPING[self]

    def move(self, x: int | tuple[int, int], y: int = None) -> tuple[int, int]:
        """
        Compute the next coordinates when moving one step in this direction.

        Parameters
        ----------
        x : int or tuple[int, int]
            Current x-coordinate or a tuple of (x, y) coordinates.
        y : int, optional
            Current y-coordinate. Required if `x` is an integer.

        Returns
        -------
        Tuple[int, int]
            New coordinates after one step in this direction.

        Raises
        ------
        TypeError
            If arguments do not match expected types.
        ValueError
            If y is not provided when x is an integer.
        """
        if isinstance(x, tuple):
            if len(x) != 2:
                raise ValueError("Tuple must have exactly two elements (x, y).")
            current_x, current_y = x
        elif isinstance(x, int) and isinstance(y, int):
            current_x, current_y = x, y
        else:
            raise TypeError("move() expects either two integers (x, y) or a single tuple (x, y).")

        dx, dy = self.value
        new_x = current_x + dx
        new_y = current_y + dy
        return new_x, new_y

    def before(self, x: int, y: int) -> tuple[int, int]:
        """
        Compute the previous coordinates when moving one step in this direction.

        Parameters
        ----------
        x : int
            Current x-coordinate.
        y : int
            Current y-coordinate.

        Returns
        -------
        (int, int)
            New coordinates after one step in this direction.
        """
        dx, dy = self.value
        return x - dx, y - dy

    def next_move_out_of_bounds(self, x: int, y: int, width: int, height: int) -> bool:
        """
        Check if the next move goes out of the given bounding box.

        Parameters
        ----------
        x : int
            Current x-coordinate.
        y : int
            Current y-coordinate.
        width : int
            Width of the area.
        height : int
            Height of the area.

        Returns
        -------
        bool
            True if the next move is out of bounds, False otherwise.
        """
        nx, ny = self.move(x, y)
        return nx < 0 or nx >= width or ny < 0 or ny >= height

    # @classmethod
    # def members(cls) -> set["Direction"]:
    #     """Return a set of all Direction members."""
    #     return set(cls)

    @classmethod
    def from_coordinates(cls, start: tuple[int, int], end: tuple[int, int]) -> "Direction":
        """
        Determine the Direction from two coordinate points.

        Coordinate system starts at (0, 0) in the top-left corner.

        Parameters
        ----------
        start : tuple[int, int]
            The starting (x, y) coordinates.
        end : tuple[int, int]
            The ending (x, y) coordinates.

        Returns
        -------
        Direction
            The direction from start to end.

        Raises
        ------
        ValueError
            If the movement does not correspond to a valid single direction.
        TypeError
            If the inputs are not tuples of two integers.
        """
        dx = end[0] - start[0]
        dy = end[1] - start[1]

        for direction in cls:
            if direction.value == (dx, dy):
                return direction

        raise ValueError(
            f"No valid direction found for movement from {start} to {end}; ({dx}, {dy})."
        )


_TURN_LEFT_MAPPING = {
    Direction.NORTH: Direction.WEST,
    Direction.WEST: Direction.SOUTH,
    Direction.SOUTH: Direction.EAST,
    Direction.EAST: Direction.NORTH,
}

_TURN_RIGHT_MAPPING = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH,
}

_DEFAULT_LABEL_MAPPING: dict[str, str] = {
    "^": "UP",
    "v": "DOWN",
    "<": "LEFT",
    ">": "RIGHT",
}
