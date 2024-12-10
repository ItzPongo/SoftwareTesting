import random
import time
from ExampleSort_sixDifference import bubbleSort, insertionSort, selectionSort, quickSort, mergeSort, heapSort

def test_sorting_algorithm(algorithm):
    """
    This function generates a random array of integers with a random size 
    and tests the provided sorting algorithm by measuring its execution time 
    and verifying its correctness.
    """
    # Generate a random size for the array between 50 and 500
    n = random.randint(50, 500)
    
    # Generate a random array of size n
    arr = [random.randint(1, 500) for _ in range(n)]
    
    # Print the unsorted array and its size
    print(f"Testing {algorithm.__name__} with array of size {n}: {arr}")
    
    # Copy the original array for correctness checking
    arr_copy = arr.copy()
    
    # Sort the array using the provided algorithm
    start_time = time.time()
    algorithm(arr)
    elapsed_time = time.time() - start_time
    
    # Print the sorted array and the time taken
    print(f"Sorted array: {arr}")
    print(f"{algorithm.__name__} finished in {elapsed_time:.3f} seconds")
    
    # Verify the correctness by comparing to the Python built-in sorted() function
    if arr == sorted(arr_copy):
        print(f"{algorithm.__name__} is correct!")
    else:
        print(f"{algorithm.__name__} is incorrect!")
    
    print("\n")


test_sorting_algorithm(bubbleSort)
test_sorting_algorithm(insertionSort)
test_sorting_algorithm(selectionSort)
test_sorting_algorithm(quickSort)
test_sorting_algorithm(mergeSort)
test_sorting_algorithm(heapSort)


