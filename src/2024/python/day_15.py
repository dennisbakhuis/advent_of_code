"""AoC 2024 - Day 15."""

from pathlib import Path

import aoc  # AoC helpers
from aoc.types import TextMap, Direction, Coordinate


YEAR = 2024
DAY = 15


def do_movement(
    warehouse_map: TextMap,
    location: Coordinate,
    move: Coordinate,
) -> Coordinate:
    """Switch tiles in warehouse map."""
    next_spot = (location[0] + move[0], location[1] + move[1])

    if not warehouse_map.within_bounds(next_spot):
        return location

    if warehouse_map.get(next_spot) == "#":
        return location

    if warehouse_map.get(next_spot) != ".":
        do_movement(warehouse_map, next_spot, move)

    if warehouse_map.get(next_spot) == "." and warehouse_map.get(location) in "@O":
        warehouse_map.switch_tiles([(location, next_spot)])
        location = next_spot

    return location


def part1(input_file: Path) -> int:
    """Solution 2024 / day 15 part 1."""
    warehouse_map_raw, movements_raw = aoc.Loader(input_file).as_multiple_parts_of_lines()
    warehouse_map = TextMap(warehouse_map_raw)
    robot_movements = "".join(movements_raw)

    robot = warehouse_map.find("@")
    for robot_movement in robot_movements:
        move = Direction.from_label(robot_movement)
        robot = do_movement(warehouse_map, robot, move.value)

    box_locations = warehouse_map.find_all("O")
    score = sum(100 * y + x for x, y in box_locations)

    return score


def reformat_map(warehouse_map_raw: list[str]) -> TextMap:
    """Reformat the warehouse map."""
    reformatted_map = [
        line.replace("O", "[]").replace("#", "##").replace(".", "..").replace("@", "@.")
        for line in warehouse_map_raw
    ]
    return TextMap(reformatted_map)


def get_move_list(
    box_id: int,
    direction: Direction,
    boxes: dict[int, tuple[Coordinate, Coordinate]],
    obstacles: set[Coordinate],
) -> list[tuple[int, tuple[Coordinate, Coordinate]]]:
    """List of boxes to move."""
    box = boxes[box_id]
    moved_box = tuple(direction.move(box[0])), tuple(direction.move(box[1]))

    if moved_box[0] in obstacles or moved_box[1] in obstacles:
        return []

    boxes_in_way = list(
        id
        for id, box in boxes.items()
        if (moved_box[0] in box or moved_box[1] in box) and id != box_id
    )

    boxes_to_move = []
    for box_in_way in boxes_in_way:
        next_moved_box = get_move_list(box_in_way, direction, boxes, obstacles)

        if not next_moved_box:
            return []

        boxes_to_move.extend(next_moved_box)

    boxes_to_move.append((box_id, moved_box))

    return boxes_to_move


def part2(input_file: Path) -> int:
    """
    Solution 2024 / day 15 part 2.

    This was very painful...
    """
    warehouse_map_raw, movements_raw = aoc.Loader(input_file).as_multiple_parts_of_lines()
    warehouse_map = reformat_map(warehouse_map_raw)
    robot_movements = "".join(movements_raw)

    robot: Coordinate = warehouse_map.find("@")
    obstacles: list[Coordinate] = warehouse_map.find_all("#")
    boxes: dict[int, tuple[Coordinate, Coordinate]] = {
        ix: tuple((box, (box[0] + 1, box[1]))) for ix, box in enumerate(warehouse_map.find_all("["))
    }

    for robot_movement in robot_movements:
        direction = Direction.from_label(robot_movement)
        next_position = direction.move(robot)

        if next_position in obstacles or not warehouse_map.within_bounds(next_position):
            continue

        box_in_way = next((box_id for box_id, box in boxes.items() if next_position in box), None)

        if box_in_way is not None:
            need_to_move = get_move_list(box_in_way, direction, boxes, obstacles)

            if need_to_move:
                for box_id, new_location in need_to_move:
                    boxes[box_id] = new_location
            else:
                continue

        robot = next_position

    score = sum(
        100 * min(box[0][1], box[1][1]) + min(box[0][0], box[1][0]) for box in boxes.values()
    )

    return score


# example_file_1: Path = aoc.DATA.example_files[(YEAR, DAY)][1]
example_file: Path = aoc.DATA.example_files[(YEAR, DAY)][2]
# example_file_3: Path = aoc.DATA.example_files[(YEAR, DAY)][3]
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = 10092
ANSWER_EXAMPLE_PART_2 = 9021
ANSWER_INPUT_PART_1 = 1475249
ANSWER_INPUT_PART_2 = 1509724


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
