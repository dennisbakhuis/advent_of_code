"""Helpers for AoC."""
from .loader import Loader
from .data_files import DataFiles

from .coordinates_to_index import coordinates_to_index
from .index_to_coordinates import index_to_coordinates
from .direction import Direction
from .textmap import TextMap


DATA = DataFiles()


__all__ = [
    "Loader",
    "DATA",
    "coordinates_to_index",
    "index_to_coordinates",
    "Direction",
    "TextMap",
]
