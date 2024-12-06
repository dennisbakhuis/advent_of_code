"""AoC 2015 - Day 1."""
from helpers import Loader, DATA


data = Loader(DATA.input_files[(2015,1)]).as_string()


def part1(data) -> int:
    """Count the number of floors Santa has to go up or down."""
    return data.count("(") - data.count(")")


def part2(data) -> int:
    """Find the position of the first character that causes Santa to enter the basement."""
    for ix in range(len(data)):
        if data[:ix].count("(") - data[:ix].count(")") == -1:
            return ix


print(f"Solution day1-part 1: {part1(data)}")
print(f"Solution day1-part 2: {part2(data)}")
