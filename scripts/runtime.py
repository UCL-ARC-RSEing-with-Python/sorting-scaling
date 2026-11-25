import argparse
from collections.abc import Callable
from pathlib import Path
from typing import Literal

import matplotlib.pyplot as plt
import numpy as np

from sorting.bubble import bubble_sort
from sorting.insertion import insertion_sort
from sorting.merge import merge_sort


def generate_input_data(seed: int, array_size: int) -> np.ndarray:
    """Generate an array containing the integers `0:array_size` in a random order.

    The output array contains the integers from `0` to `array_size-1` (inclusive).
    The order of the elements is random, determined by the `seed` and a call to
    `np.random.Generator.shuffle`.
    """
    rng = np.random.Generator(np.random.PCG64(seed=seed))

    # Create the input data array here, shuffle it, and then return the shuffled
    # values.


def plot_scaling_results(
    execution_times: dict[Literal["bubble", "insertion", "merge"], np.ndarray],
    input_sizes: np.ndarray,
    *,
    save_to: Path | None = None,
) -> plt.Figure:
    """Plot sorting algorithm execution time scaling with array input size.

    Args:
        execution_times: dict[str, np.ndarray]
            Execution times for each of the sorting algorithms. Keys are
            'bubble', 'insertion', and 'merge' corresponding to the
            respective sorting methods.
        input_sizes: np.ndarray
            The number of elements in the array to sort. `input_sizes[i]`
            is the size of the input array that resulted in an execution
            time of `execution_times[method][i]`.
        save_to: Path | None, default None
            If provided, save the generated figure to the given file.

    Returns:
        plt.Figure:
            Figure object containing the plot.
    """
    fig = plt.figure()

    # Create your plot(s) in a manner that you see fit.
    # One axes for all 3 algorithms? Separate axes that share the x-values?
    # Up to you, just make sure it's readable!

    if save_to:
        fig.savefig(save_to)


def record_execution_time(
    method: Callable[[np.ndarray], np.ndarray], input_data: np.ndarray, *, repeats: int
) -> float:
    """Record the execution time of a sorting method.

    Record the execution time of the sorting method `method` when called on the
    `input_data`. This will be done `repeats` times, with the minimum recorded
    execution time being returned by this function.

    Args:
        method: Callable[[np.ndarray], np.ndarray]
            One of `bubble_sort`, `insertion_sort`, or `merge_sort`. The sorting
            algorithm that will be executed on the `input_data`.
        input_data: np.ndarray
            Input data to pass to the sorting method.
        repeats: int
            Number of repeats to run when recording execution time. Minimum
            execution time across all repeats is returned.

    Returns:
        float:
            Execution time of the sorting `method` on the `input_data`.
    """
    # Record the execution time for the method given, using the given number of repeats.
    # Return the result.
    #
    # Hint: the command
    # ```python
    # method(input_data)
    # ```
    # will run the sorting algorithm.


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="sorting-timing",
        description="Python script for timing the execution of sorting algorithms when the input array sizes are scaled.",
    )
    parser.add_argument(
        "seed",
        type=int,
        nargs="?",
        default=0,
        help="RNG seed to use when shuffling data arrays.",
    )
    parser.add_argument(
        "repeats",
        type=int,
        default=2,
        help="Number of repeats for each call to a sorting algorithm. "
        "Minimum execution time across all repeats is reported.",
    )
    parser.add_argument(
        "-s",
        "--save",
        type=Path,
        default=None,
        help="File to save generated scaling plots to.",
    )

    args = parser.parse_args()
    save_to = Path(args.save) if args.save is not None else None

    input_sizes = np.unique(
        np.logspace(0.0, 8.0, num=9 * 3, base=2.0, endpoint=True, dtype=int)
    )
    n_sizes = input_sizes.size

    execution_times = {
        "bubble": np.zeros_like(input_sizes, dtype=float),
        "insertion": np.zeros_like(input_sizes, dtype=float),
        "merge": np.zeros_like(input_sizes, dtype=float),
    }

    # Gather execution times whilst scaling input array sizes
    for i, array_size in enumerate(input_sizes):
        print(f"({i} / {n_sizes}) Array size: {array_size}")
        input_data = generate_input_data(seed=args.seed, array_size=array_size)

        for method_name, method in [
            ("bubble", bubble_sort),
            ("insertion", insertion_sort),
            ("merge", merge_sort),
        ]:
            print(f"\t{method_name}", end=", ", flush=True)
            execution_times[method_name][i] = record_execution_time(
                method, input_data, repeats=args.repeats
            )
        print("\n", end="", flush=True)

    # Plot (and optionally save) your results!
    plot = plot_scaling_results(execution_times, input_sizes, save_to=save_to)
    plot.show()
