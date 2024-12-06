"""AoC 2024 - Day 3."""
from pathlib import Path
import re

import aoc  # AoC helpers


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


example_file_1 = aoc.DATA.example_files[(2024, 3)][1]
example_file_2 = aoc.DATA.example_files[(2024, 3)][2]
input_file = aoc.DATA.input_files[(2024, 3)]

print(f"Solution part 1: {part1(example_file_1)}")
print(f"Solution part 2: {part2(example_file_2)}")

print(f"Solution part 1: {part1(input_file)}")
print(f"Solution part 2: {part2(input_file)}")
