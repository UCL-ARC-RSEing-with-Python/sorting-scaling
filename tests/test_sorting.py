from collections.abc import Callable

import pytest

from sorting.bubble import bubble_sort
from sorting.insertion import insertion_sort
from sorting.merge import merge_sort


@pytest.mark.parametrize(
    "algorithm",
    (bubble_sort, insertion_sort, merge_sort),
    ids=("bubble", "insertion", "merge"),
)
@pytest.mark.parametrize(
    ("input_values", "expected_array"),
    [
        pytest.param([0, 1, 2, 3, 4], [0, 1, 2, 3, 4], id="Already sorted"),
        pytest.param([4, 3, 2, 1, 0], [0, 1, 2, 3, 4], id="Anti-sorted"),
        pytest.param([1.0, 8.0, 4.0, 2.5], [1.0, 2.5, 4.0, 8.0], id="Float sort"),
        pytest.param([2, 3, 1, 4, 0], [0, 1, 2, 3, 4], id="Smallest starts at end"),
        pytest.param(
            [1, 5, 0, 2, 3, 6, 4], [0, 1, 2, 3, 4, 5, 6], id="Ordered groups of 2"
        ),
        pytest.param(
            [1, 3, 6, 0, 2, 5, 4], [0, 1, 2, 3, 4, 5, 6], id="Ordered groups of 3"
        ),
    ],
)
def test_sorting_algorithms(
    algorithm: Callable,
    input_values: list,
    expected_array: list,
) -> None:
    """Test the sorting algorithms actually produce the sorted array."""
    to_sort = list(input_values)
    expected_array = list(expected_array)

    result = algorithm(to_sort)

    assert result == expected_array
    assert to_sort == input_values, "In-place changes have occurred!"
