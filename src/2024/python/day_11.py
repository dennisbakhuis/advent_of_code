"""AoC 2024 - Day 11."""

from functools import cache
from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 11


def get_stones(input_file: Path) -> tuple[int, ...]:
    """Get the stones from the input file."""
    return tuple(int(stone) for stone in aoc.Loader(input_file).as_string().split())


@cache
def blink(stone):
    """Blink at stone."""
    if stone == 0:
        return (1,)

    string = str(stone)
    length = len(string)

    if length % 2 == 0:
        return tuple(int(n) for n in [string[: length // 2], string[length // 2 :]])

    return (stone * 2024,)


def stones_after_blinks(stone, number_of_blinks):
    """Return the number of stones after n blinks."""
    stones = {stone: 1}

    for _ in range(number_of_blinks):
        splitted_stones = {}
        for stone_number, count in stones.items():
            for stone_after_blink in blink(stone_number):
                splitted_stones[stone_after_blink] = (
                    splitted_stones.get(stone_after_blink, 0) + count
                )

        stones = splitted_stones

    return sum(stones.values())


def part1(input_file: Path) -> int:
    """Solution 2024 / day 11 part 1."""
    number_of_blinks = 6 if "example" in input_file.stem else 25

    stones = get_stones(input_file)
    n_splits = sum(stones_after_blinks(stone, number_of_blinks) for stone in stones)

    return n_splits


def part2(input_file: Path) -> int:
    """Solution 2024 / day 11 part 2."""
    number_of_blinks = 75

    stones = get_stones(input_file)
    n_splits = sum(stones_after_blinks(stone, number_of_blinks) for stone in stones)

    return n_splits


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 22
ANSWER_EXAMPLE_PART_2 = 65601038650482
ANSWER_INPUT_PART_1 = 187738
ANSWER_INPUT_PART_2 = 223767210249237

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
