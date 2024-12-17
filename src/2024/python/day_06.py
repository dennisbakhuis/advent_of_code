"""AoC 2024 - Day 6."""

from pathlib import Path

import aoc  # AoC helpers
from aoc.types import Direction, Coordinate


YEAR = 2024
DAY = 6


def do_patrol(
    location: tuple[int, int, Direction],
    obstacles: set[Coordinate],
    width: int,
    height: int,
    new_obstacle: Coordinate | None = None,
) -> set[Coordinate] | None:
    """
    Compute the path until going out of bounds or looping.

    Parameters
    ----------
    location : tuple[int, int, aoc.grid.Direction]
        Starting position and direction.
    obstacles : set[Coordinate]
        Obstacle locations.
    width : int
        Map width.
    height : int
        Map height.
    new_obstacle : Coordinate or None, optional
        An extra obstacle to add, by default None.

    Returns
    -------
    set[Coordinate] or None
        Visited coordinates or None if loop detected.
    """
    obstacle_list = set(obstacles)
    if new_obstacle:
        obstacle_list.add(new_obstacle)

    x, y, direction = location
    locations = set()

    while not (x < 0 or x >= width or y < 0 or y >= height):
        if (x, y, direction) in locations:
            return None

        if (
            (direction == Direction.UP and (x, y - 1) in obstacle_list)
            or (direction == Direction.RIGHT and (x + 1, y) in obstacle_list)
            or (direction == Direction.DOWN and (x, y + 1) in obstacle_list)
            or (direction == Direction.LEFT and (x - 1, y) in obstacle_list)
        ):
            direction = direction.turn_right()
            continue

        locations.add((x, y, direction))
        x, y = direction.move(x, y)

    return set([p[:2] for p in locations])


def part1(file_path: Path) -> int:
    """
    Return the number of visited locations without adding new obstacles.

    Parameters
    ----------
    textmap : aoc.TextMap
        The map input.

    Returns
    -------
    int
        Number of visited locations.
    """
    textmap = aoc.Loader(file_path).as_textmap()

    (cx, cy) = textmap.find("^")
    locations = do_patrol(
        location=(cx, cy, Direction.UP),
        obstacles=set(textmap.find_all("#")),
        width=textmap.width,
        height=textmap.height,
    )
    return len(locations)


def part2(file_path: Path) -> int:
    """
    Return how many single added obstacles create a loop.

    Parameters
    ----------
    textmap : aoc.TextMap
        The map input.

    Returns
    -------
    int
        Count of obstacles causing a loop.
    """
    textmap = aoc.Loader(file_path).as_textmap()

    (cx, cy) = textmap.find("^")
    obstacles = set(textmap.find_all("#"))
    locations = do_patrol(
        location=(cx, cy, Direction.UP),
        obstacles=obstacles,
        width=textmap.width,
        height=textmap.height,
    )

    creates_a_loop = 0
    for location in locations:
        if location in obstacles or location == (cx, cy):
            continue
        if (
            do_patrol(
                location=(cx, cy, Direction.UP),
                obstacles=obstacles,
                width=textmap.width,
                height=textmap.height,
                new_obstacle=location,
            )
            is None
        ):
            creates_a_loop += 1

    return creates_a_loop


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 41
ANSWER_EXAMPLE_PART_2 = 6
ANSWER_INPUT_PART_1 = 5177
ANSWER_INPUT_PART_2 = 1686

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
