"""AoC 2024 - Day 19."""

from pathlib import Path
from functools import cache

import aoc  # AoC helpers


YEAR = 2024
DAY = 19


def get_stock_and_designs(input_file: Path) -> tuple[dict[str, str], list[str]]:
    """Get sorted towel_stock and designs from input file."""
    towel_stock_raw, designs = aoc.Loader(input_file).as_multiple_parts_of_lines()
    towel_stock = tuple(
        sorted(
            [towel for towel in towel_stock_raw[0].split(", ")],
            key=len,
            reverse=True,
        )
    )

    return towel_stock, designs


@cache
def get_possible_towel_arrangements(design: str, towel_stock: tuple[str, ...]) -> int:
    """Find the number of towels used for a pattern."""
    used_towels = 0
    for towel in towel_stock:
        if design == towel:
            used_towels += 1
            continue

        if design.startswith(towel):
            used_towels += get_possible_towel_arrangements(
                design=design.removeprefix(towel),
                towel_stock=towel_stock,
            )

    return used_towels


@aoc.tools.timer
def part1(input_file: Path) -> int:
    """Solution 2024 / day 19 part 1."""
    towel_stock, designs = get_stock_and_designs(input_file)

    possible_designs = 0
    for design in designs:
        possible_designs += get_possible_towel_arrangements(design, towel_stock) != 0

    return possible_designs


def part2(input_file: Path) -> int:
    """Solution 2024 / day 19 part 2."""
    towel_stock, designs = get_stock_and_designs(input_file)

    total_arrangements = 0
    for design in designs:
        total_arrangements += get_possible_towel_arrangements(design, towel_stock)

    return total_arrangements


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 6
ANSWER_EXAMPLE_PART_2 = 16
ANSWER_INPUT_PART_1 = 255
ANSWER_INPUT_PART_2 = 0

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    solution = part1(example_file)
    print(f"Solution (example) part 1: {solution}")
    assert solution == ANSWER_EXAMPLE_PART_1

    solution = part1(input_file)
    print(f"Solution (input) part 1: {solution}")
    assert solution == ANSWER_INPUT_PART_1

    # # --- Part Two ---

    solution = part2(example_file)
    print(f"Solution (example) part 2: {solution}")
    assert solution == ANSWER_EXAMPLE_PART_2

    solution = part2(input_file)
    print(f"Solution (input) part 2: {solution}")
    # assert solution == ANSWER_INPUT_PART_2

    print()
