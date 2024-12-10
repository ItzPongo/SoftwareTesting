import pytest
from ExampleSort_sixDifference import (
    bubbleSort,
    insertionSort,
    selectionSort,
    quickSort,
    mergeSort,
    heapSort,
)

# Helper function to check if an array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

# Test data
@pytest.fixture
def test_arrays():
    return [
        [5, 3, 8, 6, 2, 7, 4, 1],
        [10, 20, 30, 40, 50],
        [50, 40, 30, 20, 10],
        [1, 1, 1, 1, 1],
        [1],
        [],
    ]

# Parameterized test for all sorting algorithms
@pytest.mark.parametrize("sorting_function", [bubbleSort, insertionSort, selectionSort, quickSort, mergeSort, heapSort])
def test_sorting_algorithms(sorting_function, test_arrays):
    for arr in test_arrays:
        original = arr.copy()
        sorting_function(arr)  # Sort the array in-place
        assert is_sorted(arr), f"{sorting_function.__name__} failed on {original}"

# Specific edge case tests
def test_empty_array():
    arr = []
    bubbleSort(arr)
    assert arr == []

def test_single_element():
    arr = [42]
    mergeSort(arr)
    assert arr == [42]

def test_duplicates():
    arr = [4, 2, 2, 8, 5, 6, 2, 2]
    selectionSort(arr)
    assert is_sorted(arr)

def test_large_array():
    import random
    arr = [random.randint(1, 1000) for _ in range(1000)]
    quickSort(arr)
    assert is_sorted(arr)
