# Factorial (iterative)
def factorial_iterative(num: int) -> int:
    if num < 0:
        raise ValueError("num must be a positive number")
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


# Factorial (recursive)
def factorial_recursive(num: int) -> int:
    if num < 0:
        raise ValueError("num must be a positive number")
    # Base case: if num is 0 or 1, return 1
    if num == 0 or num == 1:
        return 1
    # Recursive case: num! = num * (num-1)!
    else:
        return num * factorial_recursive(num - 1)
