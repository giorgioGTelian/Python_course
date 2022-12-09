# iterative
def factorial(x):
    result = 1
    if x > 0:
        for y in range(1, x +1):
            result *= y
        return result

#recursive
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x)

print(factorial(10))
