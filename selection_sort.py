def selection_sort(numbers):
    # Loop through the list of numbers
    for i in range(len(numbers) - 1):
        # Find the minimum element in the unsorted portion of the list
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted portion
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    
    # Return the sorted list
    return numbers
