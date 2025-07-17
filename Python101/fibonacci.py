# Fibonacci (iterative)
def fibonacci_iterative(num: int) -> int:
    if num < 0:
        raise ValueError("num must be a positive number")
    if num == 0:
        return 0
    elif num == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, num + 1):
        a, b = b, a + b
    return b


# Fibonacci (recursive)
def fibonacci_recursive(num: int) -> int:
    if num < 0:
        raise ValueError("num must be a positive number")
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num-1) + fibonacci_recursive(num-2)
