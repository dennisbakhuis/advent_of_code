"""AoC 2023 - Day 3."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2023
DAY = 3


def part1(input_file: Path) -> int:
    """Solution 2023 / day 3 part 1."""
    textmap = aoc.Loader(input_file).as_textmap()
    all_numbers = textmap.find_horizontal_numbers()

    symbols = {x for x in set(textmap.as_string()) if x not in "0123456789."}

    sum_of_part_numbers = 0
    for number, start, end in all_numbers:
        number_coordinates = aoc.grid.get_coordinates_from_line(
            start=start,
            end=end,
        )
        surrounding_coordinates = aoc.grid.surrounding(
            number_coordinates,
            bounds=textmap.bounds,
            diagonal_sides=True,
        )
        surounded_by_symbol = any([x in symbols for x in textmap.get_many(surrounding_coordinates)])

        if surounded_by_symbol:
            sum_of_part_numbers += number

    return sum_of_part_numbers


def part2(input_file: Path) -> int:
    """Solution 2023 / day 3 part 2."""
    textmap = aoc.Loader(input_file).as_textmap()
    all_numbers = textmap.find_horizontal_numbers()

    all_number_coordinates = tuple(
        (number, aoc.grid.get_coordinates_from_line(start=start, end=end, bounds=textmap.bounds))
        for (number, start, end) in all_numbers
    )

    gear_ratio = 0
    gears = textmap.find_all("*")
    for gear in gears:
        adjacent_numbers = tuple(
            number
            for number, coordinates in all_number_coordinates
            if aoc.grid.is_adjacent(gear, coordinates, diagonal_sides=True)
        )

        if len(adjacent_numbers) == 2:
            gear_ratio += adjacent_numbers[0] * adjacent_numbers[1]

    return gear_ratio


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 4361
ANSWER_EXAMPLE_PART_2 = 467_835
ANSWER_INPUT_PART_1 = 540_131
ANSWER_INPUT_PART_2 = 86_879_020

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
