"""AoC 2024 - Day 1."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 1


def part1(file_path: Path) -> int:
    """
    Compute the sum of distances between paired numbers in a data file.

    Each line in the file contains a pair of integers, separated by a space.
    The function sorts the first and second elements of each pair independently,
    computes the differences between corresponding elements, and returns their sum.

    Parameters
    ----------
    lines : list[str]

    Returns
    -------
    int
        The sum of distances between corresponding sorted pairs.
    """
    lines = aoc.Loader(file_path).as_lines()

    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)
    distance = (abs(y - x) for x, y in zip(sorted(left), sorted(right), strict=True))

    return sum(distance)


def part2(file_path: Path) -> int:
    """
    Compute the sum of similarity scores of paired numbers in a data file.

    Parameters
    ----------
    lines : list[str]

    Returns
    -------
    int
        The sum of similarity scores of the numbers.
    """
    lines = aoc.Loader(file_path).as_lines()

    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)

    right_list = list(right)

    similarity = (x * right_list.count(x) for x in left)

    return sum(similarity)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 11
ANSWER_EXAMPLE_PART_2 = 31
ANSWER_INPUT_PART_1 = 2904518
ANSWER_INPUT_PART_2 = 18650129

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file)}")
    # assert part1(example_file) == ANSWER_EXAMPLE_PART_1

    print(f"Solution (input) part 1: {part1(input_file)}")
    # assert part1(input_file) == ANSWER_INPUT_PART_1

    # --- Part Two ---

    print(f"Solution (example) part 2: {part2(example_file)}")
    # assert part2(example_file) == ANSWER_EXAMPLE_PART_2

    print(f"Solution (input) part 2: {part2(input_file)}")
    # assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
