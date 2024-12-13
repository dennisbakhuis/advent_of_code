"""AoC 2024 - Day 13."""

from pathlib import Path
import re

import aoc  # AoC helpers


YEAR = 2024
DAY = 13


def part1(input_file: Path) -> int:
    """Solution 2024 / day 13 part 1."""
    claw_machines = aoc.Loader(input_file).as_lines(multiple_parts=True)

    token_costs = (3, 1)

    costs = 0
    for machine in claw_machines:
        numbers = tuple(tuple(int(num) for num in re.findall(r"\d+", line)) for line in machine)

        # A(94 + 34jx) + B(22 + 67J) - (8400 + 5400) = 0
        # makes system of equations
        # Real: 94A + 22B = 8400
        # Imag: 34A + 67B = 5400

        ((a1, a2), (b1, b2), (c1, c2)) = numbers
        B = (c2 * a1 - c1 * a2) / (b2 * a1 - b1 * a2)
        A = (c1 - b1 * B) / a1

        if A.is_integer() and B.is_integer():
            costs += A * token_costs[0] + B * token_costs[1]

    return int(costs)


def part2(input_file: Path) -> int:
    """Solution 2024 / day 13 part 2."""
    claw_machines = aoc.Loader(input_file).as_lines(multiple_parts=True)

    token_costs = (3, 1)
    offset = 10_000_000_000_000

    costs = 0
    for machine in claw_machines:
        numbers = tuple(tuple(int(num) for num in re.findall(r"\d+", line)) for line in machine)

        # A(94 + 34jx) + B(22 + 67J) - (8400 + 5400) = 0
        # makes system of equations
        # Real: 94A + 22B = 8400
        # Imag: 34A + 67B = 5400

        ((a1, a2), (b1, b2), (c1, c2)) = numbers
        c1, c2 = c1 + offset, c2 + offset

        B = (c2 * a1 - c1 * a2) / (b2 * a1 - b1 * a2)
        A = (c1 - b1 * B) / a1

        if A.is_integer() and B.is_integer():
            costs += A * token_costs[0] + B * token_costs[1]

    return int(costs)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 480
ANSWER_EXAMPLE_PART_2 = 875318608908
ANSWER_INPUT_PART_1 = 33481
ANSWER_INPUT_PART_2 = 92572057880885

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file)}")
    assert part1(example_file) == ANSWER_EXAMPLE_PART_1

    print(f"Solution (input) part 1: {part1(input_file)}")
    assert part1(input_file) == ANSWER_INPUT_PART_1

    # # --- Part Two ---

    print(f"Solution (example) part 2: {part2(example_file)}")
    assert part2(example_file) == ANSWER_EXAMPLE_PART_2

    print(f"Solution (input) part 2: {part2(input_file)}")
    assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
