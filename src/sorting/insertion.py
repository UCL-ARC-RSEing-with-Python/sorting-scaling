import numpy as np


def insertion_sort(array: np.ndarray) -> np.ndarray:
    """Sort the `array` input into numerical order via Insertion Sort.

    [Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort) sorts
    values by working from the start of the array, taking the next
    'unsorted' entry it has yet to examine and inserting it into the
    correct position in the 'sorted' entries at the start. This means
    that, at iteration `K`, the first `K+1` entries in the list are
    sorted into the correct order, and the remaining elements are the
    'unsorted' elements. Note that the sorted elements are only sorted
    relative to each other - the 'unsorted' elements will be inserted
    between two already 'sorted' elements in the next iteration.

    The algorithm always requires `N` iterations to sort an array of
    `N` elements. There are no early termination conditions since the
    algorithm considers each element one-at-a-time.
    """
    sorted_array = array.copy()

    # Note that a 1-element array is already sorted, so the 'unsorted'
    # elements start at the 2nd element = 1-indexed value in Python
    unsorted_start = 1
    while unsorted_start < len(sorted_array):
        value_to_insert = array[unsorted_start]
        insert_at = unsorted_start

        # Work backwards through the 'sorted' elements, to find the
        # position to insert the new value. Each time we move backwards,
        # we need to move the entry that we displaced up one index in
        # the sorted block (since the element we are inserting comes
        # before it)
        while insert_at > 0 and array[insert_at - 1] > value_to_insert:
            array[insert_at] = array[insert_at - 1]
            insert_at -= 1

        # We have now reached the index at which the new value should
        # be placed.
        array[insert_at] = value_to_insert
        unsorted_start += 1

    return sorted_array
