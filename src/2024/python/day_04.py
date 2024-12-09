"""AoC 2024 - Day 4."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 4


def part1(data_file: Path) -> int:
    """
    Find XMAS in text.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    textmap = aoc.Loader(data_file).as_textmap()
    padded = textmap.pad(3, ".")
    word_start_locations = padded.find_all("X")

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
            word = "".join([padded.get(x + i * dx, y + i * dy) for i in range(4)])
            if word == "XMAS":
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
    textmap = aoc.Loader(data_file).as_textmap()

    count = 0
    for x in range(textmap.width - 2):
        for y in range(textmap.height - 2):
            letters = "".join(
                textmap.get_many([(x, y), (x, y + 2), (x + 1, y + 1), (x + 2, y), (x + 2, y + 2)])
            )

            if letters in ["MSAMS", "SMASM", "SSAMM", "MMASS"]:
                count += 1

    return count


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 18
ANSWER_EXAMPLE_PART_2 = 9
ANSWER_INPUT_PART_1 = 2401
ANSWER_INPUT_PART_2 = 1822

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file)}")
    assert part1(example_file) == ANSWER_EXAMPLE_PART_1

    print(f"Solution (input) part 1: {part1(input_file)}")
    assert part1(input_file) == ANSWER_INPUT_PART_1

    # --- Part Two ---

    print(f"Solution (example) part 2: {part2(example_file)}")
    assert part2(example_file) == ANSWER_EXAMPLE_PART_2

    print(f"Solution (input) part 2: {part2(input_file)}")
    assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
