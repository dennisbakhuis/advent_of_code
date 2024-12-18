"""AoC 2024 - Day 9."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 9


def show_blocks(blocks: list[tuple[int | None, int]]) -> None:
    """Show the blocks as string, a debug tool."""
    full_list = [item for sublist in [[value] * size for value, size in blocks] for item in sublist]

    print("".join(str(x) if x is not None else "." for x in full_list))


def part1(input_file: Path) -> int:
    """Solution 2024 / day 10 part 1."""
    disk = aoc.Loader(input_file).as_string()

    # Create a list of partitions -> a simple string does not work
    # as file_ids can be more than one digit
    partitions = [
        (ix // 2 if ix % 2 == 0 else ".")
        for ix in range(len(disk))
        for _ in range(int(disk[ix]))  # repeat the value
    ]

    while partitions.count("."):
        first_period = partitions.index(".")
        value = partitions.pop()
        partitions[first_period] = value

        while partitions[-1] == ".":  # strip trailing free slots
            partitions.pop()

    checksum = sum(value * ix for ix, value in enumerate(partitions) if isinstance(value, int))

    return checksum


def part2(input_file: Path) -> int:
    """Solution 2024 / day 10 part 2."""
    disk = aoc.Loader(input_file).as_string()
    blocks = [(None if ix % 2 else ix // 2, int(character)) for ix, character in enumerate(disk)]

    # show_blocks(blocks)

    for ix in reversed(range(len(blocks))):
        for iy in range(ix):
            value_ix, size_ix = blocks[ix]
            value_iy, size_iy = blocks[iy]

            if value_ix is not None and value_iy is None and size_ix <= size_iy:
                blocks[ix] = (None, size_ix)
                blocks[iy] = (None, size_iy - size_ix)
                blocks.insert(iy, (value_ix, size_ix))

    flat_blocks = [
        repeated_value if repeated_value else 0
        for value, size in blocks
        for repeated_value in [value] * size
    ]

    return sum(ix * value for ix, value in enumerate(flat_blocks) if value)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 1928
ANSWER_EXAMPLE_PART_2 = 2858
ANSWER_INPUT_PART_1 = 6283170117911
ANSWER_INPUT_PART_2 = 6307653242596

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
