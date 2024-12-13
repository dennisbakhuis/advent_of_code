"""Calculate the perimeter of a group of connected coordinates."""


def perimeter(
    coordinates: set[tuple[int, int]],
    style: str = "minecraft",
) -> int:
    """
    Calculate the perimeter of a group of connected coordinates.

    There are different styles of perimeter calculation, depending on the context.

    Styles implemented:
    - "minecraft": Only horizontal and vertical sides are considered.

    Parameters
    ----------
    coordinates : set[tuple[int, int]]
        A set of 2D coordinates (x, y) representing connected cells.
    style : str, optional
        The style of perimeter calculation (default "minecraft").

    Returns
    -------
    int
        The perimeter of the group of connected coordinates
    """
    perimeter = 0

    if style == "minecraft":
        for x, y in coordinates:
            perimeter += 4
            if (x + 1, y) in coordinates:
                perimeter -= 2
            if (x, y + 1) in coordinates:
                perimeter -= 2
    else:
        raise ValueError(f"Unknown style: {style}")

    return perimeter
