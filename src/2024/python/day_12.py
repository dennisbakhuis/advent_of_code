"""AoC 2024 - Day 12."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 12


def get_plant_groups(input_file: Path) -> list[set[tuple[int, int]]]:
    """Get groups of connected plant cells."""
    tm = aoc.Loader(input_file).as_textmap()
    plant_types = set(tm.as_string().replace("\n", ""))

    plant_groups = [
        group
        for plant_type in plant_types
        for group in aoc.grid.group_adjacent(tm.find_all(plant_type))
    ]

    return plant_groups


def part1(input_file: Path) -> int:
    """Solution 2024 / day 12 part 1."""
    plant_groups = get_plant_groups(input_file)

    total_price = 0
    for group in plant_groups:
        area = len(group)
        perimeter = aoc.grid.perimeter(group)
        price = area * perimeter
        total_price += price

    return total_price


def part2(input_file: Path) -> int:
    """Solution 2024 / day 12 part 2."""
    plant_groups = get_plant_groups(input_file)

    total_price = 0
    for group in plant_groups:
        area = len(group)
        holes = aoc.grid.find_holes(group)

        filled_area = group | holes
        corners = aoc.grid.count_corners(filled_area)

        additional_corners = 0
        for hole_group in aoc.grid.group_adjacent(holes):
            additional_corners += aoc.grid.count_corners(hole_group)

        price = area * (corners + additional_corners)
        total_price += price

    return total_price


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 1930
ANSWER_EXAMPLE_PART_2 = 1206
ANSWER_INPUT_PART_1 = 1304764
ANSWER_INPUT_PART_2 = 811148

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
