import math


def isPrime(n: int) -> bool:
    """
    Checks if a given number is prime.

    Args:
        n (int): The number to check.

    Returns
        bool: True if the number is prime, False otherwise.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    elif n <= 1:        # Numbers equal to or less than 1 are not prime
        return False
    elif n == 2:        # 2 is the first prime number
        return True
    elif n % 2 == 0:    # All even number after 2 are not prime
        return False
    else:
        # Check for perfect divisibility from 3 up to the square root of n,
        # incrementing by 2 to check only odd numbers
        for d in range(3, int(math.sqrt(n)) + 1, 2):
            if ((n % d) == 0):
                return False
    return True
