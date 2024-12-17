"""Helpers for AoC."""

from .loader import Loader
from .data_files import DataFiles
from . import grid, number, types

DATA = DataFiles()


__all__ = [
    "DATA",
    "DataFiles",
    "grid",
    "Loader",
    "number",
    "types",
]
