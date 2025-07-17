# Python 101

A collection of functions, classes, and unit tests to illustrate how to solve basic problems in Python.

## factorial

* [```factorial.py```](./factorial.py) implements [Factorial](https://en.wikipedia.org/wiki/Factorial) functions:
  * ```factorial_iterative(n)``` returns ```n!``` through an iterative implementation
  * ```factorial_recursive(n)``` returns ```n!``` through a recursive implementation

* [```factorial_tests.py```](./factorial_tests.py) implements unit tests with 100% statement and branch coverage

## fibonacci

* [```fibonacci.py```](./fibonacci.py) implements functions related to the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence):
  * ```fibonacci_iterative(n)``` returns F(n) through an iterative implementation
  * ```fibonacci_recursive(n)``` returns F(n) through a recursive implementation

* [```fibonacci_tests.py```](./fibonacci_tests.py) implements unit tests with 100% statement and branch coverage

## isPrime

* [```isPrime.py```](./isPrime.py) implements a function to determine the [primality](https://en.wikipedia.org/wiki/Primality_test) of a given number:
  * ```isPrime(n)``` returns True if n is prime, False otherwise
    * Uses the ```isinstance()``` function to verify if an argument is of the expected type
* [```isPrime_tests.py```](./isPrime_tests.py) implements unit tests with 100% statement and branch coverage

## linked_list

* [```linked_list.py```](./linked_list.py) implements a ```LinkedList``` class with supporting methods:
  * ```append()```
  * ```prepend()```
  * ```delete()```
  * ```display()```
  * ```__str__```
  * ```__len__```
* [```linked_list_tests.py```](./linked_list_tests.py) implements unit tests with 100% statement and branch coverage
  * Uses the ```mock_print``` function to verify ```print()``` output
