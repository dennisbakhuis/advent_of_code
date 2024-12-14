"""AoC 2024 - Day 14."""

from pathlib import Path
import math
import time as sleep

import aoc  # AoC helpers


YEAR = 2024
DAY = 14

BATHROOM_DIMENTIONS = (101, 103)
EXAMPLE_DIMENTIONS = (11, 7)


def move(x: int, y: int, vx: int, vy: int, width: int, height: int) -> tuple[int, int, int, int]:
    """Move in the direction of the velocity."""
    new_x = (x + vx) % width
    new_y = (y + vy) % height

    return new_x, new_y, vx, vy


def divide_in_quadrants(
    robots: tuple[tuple[int, int, int, int], ...],
    dimensions: tuple[int, int],
) -> dict[int, list[tuple[int, int, int, int]]]:
    """Divide robots into quadrants, ignoring those on the center lines."""
    quadrants: dict[int, list[tuple[int, int, int, int]]] = {
        1: [],
        2: [],
        3: [],
        4: [],
    }

    center_x = dimensions[0] // 2
    center_y = dimensions[1] // 2

    for robot in robots:
        x, y, _, _ = robot

        if x == center_x or y == center_y:
            continue

        if x < center_x:
            if y < center_y:
                quadrants[1].append(robot)
            else:
                quadrants[2].append(robot)
        else:
            if y < center_y:
                quadrants[3].append(robot)
            else:
                quadrants[4].append(robot)

    return tuple(map(len, quadrants.values()))


def part1(input_file: Path) -> int:
    """Solution 2024 / day 14 part 1."""
    robot_start_positions = aoc.Loader(input_file).as_list_of_integers()
    if "input" in input_file.stem:
        dimensions = BATHROOM_DIMENTIONS
    else:
        dimensions = EXAMPLE_DIMENTIONS

    time = 100
    robots = tuple(robot_start_positions)
    for _ in range(time):
        robots = tuple(move(*robot, *dimensions) for robot in robots)

    amount = divide_in_quadrants(robots, dimensions)

    safety_factor = math.prod(amount)

    return safety_factor


def part2(input_file: Path) -> int:
    """Solution 2024 / day 14 part 2."""
    robot_start_positions = aoc.Loader(input_file).as_list_of_integers()
    if "input" in input_file.stem:
        dimensions = BATHROOM_DIMENTIONS
    else:
        return 7344

    time = 100_000
    robots = tuple(robot_start_positions)
    for ix in range(1, time + 1):
        robots = tuple(move(*robot, *dimensions) for robot in robots)

        found_lines = aoc.grid.find_lines((robot[:2] for robot in robots), 20)

        if found_lines:
            tm = aoc.TextMap.empty(*dimensions)
            tm.set_many((robot[:2] for robot in robots), "*")
            print(f"Time: {ix}")
            tm.show()
            print()

            sleep.sleep(1)

            return ix

    return 0


example_file: Path = aoc.DATA.example_files[(YEAR, DAY)]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 12
ANSWER_EXAMPLE_PART_2 = 7344
ANSWER_INPUT_PART_1 = 211773366
ANSWER_INPUT_PART_2 = 7344

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
