# Learn more at <https://en.wikipedia.org/wiki/Fibonacci_sequence>
# The code assumes the sequence starts with: 0, 1, 1, 2, 3, 5, ...


def fibonacci_sequence(n: int) -> str:
    '''
    Function: fibonacci_sequence(n)
        Returns a string representing the fibonacci sequence up to the nth element.
        Assumes the sequence starts with: 0, 1, 1, 2, 3, 5, ...
    '''
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    sequence = ""
    if n >= 1:
        sequence += "0"
        a = 0
    if n >= 3:
        sequence += ", 1"
        b = 1
    for i in range(3, n + 1):
        c = a + b
        sequence += ", " + str(c)
        a = b
        b = c
    return sequence


def fibonacci_nth_iterative(n: int) -> int:
    '''
    Function: fibonacci_nth_iterative(n)
        Returns the nth number in the Fibonacci sequence.
        Assumes the sequence starts with: 0, 1, 1, 2, 3, 5,...
        Iterative implementation.
    '''
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    elif n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        a, b = 0, 1
        for _ in range(3, n + 1):
            c = a + b
            a = b
            b = c
        return c


def fibonacci_nth_recursive(n: int) -> int:
    '''
    Function: fibonacci_nth_recursive(n)
        Returns the nth number in the Fibonacci sequence.
        Assumes the sequence starts with: 0, 1, 1, 2, 3, 5, ...
        Recursive implementation.
    '''
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    elif n == 1:
        return 0
    elif n <= 3:
        return 1
    else:
        return fibonacci_nth_recursive(n-1) + fibonacci_nth_recursive(n-2)
