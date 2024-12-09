"""AoC 2023 - Day 4."""

from pathlib import Path
import re

import aoc  # AoC helpers


YEAR = 2023
DAY = 4


REGEX_GET_NUMBERS = re.compile(r":(.*)\|(.*)")


def parse_cards(lines: list[str]) -> tuple[int, tuple[int, set[str], set[str]]]:
    """Parse the cards from the input lines."""
    return tuple(
        (set(left.split()), set(right.split()))
        for (left, right) in (REGEX_GET_NUMBERS.findall(line)[0] for line in lines)
    )


def part1(input_file: Path) -> int:
    """Solution 2023 / day 4 part 1."""
    lines = aoc.Loader(input_file).as_lines()
    cards = parse_cards(lines)

    total_points = 0
    for left, right in cards:
        winning_numbers = left.intersection(right)
        total_points += 2 ** (len(winning_numbers) - 1) if winning_numbers else 0

    return total_points


def part2(input_file: Path) -> int:
    """Solution 2023 / day 4 part 2."""
    lines = aoc.Loader(input_file).as_lines()
    cards = parse_cards(lines)

    total_cards = [1] * len(cards)  # took me a while to realize to just count the copies
    for ix, (left, right) in enumerate(cards):
        n_winning = len(left.intersection(right))
        for iy in range(n_winning):
            total_cards[ix + iy + 1] += total_cards[ix]

    return sum(total_cards)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 13
ANSWER_EXAMPLE_PART_2 = 30
ANSWER_INPUT_PART_1 = 21959
ANSWER_INPUT_PART_2 = 5_132_675

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
