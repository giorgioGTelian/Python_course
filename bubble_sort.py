def bubble_sort(numbers):
    # Set a flag to True to start the loop
    flag = True
    
    # Start the loop
    while flag:
        # Set the flag to False to prepare for the next loop
        flag = False
        
        # Loop through the list of numbers
        for i in range(len(numbers) - 1):
            # If the current number is greater than the next number,
            # swap them and set the flag to True to indicate that a swap occurred
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
                flag = True
    
    # Return the sorted list
    return numbers
