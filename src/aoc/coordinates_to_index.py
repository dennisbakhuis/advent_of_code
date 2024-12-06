"""Convert 2D coordinates to a 1D array index."""


def coordinates_to_index(cx, cy, row_length):
    """
    Convert 2D coordinates to a 1D array index.

    Parameters
    ----------
    row : int
        The row index in the 2D array.
    col : int
        The column index in the 2D array.
    cols : int
        The number of columns in the 2D array.

    Returns
    -------
    int
        The index in the 1D array.
    """
    return cy * row_length + cx
