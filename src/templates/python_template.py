"""AoC "'YEAR'" - Day "'DAY'"."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = "'YEAR'"
DAY = "'DAY'"


def part1(input_file: Path) -> int:
    """Solution "'YEAR'" / day "'DAY'" part 1."""
    pass
    return 0


def part2(input_file: Path) -> int:
    """Solution "'YEAR'" / day "'DAY'" part 2."""
    pass
    return 0


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
# example_file_1: Path = aoc.DATA.example_files[(YEAR, DAY)][1]
# example_file_2: Path = aoc.DATA.example_files[(YEAR, DAY)][2]
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = None
ANSWER_EXAMPLE_PART_2 = None
ANSWER_INPUT_PART_1 = None
ANSWER_INPUT_PART_2 = None

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file)}")
    # assert part1(example_file) == ANSWER_EXAMPLE_PART_1

    # print(f"Solution (input) part 1: {part1(input_file)}")
    # assert part1(input_file) == ANSWER_INPUT_PART_1

    # # --- Part Two ---

    # print(f"Solution (example) part 2: {part2(example_file)}")
    # assert part2(example_file) == ANSWER_EXAMPLE_PART_2

    # print(f"Solution (input) part 2: {part2(input_file)}")
    # assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
