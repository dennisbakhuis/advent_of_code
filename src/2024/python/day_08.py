"""AoC 2024 - Day 8."""
from itertools import combinations

import aoc  # AoC helpers


def part1(textmap: aoc.TextMap) -> int:
    """Soluiton day 9 part 1."""
    antenna_types = set(textmap.as_string())
    antenna_types.remove(".")

    antennas = {
        antenna_type: textmap.find_all(antenna_type)
        for antenna_type in antenna_types
    }

    antinodes = set()
    for _, locations in antennas.items():
        for node1, node2 in combinations(locations, 2):
            dx, dy = (node2[0] - node1[0], node2[1] - node1[1])

            antinodes.update([
                (node1[0] + ix * dx, node1[1] + ix * dy)
                for ix in (-1, 2)
                if textmap.within_bounds(node1[0] + ix * dx, node1[1] + ix * dy)
            ])

    return len(antinodes)


def part2(textmap: aoc.TextMap) -> int:
    """Soluiton day 9 part 1."""
    antenna_types = set(textmap.as_string())
    antenna_types.remove(".")

    max_width = max(textmap.width, textmap.height)

    antennas = {
        antenna_type: textmap.find_all(antenna_type)
        for antenna_type in antenna_types
    }

    antinodes = set()
    for _, locations in antennas.items():
        for node1, node2 in combinations(locations, 2):
            dx, dy = (node2[0] - node1[0], node2[1] - node1[1])

            antinodes.update([
                (node1[0] + ix * dx, node1[1] + ix * dy)
                for ix in range(-max_width, max_width)
                if textmap.within_bounds(node1[0] + ix * dx, node1[1] + ix * dy)
            ])

    return len(antinodes)


example_textmap = aoc.Loader(aoc.DATA.example_files[(2024, 8)]).as_textmap()
input_textmap = aoc.Loader(aoc.DATA.input_files[(2024, 8)]).as_textmap()

print(f"Solution (example) part 1: {part1(example_textmap.copy())}")
assert part1(example_textmap.copy()) == 14
print(f"Solution (input) part 1: {part1(input_textmap.copy())}")
assert part1(input_textmap.copy()) == 249

print(f"Solution (example) part 2: {part2(example_textmap.copy())}")
assert part2(example_textmap.copy()) == 34
print(f"Solution (input) part 2: {part2(input_textmap.copy())}")
assert part2(input_textmap.copy()) == 905
