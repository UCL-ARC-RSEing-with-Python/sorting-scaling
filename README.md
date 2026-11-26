# Sorting Scaling

This repository contains a small Python package that provides an implementation of three sorting algorithms:

- Bubble sort, <https://en.wikipedia.org/wiki/Bubble_sort>.
- Insertion sort, <https://en.wikipedia.org/wiki/Insertion_sort>.
- Merge sort, <https://en.wikipedia.org/wiki/Merge_sort>.

Each of these algorithms can be used to sort a `list` of numbers (or more generally, a container with elements that support comparison) into order.
All the algorithms take the `list` to sort as their input, and return a new list that contains the sorted values.

Whilst all the algorithms will all return the same answer, they do not operate in the same way and thus we will observe differences between the performance of each algorithm as we vary the inputs that we want to sort.

## Outline of Repository Code

- The package code can be found inside the `src` directory.
  The three sorting algorithms can be imported from the respectively-named files.
- The `scripts` directory contains the `runtime.py` script, which aims to measure the performance of the various sorting algorithms.
  You will be completing this script as part of the exercises.

> [!NOTE]
> The `runtime.py` script generates an array of list sizes for the algorithms to sort via `np.logspace`.
> The range that is provided typically results in the script taking around 5-10mins to complete, using 1 repeat for each input size.
> As such, when you are first starting to fill in the blanks in the script and just want to check if things are working, we recommend reducing the range of input sizes to something like
>
> ```python
> np.logspace(0.0, 4.0, num=6 * 2 - 1, base=2.0, endpoint=True, dtype=int)
> ```
>
> (swapping the `6.0` to `4.0`) to make the script run in a reasonable time.
> Once you are happy that the script is performing correctly, and with your plot formatting, you can then re-instate the full range of values for the input size and run the script again to get the complete output.

- The `tests` directory contains a few basic tests for the sorting algorithms to check that they are actually doing the right thing, _and_ to help flag if you accidentally change something about the methods themselves.
  You can run the tests using `pytest`.
