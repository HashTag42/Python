'''
The Fibonacci numbers, commonly denoted 'F(n)', form a sequence called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1.
That is,
    F(0) = 0, F(1) = 1
    F(n) = F(n - 1) + F(n - 2), for n > 1.
The first 10 Fibonacci numbers, from F(0) to F(9), are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
Learn more at <https://en.wikipedia.org/wiki/Fibonacci_sequence>
'''

from typing import List
error_message = "n must be equal to or greater than 0"


def fibonacci_nth_iterative(n: int) -> int:
    """
    Returns the nth number in the Fibonacci sequence.
    Iterative implementation.
    """
    if n < 0:
        raise ValueError(error_message)
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c


def fibonacci_nth_recursive(n: int) -> int:
    """
    Returns the nth number in the Fibonacci sequence.
    Recursive implementation.
    """
    if n < 0:
        raise ValueError(error_message)
    if n <= 1:
        return n
    return fibonacci_nth_recursive(n-1) + fibonacci_nth_recursive(n-2)


def fibonacci_nth_recursive_with_memoization(n: int, memo={}) -> int:
    """
    Returns the nth number in the Fibonacci sequence.
    Recursive implementation with memoization.
    The memo dictionary stores previously computed Fibonacci values.
    """
    if n < 0:
        raise ValueError(error_message)
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_nth_recursive_with_memoization(n - 1) + fibonacci_nth_recursive_with_memoization(n - 2)
    return memo[n]


def fibonacci_sequence(n: int) -> List[int]:
    """ Returns a list of Fibonacci numbers from F(0) up to F(n). """
    if n < 0:
        raise ValueError(error_message)
    sequence = [0]
    if n >= 1:
        sequence.append(1)
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
        sequence.append(c)
    return sequence
