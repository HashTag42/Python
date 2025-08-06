import time


def function():
    # Function without arguments
    return "I am a function"


def power(num, x=1):
    # Function with default arguments
    result = 1
    for _ in range(x):
        result *= num
    return result


def multi_add(*args):
    # Function with a variable number of arguments
    result = 0
    for x in args:
        result += x
    return result


def echo_kwargs(**info):
    # **kwargs allows a function to accept any number of named arguments,
    # which are passed in as a dictionary.
    result = ""
    for key, value in info.items():
        result += f"{key}: {value}, "
    return result


def echo_any(input):
    return input


def echo_int_weak_typed(num: int) -> int:
    # Types are not validated at runtime!
    # You can still pass and return any types.
    return num


def echo_int_strong_typed(input):
    if not isinstance(input, int):
        raise TypeError("Argument must be an integer")
    return input


# Decorator definition
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper


@timer
def slow_function():
    time.sleep(1)
    print("Finished")
