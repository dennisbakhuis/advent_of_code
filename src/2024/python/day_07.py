"""AoC 2024 - Day 7."""
from pathlib import Path
import operator
from itertools import product
from typing import Callable

import aoc  # AoC helpers


def calculate_product_of_operators(values: list[int], operators: list[Callable]) -> list[int]:
    """
    Calculate all possible results by applying combinations of operators between a list of values.

    Parameters
    ----------
    values : list[int]
        A list of integer values to be operated upon.
    operators : list[Callable]
        A list of callable operators (e.g., functions like `operator.add`,
        `operator.sub`) to apply between the values.

    Returns
    -------
    list[int]
        A list of results obtained by applying all combinations of the
        operators between the values. If an operation results in a
        division by zero, that combination is skipped.
    """
    operator_combinations = product(operators, repeat=len(values) - 1)
    answers = []
    for combination in operator_combinations:
        result = values[0]
        for i, op in enumerate(combination):
            try:
                result = op(result, values[i + 1])
            except ZeroDivisionError:
                result = None
                break
        if result is not None:
            answers.append(result)

    return answers


def part1(data_file: Path) -> int:
    """Find missing operators."""
    lines = aoc.Loader(data_file).as_lines()
    equations = {
        int(line.split(":")[0]): [int(x) for x in line.split(":")[1].split()]
        for line in lines
    }

    operators = (operator.add, operator.mul)

    sum_of_results_has_solution = 0
    for solution, values in equations.items():
        answers = calculate_product_of_operators(values, operators)

        if solution in answers:
            sum_of_results_has_solution += solution

    return sum_of_results_has_solution


def concatenate(a: int, b: int) -> int:
    """Concatenate two integers."""
    return int(str(a) + str(b))


def part2(data_file: Path) -> int:
    """Find missing operators including concatenate."""
    lines = aoc.Loader(data_file).as_lines()
    equations = {
        int(line.split(":")[0]): [int(x) for x in line.split(":")[1].split()]
        for line in lines
    }

    operators = (operator.add, operator.mul, concatenate)

    sum_of_results_has_solution = 0
    for solution, values in equations.items():
        answers = calculate_product_of_operators(values, operators)

        if solution in answers:
            sum_of_results_has_solution += solution

    return sum_of_results_has_solution


example_file = aoc.DATA.example_files[(2024, 7)]
input_file = aoc.DATA.input_files[(2024, 7)]

print(f"Solution (example) part 1: {part1(example_file)}")
print(f"Solution (example) part 2: {part2(example_file)}")

print(f"Solution (input) part 1: {part1(input_file)}")
print(f"Solution (input) part 2: {part2(input_file)}")
