from collections.abc import Callable

import numpy as np
import pytest

from sorting.bubble import bubble_sort


@pytest.mark.parametrize("algorithm", (bubble_sort,), ids=("bubble",))
@pytest.mark.parametrize(
    ("input", "expected_array"),
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
    input: np.ndarray,
    expected_array: np.ndarray,
) -> None:
    """Test the sorting algorithms actually produce the sorted array."""
    # Saves needing to write out np.array in all the params
    input = np.array(input)
    expected_array = np.array(expected_array)

    result = algorithm(expected_array)

    assert np.all(result == expected_array)
