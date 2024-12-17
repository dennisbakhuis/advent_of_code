"""AoC 2024 - Day 17."""

from pathlib import Path

import aoc  # AoC helpers


YEAR = 2024
DAY = 17


A, B, C = 0, 1, 2


def get_registers_and_instructions(input_file: Path) -> tuple[list[int], list[int]]:
    """Get registers and instructions from input file."""
    *numbers_raw, instructions = aoc.Loader(input_file).as_list_of_integers()
    registers = [value[0] for value in numbers_raw]
    instructions = list(instructions)

    return registers, instructions


def perform_instruction(instructions: list[int], registers: list[int]) -> str:
    """Perform instruction on registers."""
    output, current_instruction = [], 0
    n_instructions = len(instructions)

    while current_instruction < n_instructions:
        operand = instructions[current_instruction]
        literal = instructions[current_instruction + 1]
        combo = [0, 1, 2, 3, *registers][literal]

        match operand:
            case 0:  # adv
                registers[A] = int(registers[A] / 2**combo)
            case 1:  # bxl
                registers[B] = registers[B] ^ literal
            case 2:  # bst
                registers[B] = combo % 8
            case 3:  # jnz
                current_instruction = current_instruction if registers[A] == 0 else literal - 2
            case 4:  # bxc
                registers[B] = registers[B] ^ registers[C]
            case 5:  # out
                output.append(combo % 8)
            case 6:  # bdv
                registers[B] = int(registers[A] / 2**combo)
            case 7:  # cdv
                registers[C] = int(registers[A] / 2**combo)

        current_instruction += 2

    return output


def part1(input_file: Path) -> str:
    """Solution 2024 / day 17 part 1."""
    registers, instructions = get_registers_and_instructions(input_file)
    output = perform_instruction(instructions, registers)

    output_string = ",".join(map(str, output))

    return output_string


def reverse_engineer(
    register_a: int,
    instructions: list[int],
    index: int = 0,
) -> int | None:
    """Reverse engineers the instructions so that register_a generates the program itself."""
    if index == len(instructions):
        return register_a

    reversed_index = len(instructions) - index - 1

    for offset in range(8):
        candidate_register = register_a * 8 + offset
        output = perform_instruction(instructions, [candidate_register, 0, 0])

        if output and output[0] == instructions[reversed_index]:
            result = reverse_engineer(candidate_register, instructions, index + 1)
            if result is not None:
                return result

    return None


def part2(input_file: Path) -> int:
    """Solution 2024 / day 17 part 2."""
    _, instructions = get_registers_and_instructions(input_file)
    register_a = reverse_engineer(0, instructions)

    return register_a


example_file_1: Path = aoc.DATA.example_files[(YEAR, DAY)][1]  # type: ignore
example_file_2: Path = aoc.DATA.example_files[(YEAR, DAY)][2]  # type: ignore
input_file: Path = aoc.DATA.input_files[(YEAR, DAY)]

ANSWER_EXAMPLE_PART_1 = "4,6,3,5,6,3,5,2,1,0"
ANSWER_EXAMPLE_PART_2 = 117440
ANSWER_INPUT_PART_1 = "2,1,3,0,5,2,3,7,1"
ANSWER_INPUT_PART_2 = 107416732707226

if __name__ == "__main__":
    title_line = f"Solutions for day {DAY} of year {YEAR}."
    print(title_line + "\n" + "-" * len(title_line))

    # --- Part One ---

    print(f"Solution (example) part 1: {part1(example_file_1)}")
    assert part1(example_file_1) == ANSWER_EXAMPLE_PART_1

    print(f"Solution (input) part 1: {part1(input_file)}")
    assert part1(input_file) == ANSWER_INPUT_PART_1

    # # --- Part Two ---

    print(f"Solution (example) part 2: {part2(example_file_2)}")
    assert part2(example_file_2) == ANSWER_EXAMPLE_PART_2

    print(f"Solution (input) part 2: {part2(input_file)}")
    assert part2(input_file) == ANSWER_INPUT_PART_2

    print()
