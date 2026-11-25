from dataclasses import dataclass

import numpy as np


@dataclass(kw_only=True)
class SortResult:
    """Small container class to preserve sorting information.

    Attributes:
        iterations: int
            The number of iterations that the algorithm performed.
        sorted_array: np.ndarray
            The sorted array returned from an algorithm.
    """

    iterations: int
    sorted_array: np.ndarray

    @property
    def n_elements(self) -> int:
        """Number of elements in the sorted array."""
        return self.sorted_array.size
