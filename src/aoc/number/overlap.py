"""Check if two ranges are overlapping."""


def overlap(
    input_range: tuple[int, int],
    other_range: tuple[int, int],
    translate_range: tuple[int, int] = None,
) -> tuple[set[tuple[int, int]], set[tuple[int, int]]]:
    """
    Identify overlapping and non-overlapping portions of an input range with another range.

    If `translate_range` is provided, the overlapping portion is translated accordingly.

    Parameters
    ----------
    input_range : tuple[int, int]
        The (start, end) range to check.
    other_range : tuple[int, int]
        The (start, end) range to compare against.
    translate_range : tuple[int, int], optional
        The (start, end) range to translate the overlapping portion into.

    Returns
    -------
    overlapping : set of tuple[int, int]
        Overlapping portion(s) of the input range (translated if `translate_range` is given).
    non_overlapping : set of tuple[int, int]
        Non-overlapping portion(s) of the input range.
    """
    in_start, in_end = input_range
    src_start, src_end = other_range

    overlap_start = max(in_start, src_start)
    overlap_end = min(in_end, src_end)

    if overlap_start > overlap_end:
        return set(), {input_range}

    non_overlapping = set()
    if overlap_start > in_start:
        non_overlapping.add((in_start, overlap_start - 1))
    if overlap_end < in_end:
        non_overlapping.add((overlap_end + 1, in_end))

    if translate_range:
        dst_start, dst_end = translate_range
        offset = overlap_start - src_start
        overlapping = {(dst_start + offset, dst_start + offset + (overlap_end - overlap_start))}
    else:
        overlapping = {(overlap_start, overlap_end)}

    return overlapping, non_overlapping
