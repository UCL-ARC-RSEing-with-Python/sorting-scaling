# Analysing Code Scaling with Input Size

In this exercise you will practice recording scaling information about code execution time with the size of the inputs to said code.

- Fork [the `sorting-scaling` repository](FIXME), and then clone yourself a local copy.
- Study the repository code and examine the `README.md` file so you understand what the code in the repository codes, and what the `scripts/runtime.py` file is meant to do.

Our objective is to determine the scaling relationship between the execution time ($t_{exe}$) of the three sorting algorithms and the size of the input array ($N$) that they are asked to sort.
We will do this by asking the algorithms to sort lists of increasing input size (number of elements) and timing how long each algorithm takes to do this.
You will need to complete the missing steps in `scripts/runtime.py` so that you can record this information.

## Write the Functionality for Recording Execution Times

1. First, complete the implementation of the `generate_input_data` function.
   Read the function's docstring to understand what it should be doing, and what it must return.
2. Next, implement the `record_execution_time` method.
   Remember that you should use a performance timer like `timeit.timeit` or `timeit.repeats` during your tests, and not a system-time recorder.

Once you have completed these steps, you should be able to run the script and see $t_{exe}$ being reported in your terminal.

> [!IMPORTANT]
> React with your favourite emoji to this issue once you're able to see the execution times being reported. 🎉

The script will error when it tries to create the plot, since we haven't implemented that yet... so let's do that next!

## Interpret the Outputs

1. Implement the `plot_scaling_results` figure.
   This function will receive the $t_{exe}$ values for each of the algorithms, and the input sizes $N$ that were used to collect them.
   It is up to you to produce a well-formatted plot using this information, plotting $t_{exe}$ (on the y-axis) against $N$ (on the x-axis).
2. Using the information from your plot, theorise about what the relationship between the execution time $t_{exe}$ and $N$ is for each of the algorithms.
   Is it a power-law (polynomial) relationship?
   Is it exponential?
   Can you format your plot in such a way as to help you back up your theory?
3. Based on your results, which of the sorting algorithms do you expect to be the best (in terms of minimising code run-time) for very large input sizes?
   What about for smaller input sizes?

> [!TIP]
> If you are struggling to figure out what the scaling on `merge_sort` is, consider plotting $\frac{t_{exe}}{\log N}$ against $N$ instead of just $t_{exe}$ against $N$.

Leave a comment on this issue containing your plot and your predictions about the scaling of the three sorting algorithms.
You might also want to explain how you came to the conclusions that you did.

## (Stretch) Control Variables

The `generate_input_data` function that we're using to create the arrays that need to be sorted currently shuffles the values `0:N` into a random order, and then this list is passed to each algorithm to sort.

1. Think about what this means for each of the algorithms.
   Could the original ordering of the input values have an impact on $t_{exe}$ for one (or more) of the sorting algorithms?
   Why / why not?
2. Write another function (or modify the existing function) so that instead of returning the values `0:N` in a random order, they are returned already sorted.
   Then, re-run your experiment from before and examine the scaling relationships.
   Has anything changed?
   Does this fit your expectations from part (1)?
3. Write another function (or modify the existing functions) so that instead of returning the values `0:N` in a random order, they are returned in *reverse* order (that is, from `N-1` through to `0`).
   Again, re-run your experiment from before using this form for the input data.
   What do you notice?
