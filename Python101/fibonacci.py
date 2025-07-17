# Fibonacci (iterative)
def fibonacci_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("num must be a positive number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# Fibonacci (recursive)
def fibonacci_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("num must be a positive number")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)
