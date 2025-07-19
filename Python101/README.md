# Python 101

A collection of functions and classes to illustrate how to solve basic problems in Python. Usage is demonstrated through the included unit tests.

## ```BinaryTree``` class

* [```BinaryTree.py```](./BinaryTree.py) implements a ```BinaryTree``` class with supporting methods:
  * ```insert()```
  * ```search()```
  * ```inorder_traversal()```
* [```BinaryTree_tests.py```](./BinaryTree_tests.py) implements unit tests with 100% statement and branch coverage

## ```factorial``` functions

* [```factorial.py```](./factorial.py) implements [Factorial](https://en.wikipedia.org/wiki/Factorial) functions:
  * ```factorial_iterative(n)``` returns ```n!``` through an iterative implementation
  * ```factorial_recursive(n)``` returns ```n!``` through a recursive implementation

* [```factorial_tests.py```](./factorial_tests.py) implements unit tests with 100% statement and branch coverage

## ```fibonacci``` functions

* [```fibonacci.py```](./fibonacci.py) implements functions related to the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence):
  * ```fibonacci_iterative(n)``` returns F(n) through an iterative implementation
  * ```fibonacci_recursive(n)``` returns F(n) through a recursive implementation

* [```fibonacci_tests.py```](./fibonacci_tests.py) implements unit tests with 100% statement and branch coverage

## ```is_prime``` function

* [```is_prime.py```](./is_prime.py) implements a function to determine the [primality](https://en.wikipedia.org/wiki/Primality_test) of a given number:
  * ```is_prime(n)``` returns True if n is prime, False otherwise
    * Uses the ```isinstance()``` function to verify if an argument is of the expected type
* [```is_prime_tests.py```](./isPrime_tests.py) implements unit tests with 100% statement and branch coverage

## ```LinkedList``` class

* [```LinkedList.py```](./LinkedList.py) implements a ```LinkedList``` class with supporting methods:
  * ```append()```
  * ```prepend()```
  * ```insert()```
  * ```delete()```
  * ```display()```
  * ```__str__```
  * ```__len__```
* [```LinkedList_tests.py```](./LinkedList_tests.py) implements unit tests with 100% statement and branch coverage
  * Uses the ```mock_print``` function to verify ```print()``` output
