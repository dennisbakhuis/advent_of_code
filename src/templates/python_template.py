"""AoC "'YEAR'" - Day "'DAY'"."""
from pathlib import Path

import aoc  # AoC helpers


def part1(input_file: Path) -> int:
    """Solution day "'DAY'" part 1."""
    pass
    return 0


def part2(input_file: Path) -> int:
    """Solution day "'DAY'" part 2."""
    pass
    return 0


example_textmap = aoc.Loader(aoc.DATA.example_files[("'YEAR'", "'DAY'")]).as_textmap()
input_textmap = aoc.Loader(aoc.DATA.input_files[("'YEAR'", "'DAY'")]).as_textmap()

example_file = aoc.DATA.example_files[("'YEAR'", "'DAY'")]
# example_file_1 = aoc.DATA.example_files[("'YEAR'", "'DAY'")][1]
# example_file_2 = aoc.DATA.example_files[("'YEAR'", "'DAY'")][2]
input_file = aoc.DATA.input_files[("'YEAR'", "'DAY'")]


print(f"Solution (example) part 1: {part1(example_file)}")
# print(f"Solution (example) part 1: {part1(example_file_1)}")
# assert part1(example_file) == None

# print(f"Solution (input) part 1: {part1(input_file)}")
# assert part1(input_file) == None

# --- Part Two ---

# print(f"Solution (example) part 2: {part2(example_file)}")
# assert part2(example_textmap.copy()) == None

# print(f"Solution (input) part 2: {part2(input_file)}")
# assert part2(input_file) == None
