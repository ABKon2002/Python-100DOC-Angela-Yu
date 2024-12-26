
def add(*args):
    """
    Returns the sum of all the arguments passed in.
    Args:
        *args: any number of positional arguments
    Returns:
        int: the sum of all the arguments
    """
    total = 0
    for num in args:    # The arguments given are packed into a tuple.
        total += num
    return total

# print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def calc(n, **kwargs):
    result = n
    for key, value in kwargs.items():
        if key == "add":
            result += value
        elif key == "subtract":
            result -= value
        elif key == "multiply":
            result *= value
        elif key == "divide":
            result /= value
    return result

print(calc(2, add = 3, multiply = 5, divide = 3))