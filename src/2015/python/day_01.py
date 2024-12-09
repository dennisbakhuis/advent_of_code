"""AoC 2015 - Day 1."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2015
DAY = 1


def part1(file_path: Path) -> int:
    """Count the number of floors Santa has to go up or down."""
    string = aoc.Loader(file_path).as_string()

    return string.count("(") - string.count(")")


def part2(file_path: Path) -> int:
    """Find the position of the first character that causes Santa to enter the basement."""
    string = aoc.Loader(file_path).as_string()

    for ix in range(len(string)):
        if string[:ix].count("(") - string[:ix].count(")") == -1:
            return ix


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = -4
ANSWER_EXAMPLE_PART_2 = 1
ANSWER_INPUT_PART_1 = 74
ANSWER_INPUT_PART_2 = 1795

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
