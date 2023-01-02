def heapify(numbers, n, i):
    # Initialize the largest element as the root
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Check if the left child is larger than the root
    if left < n and numbers[left] > numbers[largest]:
        largest = left
    
    # Check if the right child is larger than the largest element
    if right < n and numbers[right] > numbers[largest]:
        largest = right
    
    # If the largest element is not the root, swap it and heapify the sub-tree
    if largest != i:
        numbers[i], numbers[largest] = numbers[largest], numbers[i]
        heapify(numbers, n, largest)

def heap_sort(numbers):
    # Build the max heap
    for i in range(len(numbers) // 2 - 1, -1, -1):
        heapify(numbers, len(numbers), i)
    
    # Extract the elements from the heap one by one
    for i in range(len(numbers) - 1, 0, -1):
        numbers[0], numbers[i] = numbers[i], numbers[0]
        heapify(numbers, i, 0)
    
    # Return the sorted list
    return numbers
