"""AoC 2024 - Day 1."""
import aoc  # AoC helpers


def part1(lines: list[str]) -> int:
    """
    Compute the sum of distances between paired numbers in a data file.

    Each line in the file contains a pair of integers, separated by a space.
    The function sorts the first and second elements of each pair independently,
    computes the differences between corresponding elements, and returns their sum.

    Parameters
    ----------
    lines : list[str]

    Returns
    -------
    int
        The sum of distances between corresponding sorted pairs.
    """
    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)
    distance = (abs(y - x) for x, y in zip(sorted(left), sorted(right), strict=True))

    return sum(distance)


def part2(lines: list[str]) -> int:
    """
    Compute the sum of similarity scores of paired numbers in a data file.

    Parameters
    ----------
    lines : list[str]

    Returns
    -------
    int
        The sum of similarity scores of the numbers.
    """
    left, right = zip(*(map(int, line.split()) for line in lines), strict=True)

    right_list = list(right)

    similarity = (x * right_list.count(x) for x in left)

    return sum(similarity)


lines_example = aoc.Loader(aoc.DATA.example_files[(2024, 1)]).as_lines()
lines_input = aoc.Loader(aoc.DATA.input_files[(2024, 1)]).as_lines()

print(f"Solution part 1: {part1(lines_example)}")
print(f"Solution part 2: {part2(lines_example)}")

print(f"Solution part 1: {part1(lines_input)}")
print(f"Solution part 2: {part2(lines_input)}")
