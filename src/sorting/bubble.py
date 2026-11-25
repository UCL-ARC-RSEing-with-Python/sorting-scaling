import numpy as np


def bubble_sort(array: np.ndarray) -> np.ndarray:
    """Sort the `array` input into numerical order via Bubble Sort.

    [Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort) sorts values
    into order by scanning through the list, and swapping un-ordered pairs
    into the correct order. After the first iteration ("or pass") the
    greatest value is guaranteed to be at the end of the array, after the
    2nd pass the greatest two values at the end of the array, etc.

    In the worst cast, the algorithm will need to make `N` passes to
    guarantee that an array of `N` elements is sorted. The algorithm can
    stop at an earlier pass if it does not make any "swaps" during that pass
    (which implies the array is already sorted).
    """
    sorted_array = array.copy()

    for pass_number in range(sorted_array.size):
        swaps_performed = False

        for i in range(sorted_array.size - (pass_number + 1)):
            if sorted_array[i] > sorted_array[i + 1]:
                to_swap = sorted_array[i]
                sorted_array[i] = sorted_array[i + 1]
                sorted_array[i + 1] = to_swap
                swaps_performed = True

        # If we didn't make any swaps this pass, everything must be in order
        if not swaps_performed:
            break

    return sorted_array
