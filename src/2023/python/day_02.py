"""AoC 2023 - Day 2."""

from pathlib import Path
import re
import math

import aoc  # AoC helpers


YEAR = 2023
DAY = 2


POSSIBLE = {"red": 12, "green": 13, "blue": 14}
REGEX_COLOR_FINDER = re.compile(r"(\d+) (red|green|blue)")


def part1(input_file: Path) -> int:
    """Solution 2023 / day 2 part 1."""
    lines = aoc.Loader(input_file).as_lines()

    summed_possible_game_ids = 0
    for game_id, game in enumerate(lines, start=1):
        for n, color in REGEX_COLOR_FINDER.findall(game):
            if POSSIBLE[color] < int(n):
                break
        else:
            summed_possible_game_ids += game_id

    return summed_possible_game_ids


def part2(input_file: Path):
    """Solution 2023 / day 2 part 2."""
    lines = aoc.Loader(input_file).as_lines()

    total = 0
    for game in lines:
        maximum_cubes = {"red": 0, "green": 0, "blue": 0}

        for number_of_cubes, color in REGEX_COLOR_FINDER.findall(game):
            maximum_cubes[color] = max(int(number_of_cubes), maximum_cubes[color])

        total += math.prod(maximum_cubes.values())

    return total


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 8
ANSWER_EXAMPLE_PART_2 = 2286
ANSWER_INPUT_PART_1 = 2447
ANSWER_INPUT_PART_2 = 56322

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
