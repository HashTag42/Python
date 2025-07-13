import math

def isPrime(number: int) -> bool:
    isPrime = True
    if number < 2:
        isPrime = False
    elif number == 2:
        isPrime = True
    elif number % 2 == 0:
        isPrime = False
    else:
        stop = int(math.sqrt(number)) + 1
        for d in range (3, stop, 2):
            if ((number % d) == 0):
                isPrime = False
                break
    return isPrime
