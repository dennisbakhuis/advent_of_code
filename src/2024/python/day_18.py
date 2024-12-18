"""AoC 2024 - Day 18."""

from pathlib import Path

import aoc
from aoc.types import TextMap
from aoc.grid import find_shortest_path


YEAR = 2024
DAY = 18


def part1(input_file: Path) -> int:
    """Solution 2024 / day 18 part 1."""
    if "example" in input_file.stem:
        drop_index = 12
        width, height = 7, 7
    else:
        drop_index = 1024
        width, height = 71, 71

    coordinates = aoc.Loader(input_file).as_list_of_integers()
    tm = TextMap.new(width=width, height=height, fill=".")
    start = (0, 0)
    end = (width - 1, height - 1)

    for drop in coordinates[:drop_index]:
        tm.set(drop, "X")

    waypoints = tm.find_all(".")

    shortest_path = find_shortest_path(waypoints, start, end)

    steps = len(shortest_path) - 1

    return steps


def part2(input_file: Path) -> int:
    """Solution 2024 / day 18 part 2."""
    if "example" in input_file.stem:
        width, height = 7, 7
        drop_index = 0
    else:
        width, height = 71, 71
        drop_index = 1024

    coordinates = aoc.Loader(input_file).as_list_of_integers()
    tm = TextMap.new(width=width, height=height, fill=".")
    start = (0, 0)
    end = (width - 1, height - 1)
    if drop_index != 0:
        tm.set_many(coordinates[:drop_index], "X")

    while True:
        drop = coordinates[drop_index]
        tm.set(drop, "X")
        waypoints = tm.find_all(".")
        if not find_shortest_path(waypoints, start, end):
            break

        drop_index += 1

    return ",".join([str(x) for x in coordinates[drop_index]])


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 22
ANSWER_EXAMPLE_PART_2 = "6,1"
ANSWER_INPUT_PART_1 = 334
ANSWER_INPUT_PART_2 = "20,12"

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
    assert solution == ANSWER_INPUT_PART_2

    print()
