"""Helpers for AoC."""

from .loader import Loader
from .data_files import DataFiles
from .direction import Direction
from .textmap import TextMap


DATA = DataFiles()


__all__ = [
    "Loader",
    "DataFiles",
    "Direction",
    "TextMap",
    "DATA",
]
