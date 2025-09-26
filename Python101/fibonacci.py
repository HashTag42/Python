'''
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1.
    That is,
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2), for n > 1.
    The first 10 Fibonacci numbers, from F(0) to F(9), are: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
    Learn more at <https://en.wikipedia.org/wiki/Fibonacci_sequence>
'''


def fibonacci_nth_iterative(n: int) -> int:
    '''
    Function: fibonacci_nth_iterative(n)
        Returns the nth number in the Fibonacci sequence. Iterative implementation.
        Definition of a Fibonacci number:
            F(0) = 0, F(1) = 1,
            F(n) = F(n - 1) + F(n - 2), for n > 1.
    '''
    if n < 0:
        raise ValueError("Number must be a positive integer")
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            c = a + b
            a, b = b, c
        return c


def fibonacci_nth_recursive(n: int) -> int:
    '''
    Function: fibonacci_nth_recursive(n)
        Returns the nth number in the Fibonacci sequence. Recursive implementation.
        Definition of a Fibonacci number:
            F(0) = 0, F(1) = 1,
            F(n) = F(n - 1) + F(n - 2), for n > 1.
    '''
    if n < 0:
        raise ValueError("Number must be a positive integer")
    elif n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci_nth_recursive(n-1) + fibonacci_nth_recursive(n-2)


def fibonacci_sequence(n: int) -> str:
    '''
    Function: fibonacci_sequence(n)
        Returns a string representing a list of the Fibonacci numbers from F(0) up to F(n).
        Definition of a Fibonacci number:
            F(0) = 0, F(1) = 1,
            F(n) = F(n - 1) + F(n - 2), for n > 1.
        Examples:
            fibonacci_sequence(0) = "0"
            fibonacci_sequence(1) = "0, 1"
            fibonacci_sequence(2) = "0, 1, 1"
            fibonacci_sequence(5) = "0, 1, 1, 2, 3, 5"
            fibonacci_sequence(10) = "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55"
    '''
    if n < 0:
        raise ValueError("Number must be a positive integer")
    sequence = ""
    if n >= 0:
        sequence += "0"
    if n >= 1:
        sequence += ", 1"
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = a + b
        a, b = b, c
        sequence += ", " + str(c)
    return sequence
