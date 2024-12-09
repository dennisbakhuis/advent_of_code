"""Helpers for AoC."""

from .loader import Loader
from .data_files import DataFiles
from .textmap import TextMap
from . import grid, number

DATA = DataFiles()


__all__ = [
    "DATA",
    "DataFiles",
    "grid",
    "Loader",
    "number",
    "TextMap",
]
