"""AoC 2023 - Day 5."""

from pathlib import Path


import aoc  # AoC helpers


YEAR = 2023
DAY = 5


def parse_seeds_and_mappings(input_file: Path) -> tuple[tuple[int], tuple[tuple[tuple[int]]]]:
    """Parse the seeds and mappings from the input file."""
    parts = aoc.Loader(input_file).as_multiple_parts_of_lines()

    seeds = tuple(int(value) for value in parts[0][0].split(":")[1].split())
    mappings = tuple(
        tuple(tuple(int(value) for value in line.split()) for line in part[1:])
        for part in parts[1:]
    )

    return seeds, mappings


def part1(input_file: Path) -> int:
    """Solution 2023 / day 5 part 1."""
    seeds, mappings = parse_seeds_and_mappings(input_file)

    location_numbers = []
    for seed in seeds:
        for mapping in mappings:
            value_to_set = int(seed)
            for destination_start, source_start, length in mapping:
                if source_start <= seed < source_start + length:
                    delta = seed - source_start
                    value_to_set = destination_start + delta
                    break
            seed = value_to_set

        location_numbers.append(seed)

    return min(location_numbers)


def part2(input_file: Path) -> int:
    """Solution 2023 / day 5 part 2."""
    seeds, mappings = parse_seeds_and_mappings(input_file)

    seed_ranges = set(
        (start, start + length - 1) for start, length in zip(seeds[0::2], seeds[1::2], strict=True)
    )

    map_ranges = tuple(
        tuple(
            (
                (destination_start, destination_start + length - 1),
                (source_start, source_start + length - 1),
            )
            for destination_start, source_start, length in mapping
        )
        for mapping in mappings
    )

    location_ranges = set()
    for seed_range in seed_ranges:
        current_ranges = {seed_range}
        for mapping in map_ranges:
            processed_ranges = set()

            for destination_range, source_range in mapping:
                non_overlapping = set()
                for current_range in current_ranges:
                    new_overlapping, new_non_overlapping = aoc.number.overlap(
                        input_range=current_range,
                        other_range=source_range,
                        translate_range=destination_range,
                    )
                    processed_ranges |= new_overlapping
                    non_overlapping |= new_non_overlapping
                current_ranges = non_overlapping
            current_ranges |= processed_ranges
        location_ranges |= current_ranges

    return min(start for start, _ in location_ranges)


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 35
ANSWER_EXAMPLE_PART_2 = 46
ANSWER_INPUT_PART_1 = 282277027
ANSWER_INPUT_PART_2 = 11554135

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
