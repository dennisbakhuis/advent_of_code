"""AoC 2024 - Day 6."""
import aoc  # AoC helpers


def do_patrol(
    location: tuple[int, int, aoc.Direction],
    obstacles: set[tuple[int, int]],
    width: int,
    height: int,
    new_obstacle: tuple[int, int] | None = None,
) -> set[tuple[int, int]] | None:
    """
    Compute the path until going out of bounds or looping.

    Parameters
    ----------
    location : tuple[int, int, aoc.Direction]
        Starting position and direction.
    obstacles : set[tuple[int, int]]
        Obstacle locations.
    width : int
        Map width.
    height : int
        Map height.
    new_obstacle : tuple[int, int] or None, optional
        An extra obstacle to add, by default None.

    Returns
    -------
    set[tuple[int, int]] or None
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
            (direction == aoc.Direction.UP and (x, y - 1) in obstacle_list)
            or (direction == aoc.Direction.RIGHT and (x + 1, y) in obstacle_list)
            or (direction == aoc.Direction.DOWN and (x, y + 1) in obstacle_list)
            or (direction == aoc.Direction.LEFT and (x - 1, y) in obstacle_list)
        ):
            direction = direction.turn_right()
            continue

        locations.add((x, y, direction))
        x, y = direction.move(x, y)

    return set([p[:2] for p in locations])


def part1(textmap: aoc.TextMap) -> int:
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
    (cx, cy) = textmap.find("^")
    locations = do_patrol(
        location=(cx, cy, aoc.Direction.UP),
        obstacles=set(textmap.find_all("#")),
        width=textmap.width,
        height=textmap.height,
    )
    return len(locations)


def part2(textmap: aoc.TextMap) -> int:
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
    (cx, cy) = textmap.find("^")
    obstacles = set(textmap.find_all("#"))
    locations = do_patrol(
        location=(cx, cy, aoc.Direction.UP),
        obstacles=obstacles,
        width=textmap.width,
        height=textmap.height,
    )

    creates_a_loop = 0
    for location in locations:
        if location in obstacles or location == (cx, cy):
            continue
        if do_patrol(
            location=(cx, cy, aoc.Direction.UP),
            obstacles=obstacles,
            width=textmap.width,
            height=textmap.height,
            new_obstacle=location,
        ) is None:
            creates_a_loop += 1

    return creates_a_loop


example_textmap = aoc.Loader(aoc.DATA.example_files[(2024, 6)]).as_textmap()
input_textmap = aoc.Loader(aoc.DATA.input_files[(2024, 6)]).as_textmap()

print(f"Solution (example) part 1: {part1(example_textmap.copy())}")
print(f"Solution (example) part 2: {part2(example_textmap.copy())}")

print(f"Solution (input) part 1: {part1(input_textmap.copy())}")
print(f"Solution (input) part 2: {part2(input_textmap.copy())}")
