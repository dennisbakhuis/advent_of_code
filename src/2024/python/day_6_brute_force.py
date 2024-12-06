"""AoC 2015 - Day 6."""
from enum import Enum

from aoc import Loader, DATA, coordinates_to_index, index_to_coordinates


data = Loader(DATA.input_files[(2024,6)]).as_lines()
# data = Loader(DATA.example_files[(2024,6)]).as_lines()


class Direction(int, Enum):
    """Enum for directions."""

    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


def part1(data) -> int:
    """Count the number of floors Santa has to go up or down."""
    plan = "\n".join(data)

    n_rows, n_columns = len(data), len(data[0]) + 1  # newline character

    current_direction = Direction.UP
    index = plan.index("^")
    (cy, cx) = index_to_coordinates(
        index=index,
        row_length=n_columns,
    )

    while True:
        plan = plan[:index] + "X" + plan[index + 1:]

        if current_direction == Direction.UP:
            cy -= 1
        elif current_direction == Direction.DOWN:
            cy += 1
        elif current_direction == Direction.LEFT:
            cx -= 1
        elif current_direction == Direction.RIGHT:
            cx += 1

        if (
            cy < 0
            or cy >= n_rows
            or cx < 0
            or cx >= n_columns
        ):
            break

        index = coordinates_to_index(
            cx=cx,
            cy=cy,
            row_length=n_columns,
        )

        if plan[index] == "#":
            if current_direction == Direction.UP:
                cy += 1
                current_direction = Direction.RIGHT
            elif current_direction == Direction.DOWN:
                cy -= 1
                current_direction = Direction.LEFT
            elif current_direction == Direction.LEFT:
                cx += 1
                current_direction = Direction.UP
            elif current_direction == Direction.RIGHT:
                cx -= 1
                current_direction = Direction.DOWN

        index = coordinates_to_index(
            cx=cx,
            cy=cy,
            row_length=n_columns,
        )

    n_squares = plan.count("X")

    return n_squares, plan


def is_in_loop(plan: str, n_rows: int, n_columns: int) -> bool:
    """Check if the plan is in a loop."""
    current_direction = Direction.UP
    index = plan.index("^")
    (cy, cx) = index_to_coordinates(
        index=index,
        row_length=n_columns,
    )

    visited = set((cy, cx, current_direction))

    while True:
        if current_direction == Direction.UP:
            cy -= 1
        elif current_direction == Direction.DOWN:
            cy += 1
        elif current_direction == Direction.LEFT:
            cx -= 1
        elif current_direction == Direction.RIGHT:
            cx += 1

        if (
            cy < 0
            or cy >= n_rows
            or cx < 0
            or cx >= n_columns
        ):
            break

        if (cy, cx, current_direction) in visited:
            return True

        visited.add((cy, cx, current_direction))

        index = coordinates_to_index(
            cx=cx,
            cy=cy,
            row_length=n_columns,
        )

        if plan[index] == "#":
            if current_direction == Direction.UP:
                cy += 1
                current_direction = Direction.RIGHT
            elif current_direction == Direction.DOWN:
                cy -= 1
                current_direction = Direction.LEFT
            elif current_direction == Direction.LEFT:
                cx += 1
                current_direction = Direction.UP
            elif current_direction == Direction.RIGHT:
                cx -= 1
                current_direction = Direction.DOWN

            index = coordinates_to_index(
                cx=cx,
                cy=cy,
                row_length=n_columns,
            )

            continue


def part2(data, old_plan) -> int:
    """Count the number of floors Santa has to go up or down."""
    plan = "\n".join(data)
    n_rows, n_columns = len(data), len(data[0]) + 1  # newline character
    n_loops = 0

    indices_on_route = [
        ix
        for ix, char in enumerate(old_plan)
        if char == "X"
    ]

    n_indices = len(indices_on_route)

    for ix, index in enumerate(indices_on_route):
        char = plan[index]
        if char in "^\n#":
            continue

        test_plan = plan[:index] + "#" + plan[index + 1:]

        if is_in_loop(test_plan, n_rows, n_columns):
            print(f"Loop found at {index} -- {ix / n_indices * 100:.2f}%")
            n_loops += 1

    return n_loops


n_squares, plan = part1(data)
print(f"Solution day1-part 1: {n_squares}")
print(f"Solution day1-part 2: {part2(data, old_plan=plan)}")
