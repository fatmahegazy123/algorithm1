def max_heapify(array, size, root_index):
    """
    Adjusts the heap to maintain the Max Heap property for the subtree rooted at root_index.
    """
    largest = root_index  # Assume root is largest
    left_child = 2 * root_index + 1  # Left child index
    right_child = 2 * root_index + 2  # Right child index

    # Check if left child exists and is greater than root
    if left_child < size and array[left_child] > array[largest]:
        largest = left_child

    # Check if right child exists and is greater than current largest
    if right_child < size and array[right_child] > array[largest]:
        largest = right_child

    # If largest is not root
    if largest != root_index:
        array[root_index], array[largest] = array[largest], array[root_index]  # Swap
        max_heapify(array, size, largest)  # Recursively heapify the affected subtree


def heapsort(array):
    """
    Sorts an array using the Heap Sort algorithm.
    """
    n = len(array)

    # Step 1: Build a Max Heap
    for i in range(n // 2 - 1, -1, -1):  # Start from the last non-leaf node
        max_heapify(array, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]  # Swap current root with the end
        max_heapify(array, i, 0)  # Heapify the reduced heap


if __name__ == "__main__":
    # Test case 1: Small array
    test_case1 = [4, 10, 3, 5, 1]
    print("Original Array:", test_case1)
    heapsort(test_case1)
    print("Sorted Array:", test_case1)

    # Test case 2: Larger array
    test_case2 = [19, 1, 10, 14, 16, 4, 7, 9, 3, 2, 8]
    print("\nOriginal Array:", test_case2)
    heapsort(test_case2)
    print("Sorted Array:", test_case2)

    # Test case 3: Already sorted array
    test_case3 = [1, 2, 3, 4, 5, 6, 7, 8]
    print("\nOriginal Array:", test_case3)
    heapsort(test_case3)
    print("Sorted Array:", test_case3)

    # Test case 4: Reverse sorted array
    test_case4 = [8, 7, 6, 5, 4, 3, 2, 1]
    print("\nOriginal Array:", test_case4)
    heapsort(test_case4)
    print("Sorted Array:", test_case4)