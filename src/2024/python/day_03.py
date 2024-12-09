"""AoC 2024 - Day 3."""

from pathlib import Path
import re

import aoc  # AoC helpers


YEAR = 2024
DAY = 3


def part1(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    string = aoc.Loader(data_file).as_string()

    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, string)

    pattern = r"mul\((\d+),(\d+)\)"
    products = [int(a) * int(b) for a, b in re.findall(pattern, ",".join(matches))]

    return sum(products)


def part2(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    string = aoc.Loader(data_file).as_string()

    mul_pattern = r"mul\(\d+,\d+\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    matches = []
    for pattern in [mul_pattern, do_pattern, dont_pattern]:
        matches += [(match.start(), match.group()) for match in re.finditer(pattern, string)]

    matches = list(sorted(matches, key=lambda x: x[0]))

    products = []
    do_multiply = True
    for match in matches:
        command = match[1]
        if command.startswith("mul(") and do_multiply:
            pattern = r"mul\((\d+),(\d+)\)"
            a, b = re.match(pattern, command).groups()
            products.append(int(a) * int(b))
        elif command.startswith("don"):
            do_multiply = False
        elif command.startswith("do"):
            do_multiply = True

    return sum(products)


example_file_1: Path = aoc.DATA.example_files[(YEAR, DAY)][1]
example_file_2: Path = aoc.DATA.example_files[(YEAR, DAY)][2]
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 161
ANSWER_EXAMPLE_PART_2 = 48
ANSWER_INPUT_PART_1 = 178886550
ANSWER_INPUT_PART_2 = 87163705

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file_1)}")
    assert part1(example_file_1) == ANSWER_EXAMPLE_PART_1

    print(f"Solution (input) part 1: {part1(input_file)}")
    assert part1(input_file) == ANSWER_INPUT_PART_1

    # --- Part Two ---

    print(f"Solution (example) part 2: {part2(example_file_2)}")
    assert part2(example_file_2) == ANSWER_EXAMPLE_PART_2

    print(f"Solution (input) part 2: {part2(input_file)}")
    assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
