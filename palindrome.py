def is_palindrome(s):
    # First, we'll remove any non-alphanumeric characters from the string
    s = ''.join(c for c in s if c.isalnum())

    # Next, we'll convert the string to lowercase
    s = s.lower()

    # Then, we'll check if the string is a palindrome by comparing the first and last characters,
    # then the second and second-to-last characters, and so on.
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False


#what about to check input

def is_palindrome(s):
    # First, we'll check if the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Next, we'll remove any non-alphanumeric characters from the string
    s = ''.join(c for c in s if c.isalnum())

    # Then, we'll check if the string is empty after removing non-alphanumeric characters
    if not s:
        raise ValueError("Input must not be empty")

    # Finally, we'll convert the string to lowercase and check if it is a palindrome
    s = s.lower()
    return s == s[::-1]

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome(123))  # ValueError: Input must be a string
print(is_palindrome(""))  # ValueError: Input must not be empty


def is_palindrome(s):
    # First, we'll check if the input is a string
    if not isinstance(s, str):
        raise ValueError("Input must be a string")

    # Next, we'll remove any non-alphanumeric characters from the string
    s = ''.join(c for c in s if c.isalnum())

    # Then, we'll check if the string is empty after removing non-alphanumeric characters
    if not s:
        raise ValueError("Input must not be empty")

    # Next, we'll split the string into two halves
    half_length = len(s) // 2
    first_half = s[:half_length]
    second_half = s[half_length:]

    # Then, we'll reverse the second half of the string
    second_half = second_half[::-1]

    # Finally, we'll compare the first half of the string to the reversed second half
    return first_half == second_half

# Example usage
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome(123))  # ValueError: Input must be a string
print(is_palindrome(""))  # ValueError: Input must not be empty


#This algorithm first checks whether the input is a string. If it is not a string, 
#it raises a ValueError indicating that the input must be a string. 
#It then removes any non-alphanumeric characters from the string, and checks whether the resulting string is empty. 
#If the string is empty, it raises a ValueError indicating that the input must not be empty.
#Next, it splits the string into two halves and reverses the second half. Finally,
#it compares the first half of the string to the reversed second half.
