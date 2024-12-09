"""AoC 2023 - Day 2."""

from pathlib import Path

import aoc  # AoC helpers


def part1(input_file: Path) -> int:
    """Solution day 2 part 1."""
    pass
    return 0


def part2(input_file: Path) -> int:
    """Solution day 2 part 2."""
    pass
    return 0


example_textmap: Path = aoc.Loader(aoc.DATA.example_files[(2023, 2)]).as_textmap()  # type: ignore
input_textmap: Path = aoc.Loader(aoc.DATA.input_files[(2023, 2)]).as_textmap()  # type: ignore

example_file: Path = aoc.DATA.example_files[(2023, 2)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(2023, 2)]


# print(f"Solution (example) part 1: {part1(example_file)}")
# assert part1(example_file) == None

# print(f"Solution (input) part 1: {part1(input_file)}")
# assert part1(input_file) == 2447

# # --- Part Two ---

# print(f"Solution (example) part 2: {part2(example_file)}")
# assert part2(example_textmap.copy()) == None

# print(f"Solution (input) part 2: {part2(input_file)}")
# assert part2(input_file) == None
