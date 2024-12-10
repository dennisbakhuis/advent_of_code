"""Test cases for the overlap function."""

import pytest
from aoc.number import overlap


@pytest.mark.parametrize(
    "input_range,other_range,translate_range,expected_overlapping,expected_non_overlapping",
    [
        ((1, 5), (6, 10), None, set(), {(1, 5)}),  # No overlap
        ((1, 5), (5, 10), None, {(5, 5)}, {(1, 4)}),  # Overlap at boundary
        ((1, 5), (1, 5), None, {(1, 5)}, set()),  # Exact match
        ((1, 10), (3, 7), None, {(3, 7)}, {(1, 2), (8, 10)}),  # Middle overlap
        ((3, 7), (1, 10), None, {(3, 7)}, set()),  # Input fully within other
        ((1, 5), (2, 2), None, {(2, 2)}, {(1, 1), (3, 5)}),  # Single-point overlap
        ((1, 5), (2, 3), None, {(2, 3)}, {(1, 1), (4, 5)}),  # Partial overlap in middle
        ((1, 5), (1, 1), None, {(1, 1)}, {(2, 5)}),  # Overlap at start only
        ((1, 5), (5, 5), None, {(5, 5)}, {(1, 4)}),  # Overlap at end only
        ((5, 12), (8, 16), (18, 26), {(18, 22)}, {(5, 7)}),  # Translate overlap
    ],
)
def test_overlap(
    input_range, other_range, translate_range, expected_overlapping, expected_non_overlapping
):
    """Test overlap function."""
    overlapping, non_overlapping = overlap(input_range, other_range, translate_range)
    assert overlapping == expected_overlapping
    assert non_overlapping == expected_non_overlapping
