"""AoC 2023 - Day 1."""
from pathlib import Path

import aoc  # AoC helpers


DIGIT_VALUES = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_digit(
    line: str,
    backwards: bool = False,
    use_words: bool = False,
) -> str:
    """Get the first digit."""
    line_to_use = line[::-1] if backwards else line

    buffer = "....."
    for character in line_to_use:
        buffer += character

        if character.isdigit():
            return character

        if use_words and not backwards:
            if any(word in buffer for word in DIGIT_VALUES):
                for name, digit in DIGIT_VALUES.items():
                    if name in buffer:
                        return digit
        elif use_words:
            if any(word[::-1] in buffer for word in DIGIT_VALUES):
                for name, digit in DIGIT_VALUES.items():
                    if name[::-1] in buffer:
                        return digit



def part1(input_file: Path, use_words: bool=False) -> int:
    """Solution day 1 part 1."""
    lines = aoc.Loader(input_file).as_lines()

    digits = [
        int(
            get_first_digit(line, use_words=use_words)
            + get_first_digit(line, backwards=True, use_words=use_words)
        ) for line in lines
    ]

    return sum(digits)


def part2(input_file: Path) -> int:
    """Solution day 1 part 2."""
    return part1(input_file, use_words=True)


example_file_1 = aoc.DATA.example_files[(2023, 1)][1]
example_file_2 = aoc.DATA.example_files[(2023, 1)][2]
input_file = aoc.DATA.input_files[(2023, 1)]


print(f"Solution (example) part 1: {part1(example_file_1)}")
assert part1(example_file_1) == 142

print(f"Solution (input) part 1: {part1(input_file)}")
assert part1(input_file) == 54634

# --- Part Two ---

print(f"Solution (example) part 2: {part2(example_file_2)}")
assert part2(example_file_2) == 281
print(f"Solution (input) part 2: {part2(input_file)}")

assert part2(input_file) == 53855
