"""AoC 2024 - Day 16."""

from pathlib import Path


import aoc  # AoC helpers
from aoc.types import Direction


YEAR = 2024
DAY = 16


def corner_penalty_scoring(
    _, __, previous_direction: Direction, current_direction: Direction
) -> int:
    """Scoring function that penalizes turning at corners."""
    if previous_direction == current_direction:
        return 1
    return 1001


def part1(input_file: Path) -> int:
    """Solution 2024 / day 16 part 1."""
    maze = aoc.Loader(input_file).as_textmap()

    start = maze.find("S")
    end = maze.find("E")
    way_points = tuple(maze.find_all(".") + [start, end])

    states = aoc.grid.dijkstra(way_points, start, corner_penalty_scoring)
    min_direction = min(states[end].values(), key=lambda d: d["score"])
    score = min_direction["score"]

    return score


def part2(input_file: Path) -> int:
    """Solution 2024 / day 16 part 2."""
    maze = aoc.Loader(input_file).as_textmap()

    start = maze.find("S")
    end = maze.find("E")
    way_points = tuple(maze.find_all(".") + [start, end])

    states = aoc.grid.dijkstra(way_points, start, corner_penalty_scoring)
    min_direction = min(states[end].values(), key=lambda d: d["score"])
    n_tiles = len(min_direction["tiles"]) + 1

    return n_tiles


example_file_1: Path = aoc.DATA.example_files[(YEAR, DAY)][1]
example_file_2: Path = aoc.DATA.example_files[(YEAR, DAY)][2]
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 7036
ANSWER_EXAMPLE_PART_2 = 64
ANSWER_INPUT_PART_1 = 75416
ANSWER_INPUT_PART_2 = 476


if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    answer_example_1 = part1(example_file_1)
    print(f"Solution (example) part 1: {answer_example_1}")
    assert answer_example_1 == ANSWER_EXAMPLE_PART_1

    answer_input_1 = part1(input_file)
    print(f"Solution (input) part 1: {answer_input_1}")
    assert answer_input_1 == ANSWER_INPUT_PART_1

    # # --- Part Two ---

    answer_example_2 = part2(example_file_2)
    print(f"Solution (example) part 2: {answer_example_2}")
    assert answer_example_2 == ANSWER_EXAMPLE_PART_2

    answer_input_2 = part2(input_file)
    print(f"Solution (input) part 2: {answer_input_2}")
    assert answer_input_2 == ANSWER_INPUT_PART_2

    print()
