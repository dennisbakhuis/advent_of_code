"""AoC 2024 - Day 2."""

from pathlib import Path
import aoc  # AoC helpers


YEAR = 2024
DAY = 2


def check_level_rules(levels: list[int], problem_dampener: bool = False) -> bool:
    """
    Check for level rules.

    Rules to check:
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.

    Parameters
    ----------
    levels : list[int]
        List of levels.

    Returns
    -------
    bool
        True if the levels follow the rules, False otherwise
    """
    if len(levels) < 2:
        return True

    n_levels_minus_1 = len(levels) - 1

    is_increasing = sum(levels[i] < levels[i + 1] for i in range(n_levels_minus_1))
    is_decreasing = sum(levels[i] > levels[i + 1] for i in range(n_levels_minus_1))
    is_within_values = sum(
        1 <= abs(levels[i] - levels[i + 1]) <= 3 for i in range(n_levels_minus_1)
    )

    if not (is_increasing == n_levels_minus_1 or is_decreasing == n_levels_minus_1):
        safe_without_damper = False
    else:
        safe_without_damper = is_within_values == n_levels_minus_1

    if not problem_dampener or safe_without_damper:
        return safe_without_damper

    # Problem dampener
    for i in range(n_levels_minus_1 + 1):
        new_levels = levels.copy()
        new_levels.pop(i)
        if check_level_rules(new_levels):
            return True

    return False


def part1(data_file: Path) -> int:
    """
    Calculate the safe reports.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    lines = aoc.Loader(data_file).as_lines()

    safe_reports = [check_level_rules(list(int(x) for x in line.split())) for line in lines]

    return sum(safe_reports)


def part2(data_file: Path) -> int:
    """
    Calculate the safe reports using the problem damper.

    Parameters
    ----------
    data_file : pathlib.Path
        Path to the file containing pairs of integers.
    """
    lines = aoc.Loader(data_file).as_lines()

    safe_reports = [
        check_level_rules(list(int(x) for x in line.split()), problem_dampener=True)
        for line in lines
    ]

    return sum(safe_reports)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 2
ANSWER_EXAMPLE_PART_2 = 4
ANSWER_INPUT_PART_1 = 670
ANSWER_INPUT_PART_2 = 700

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
