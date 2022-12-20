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
