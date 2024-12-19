"""Coordinate type class."""

from __future__ import annotations


class Coordinate(tuple):
    """
    A class to represent a 2D coordinate with arithmetic operations.

    It is made compatible with the legacy tuple[int, int] type.

    Attributes
    ----------
    x : int
        The x-coordinate.
    y : int
        The y-coordinate.

    Methods
    -------
    __add__(other: Coordinate) -> Coordinate:
        Adds two coordinates component-wise.
    __sub__(other: Coordinate) -> Coordinate:
        Subtracts two coordinates component-wise.
    __mul__(scalar: int) -> Coordinate:
        Multiplies both components of the coordinate by a scalar.
    __rmul__(scalar: int) -> Coordinate:
        Allows scalar multiplication from the left.
    """

    def __new__(cls, x: int, y: int) -> Coordinate:
        """
        Create a new Coordinate instance.

        Parameters
        ----------
        x : int
            The x-coordinate.
        y : int
            The y-coordinate.

        Returns
        -------
        Coordinate
            A new Coordinate instance.
        """
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("Both x and y must be integers.")

        return super().__new__(cls, (x, y))

    @property
    def x(self) -> int:
        """int: The x-coordinate."""
        return self[0]

    @property
    def y(self) -> int:
        """int: The y-coordinate."""
        return self[1]

    def __add__(self, other: Coordinate) -> Coordinate:
        """
        Add two coordinates component-wise.

        Parameters
        ----------
        other : Coordinate
            The coordinate to add.

        Returns
        -------
        Coordinate
            The result of the addition.

        Raises
        ------
        TypeError
            If the operand is not a Coordinate instance.
        """
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Coordinate) -> Coordinate:
        """
        Subtract two coordinates component-wise.

        Parameters
        ----------
        other : Coordinate
            The coordinate to subtract.

        Returns
        -------
        Coordinate
            The result of the subtraction.

        Raises
        ------
        TypeError
            If the operand is not a Coordinate instance.
        """
        if not isinstance(other, Coordinate):
            return NotImplemented

        return Coordinate(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar: int) -> Coordinate:
        """
        Multiply both components of the coordinate by a scalar.

        Parameters
        ----------
        scalar : int
            The scalar to multiply by.

        Returns
        -------
        Coordinate
            The result of the scalar multiplication.

        Raises
        ------
        TypeError
            If the scalar is not an integer.
        """
        if not isinstance(scalar, int):
            return NotImplemented

        return Coordinate(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar: int) -> Coordinate:
        """
        Allow scalar multiplication from the left.

        Parameters
        ----------
        scalar : int
            The scalar to multiply by.

        Returns
        -------
        Coordinate
            The result of the scalar multiplication.

        Raises
        ------
        TypeError
            If the scalar is not an integer.
        """
        return self.__mul__(scalar)

    def __repr__(self) -> str:
        """
        Return a string representation of the coordinate.

        Returns
        -------
        str
            A string representing the coordinate.
        """
        return f"Coordinate(x={self.x}, y={self.y})"

    @property
    def adjacent(self) -> set[Coordinate]:
        """
        Return the adjacent coordinates.

        Returns
        -------
        set[Coordinate]
            The adjacent coordinates.
        """
        return {
            self + Coordinate(1, 0),
            self + Coordinate(-1, 0),
            self + Coordinate(0, 1),
            self + Coordinate(0, -1),
        }

    @property
    def adjacent_with_diagonal(self) -> set[Coordinate]:
        """
        Return the adjacent coordinates with diagonals.

        Returns
        -------
        set[Coordinate]
            The adjacent coordinates with diagonals.
        """
        return {
            self + Coordinate(1, 0),
            self + Coordinate(-1, 0),
            self + Coordinate(0, 1),
            self + Coordinate(0, -1),
            self + Coordinate(1, 1),
            self + Coordinate(-1, 1),
            self + Coordinate(1, -1),
            self + Coordinate(-1, -1),
        }
