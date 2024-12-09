"""AoC 2024 - Day 8."""

from pathlib import Path
from itertools import combinations

import aoc  # AoC helpers


YEAR = 2024
DAY = 8


def part1(file_path: Path) -> int:
    """Soluiton day 9 part 1."""
    textmap = aoc.Loader(file_path).as_textmap()

    antenna_types = set(textmap.as_string())
    antenna_types.remove(".")

    antennas = {antenna_type: textmap.find_all(antenna_type) for antenna_type in antenna_types}

    antinodes = set()
    for _, locations in antennas.items():
        for node1, node2 in combinations(locations, 2):
            dx, dy = (node2[0] - node1[0], node2[1] - node1[1])

            antinodes.update(
                [
                    (node1[0] + ix * dx, node1[1] + ix * dy)
                    for ix in (-1, 2)
                    if textmap.within_bounds((node1[0] + ix * dx, node1[1] + ix * dy))
                ]
            )

    return len(antinodes)


def part2(file_path: Path) -> int:
    """Soluiton day 9 part 1."""
    textmap = aoc.Loader(file_path).as_textmap()

    antenna_types = set(textmap.as_string())
    antenna_types.remove(".")

    max_width = max(textmap.width, textmap.height)

    antennas = {antenna_type: textmap.find_all(antenna_type) for antenna_type in antenna_types}

    antinodes = set()
    for _, locations in antennas.items():
        for node1, node2 in combinations(locations, 2):
            dx, dy = (node2[0] - node1[0], node2[1] - node1[1])

            antinodes.update(
                [
                    (node1[0] + ix * dx, node1[1] + ix * dy)
                    for ix in range(-max_width, max_width)
                    if textmap.within_bounds((node1[0] + ix * dx, node1[1] + ix * dy))
                ]
            )

    return len(antinodes)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 14
ANSWER_EXAMPLE_PART_2 = 34
ANSWER_INPUT_PART_1 = 249
ANSWER_INPUT_PART_2 = 905

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
