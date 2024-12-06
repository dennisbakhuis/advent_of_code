"""Method to convert a 1D array index to 2D coordinates."""


def index_to_coordinates(index, row_length):
    """
    Convert a 1D array index to 2D coordinates.

    Parameters
    ----------
    index : int
        The index in the 1D array.
    rows : int
        The number of rows in the 2D array.
    cols : int
        The number of columns in the 2D array.

    Returns
    -------
    tuple of int
        A tuple (row, col) representing the 2D coordinates.
    """
    y = index // row_length
    x = index % row_length
    return y, x
