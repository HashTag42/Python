# Fibonacci sequence:
def fibonacci_series(n: int) -> str:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    sequence = ""
    if n >= 1:
        sequence += "1"
        a = 1
    if n >= 2:
        sequence += ", 1"
        b = 1
    for i in range(3, n + 1):
        c = a + b
        sequence += ", " + str(c)
        a = b
        b = c
    return sequence


# Fibonacci Nth (iterative)
def fibonacci_nth_iterative(n: int) -> int:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    elif n <= 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


# Fibonacci Nth (recursive)
def fibonacci_nth_recursive(n: int) -> int:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    elif n <= 2:
        return 1
    else:
        return fibonacci_nth_recursive(n-1) + fibonacci_nth_recursive(n-2)
