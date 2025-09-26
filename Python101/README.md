# Python 101

A collection of functions and classes to illustrate how to solve basic problems in Python. Usage is demonstrated through the included unit tests.

## ```BinaryTree```

* [```BinaryTree.py```](./BinaryTree.py) implements a ```BinaryTree``` class with supporting methods:

  * ```insert()```
  * ```search()```
  * ```inorder_traversal()```
  * ```height()```

* [```BinaryTree_tests.py```](./BinaryTree_tests.py) implements unit tests with 100% statement and branch coverage

## ```Classes```

* [```classes.py```](./classes.py) implements classes demonstrating inheritance:
  * Human
    * Person
      * Man
      * Woman
  * Vehicle
    * Car
    * Motorcycle
* [```classes_tests.py```](./classes_tests.py) implements unit tests with 100% statement and branch coverage

## ```Datetime```

* [```datime_tests.py```](./datetime_tests.py) implements unit tests to demonstrate the use of the `date`, `datetime`, `time`, and `deltatime` classes

## ```Factorial``` functions

* [```factorial.py```](./factorial.py) implements [Factorial](https://en.wikipedia.org/wiki/Factorial) functions

  * ```factorial_iterative(n)``` returns ```n!``` through an iterative implementation
  * ```factorial_recursive(n)``` returns ```n!``` through a recursive implementation

* [```factorial_tests.py```](./factorial_tests.py) implements unit tests with 100% statement and branch coverage

## ```Fibonacci``` functions

* [```fibonacci.py```](./fibonacci.py) implements functions related to the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence), defined as:
    > ```F(0) = 0, F(1) = 1```
    >
    > ```F(n) = F(n - 1) + F(n - 2), with n > 1```

  * ```fibonacci_nth_iterative(n)``` returns F(n) through an iterative implementation
  * ```fibonacci_nth_recursive(n)``` returns F(n) through a recursive implementation
  * ```fibonacci_nth_recursive_with_memoization(n)``` returns F(n) through a recursive implementation using [memoization](https://en.wikipedia.org/wiki/Memoization) to store past results
  * ```fibonacci_sequence(n)``` returns a string representing a list of Fibonacci numbers from F(0) to F(n)

* [```fibonacci_tests.py```](./fibonacci_tests.py) implements unit tests with 100% statement and branch coverage

## ```Files```

* [```files.py```](./files.py) illustrates file manipulation

## ```Functions```

* [```functions.py```](./functions.py) illustrates different types of functions with:

  * no arguments
  * named arguments
  * variable number of arguments
  * variable number of keyword arguments
  * weak argument type validation
  * strong argument type validation
  * function decorator

* [```functions_tests.py```](./functions_tests.py) implements unit tests with 100% statement and branch coverage

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

## ```Sequences```

* [```sequences_tests.py```](./sequences_tests.py) defines unit tests to illustrate how to access sequences of items

## ```SortedList``` class

* [```SortedList.py```](./SortedList.py) implements a ```SortedList``` subclass of the ```list``` class.
* [```SortedList_tests.py```](./SortedList_tests.py) implements unit tests with 100% statement and branch coverage

## ```Types```

* [```types_tests.py```](./types_tests.py) defines unit tests to illustrate all basic data types:

  * int
  * float
  * complex
  * str
  * bool
  * list
  * tuple
  * range
  * dict
  * set
  * frozenset
  * NoneType

***
