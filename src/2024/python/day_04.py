"""AoC 2024 - Day 4."""
from pathlib import Path

import aoc  # AoC helpers


def part1(data_file: Path) -> int:
    """
    Find XMAS in text.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    list_2d = aoc.Loader(data_file).as_textmap()

    word = np.array(["X", "M", "A", "S"])

    array = np.array(list_2d)
    padded_array = np.pad(array, 3, constant_values=".")
    word_start_locations = np.argwhere(padded_array == "X")

    count = 0
    directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    for x, y in word_start_locations:
        for dx, dy in directions:
            slice = [
                padded_array[x + i * dx, y + i * dy]
                for i in range(4)
            ]
            if np.array_equal(slice, word):
                count += 1

    return count


def part2(data_file: Path) -> int:
    """
    Find XMAS in text.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    list_2d = aoc.Loader(data_file).as_2dlist()
    array = list_2d

    count = 0
    for x in range(array.shape[0] - 2):
        for y in range(array.shape[1] - 2):
            letters = array[x, y] + array[x][y+2] + array[x+1][y+1] + array[x+2][y] + array[x+2][y+2]

            if letters in ["MSAMS", "SMASM", "SSAMM", "MMASS"]:
                count += 1


    return count


example_file = aoc.DATA.example_files[(2024, 4)]
input_file = aoc.DATA.input_files[(2024, 3)]

# print(f"Solution part 1: {part1(example_file)}")
print(f"Solution part 2: {part2(example_file)}")

# print(f"Solution part 1: {part1(input_file)}")
# print(f"Solution part 2: {part2(input_file)}")

