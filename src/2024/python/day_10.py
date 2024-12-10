"""AoC 2024 - Day 10."""

from pathlib import Path
from collections import deque

import aoc  # AoC helpers


YEAR = 2024
DAY = 10


simple_map = """0123
1234
8765
9876"""


def get_trails(textmap: aoc.TextMap) -> set[tuple[str]]:
    """
    Get all trails from the textmap.

    I was already a bit to throrough with part 1 :-D
    and puzzled why the answer was too high.
    """
    start_locations = textmap.find_all("0")
    trails = set()

    for start in start_locations:
        queue = deque()
        queue.append([start])

        while queue:
            trail = queue.popleft()
            position = trail[-1]
            current_height = textmap.get(position)

            if current_height == "9":
                trails.add(tuple(trail))
                continue

            for surround in aoc.grid.surrounding(position, bounds=textmap.bounds):
                if textmap.get(surround) == str(int(current_height) + 1):
                    queue.append(trail + [surround])

    return trails


def part1(input_file: Path) -> int:
    """Solution 2024 / day 10 part 1."""
    textmap = aoc.Loader(input_file).as_textmap()
    # textmap = aoc.TextMap(simple_map.split("\n"))
    trails = get_trails(textmap)

    start_to_trailheads = set([(x[0], x[-1]) for x in trails])

    return len(start_to_trailheads)


def part2(input_file: Path) -> int:
    """Solution 2024 / day 10 part 2."""
    textmap = aoc.Loader(input_file).as_textmap()
    trails = get_trails(textmap)

    return len(trails)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 36
ANSWER_EXAMPLE_PART_2 = 81
ANSWER_INPUT_PART_1 = 430
ANSWER_INPUT_PART_2 = 928

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
    # assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
