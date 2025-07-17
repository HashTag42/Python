# Factorial (iterative)
def factorial_iterative(n: int) -> int:
    if n < 0:
        raise ValueError("num must be a positive number")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


# Factorial (recursive)
def factorial_recursive(n: int) -> int:
    if n < 0:
        raise ValueError("num must be a positive number")
    # Base case: if num is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: num! = num * (num-1)!
    else:
        return n * factorial_recursive(n - 1)
