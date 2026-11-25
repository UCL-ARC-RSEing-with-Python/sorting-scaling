import numpy as np


def merge_sort(array: np.ndarray) -> np.ndarray:
    """Sort the `array` input into numerical order via Merge Sort.

    [Merge sort](https://en.wikipedia.org/wiki/Merge_sort) sorts values
    in a recursive fashion. Given an array of values to sort, merge
    sort will:

    - If the array has only a single value, return the array as it is,
      since it is already sorted.
    - Otherwise, split the array in half and call merge sort on the two
      halves. This will sort the two halves, and then they can be
      combined into a single array by moving through both (sorted) halves
      from start to finish, and comparing the least values yet to be
      placed into the combined array.

    Merge sort is a 'divide and conquer' approach - we split the problem
    of sorting one array of `N` elements into sorting 2 arrays of `N/2`
    elements, which in turn becomes the problem of sorting 4 arrays of
    `N/4` elements into order, then 8 arrays of `N/8` elements, and so on
    until we have `N` arrays of `1 = N/N` elements. After having sorted
    the shorter arrays, we combine the answers in an efficient manner to
    produce the result.
    """
    # := is the Walrus operator. It's use here is equivalent to
    # ```python
    # K = len(array)
    # if K == 1:
    #   ...
    # ```
    if (K := len(array)) == 1:
        return array

    left = merge_sort(array[: K // 2])
    right = merge_sort(array[K // 2 :])
    # K might be odd, so we do actually need to compute the lengths of the
    # two 'halves' in case one is greater than the other.
    L = len(left)
    R = len(right)
    sorted_array = np.zeros_like(array)

    next_left_index = 0
    next_right_index = 0
    current_sorted_index = 0
    while next_left_index < L and next_right_index < R:
        least_left_value = left[next_left_index]
        least_right_value = right[next_right_index]

        # Determine whether the next element in the left or right array is to
        # be placed into the combined array next
        if least_left_value < least_right_value:
            sorted_array[current_sorted_index] = least_left_value
            next_left_index += 1
        else:
            sorted_array[current_sorted_index] = least_right_value
            next_right_index += 1
        current_sorted_index += 1

    # At this point, either all the values in the left array have been placed
    # into the combined array, OR all the values in the right array have been
    # placed into the combined array. However, this means that we still need
    # to place all the remaining values in the OTHER array into the combined
    # array.
    if next_left_index < L:
        sorted_array[current_sorted_index:] = left[next_left_index:]
    else:
        sorted_array[current_sorted_index:] = right[next_right_index:]

    return sorted_array
