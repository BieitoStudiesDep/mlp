import numpy as np


def isArray(arr: np.ndarray) -> bool:
    """Check if the input is a NumPy array."""
    return isinstance(arr, np.ndarray)


def isArrayThrow(arr: np.ndarray):
    """Check if the input is a NumPy array, if not, raise ValueError."""
    if not isinstance(arr, np.ndarray):
        raise ValueError("arr is not a NumPy array")


def arrayGetFirstValue(arr: np.ndarray):
    """Get the first value of the NumPy array."""
    return arr.flat[0]


def arrayCompare(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """Compare two NumPy arrays and return the comparison result."""
    return np.equal(arr1, arr2)


def arrayEqu(arr1: np.ndarray, arr2: np.ndarray) -> dict:
    """
    Compare two NumPy arrays element-wise and return a dictionary containing:
    1. A NumPy array of boolean values indicating equality.
    2. A boolean value indicating if all elements are equal.
    3. A boolean value indicating if any element is equal.
    """
    arr_bool = arr1 == arr2
    all_values_equal = np.all(arr_bool)
    any_value_equal = np.any(arr_bool)
    return {
        "arr_bool": arr_bool,
        "all_values_equal": all_values_equal,
        "any_value_equal": any_value_equal,
    }
