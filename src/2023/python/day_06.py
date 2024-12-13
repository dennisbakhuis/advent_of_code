"""AoC 2023 - Day 6."""

from pathlib import Path
import re
import math

import aoc  # AoC helpers


YEAR = 2023
DAY = 6


def get_time_distance(input_file: Path) -> tuple[list[int], list[int]]:
    """Get time and distance from input file."""
    lines = aoc.Loader(input_file).as_lines()

    time, distance = [tuple(int(x) for x in re.findall(r"\d+", line)) for line in lines]

    return time, distance


def solve_inequality(distance, time):
    """Solve the inequality x^2 + distance < time * x."""
    d = time**2 - 4 * distance

    if d < 0:
        return []

    sqrt_d = math.sqrt(d)
    r1 = (time - sqrt_d) / 2
    r2 = (time + sqrt_d) / 2

    start = math.ceil(r1)
    end = math.floor(r2)

    result = []
    for x in range(start, end + 1):
        if x**2 + distance < time * x:
            result.append(x)

    return result


def part1(input_file: Path) -> int:
    """Solution 2023 / day 6 part 1."""
    time, distance = get_time_distance(input_file)

    possibilities = []
    for t, d in zip(time, distance, strict=True):
        possibilities.append(len(solve_inequality(d, t)))

    return math.prod(possibilities)


def part2(input_file: Path) -> int:
    """Solution 2023 / day 6 part 2."""
    time, distance = get_time_distance(input_file)

    new_time = int("".join(str(x) for x in time))
    new_distance = int("".join(str(x) for x in distance))

    possibilities = solve_inequality(new_distance, new_time)

    return len(possibilities)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 288
ANSWER_EXAMPLE_PART_2 = 71503
ANSWER_INPUT_PART_1 = 4811940
ANSWER_INPUT_PART_2 = 30077773

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
