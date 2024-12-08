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

    def turn_left(self) -> "Direction":
        """
        Turn left relative to the current direction.

        Returns
        -------
        Direction
            The direction after turning left.
        """
        return _left_map[self]

    def turn_right(self) -> "Direction":
        """
        Turn right relative to the current direction.

        Returns
        -------
        Direction
            The direction after turning right.
        """
        return _right_map[self]

    def move(self, x: int, y: int) -> tuple[int, int]:
        """
        Compute the next coordinates when moving one step in this direction.

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
        return x + dx, y + dy

    # def before(self, x: int, y: int) -> tuple[int, int, "Direction"]:
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


_left_map = {
    Direction.NORTH: Direction.WEST,
    Direction.WEST: Direction.SOUTH,
    Direction.SOUTH: Direction.EAST,
    Direction.EAST: Direction.NORTH,
}
_right_map = {
    Direction.NORTH: Direction.EAST,
    Direction.EAST: Direction.SOUTH,
    Direction.SOUTH: Direction.WEST,
    Direction.WEST: Direction.NORTH,
}
