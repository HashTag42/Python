# Python 101

A collection of functions and classes to illustrate how to solve basic problems in Python. Usage is demonstrated through the included unit tests.

## `BinaryTree`

* [`BinaryTree.py`](./BinaryTree.py) implements a `BinaryTree` class with supporting methods:

  * `height()`
  * `inorder_traversal()`
  * `insert()`
  * `levels()`
  * `search()`

* [`BinaryTree_tests.py`](./BinaryTree_tests.py) implements unit tests with 100% statement and branch coverage

## `Classes`

* [`classes.py`](./classes.py) implements classes demonstrating inheritance:
  * Human
    * Person
      * Man
      * Woman
  * Vehicle
    * Car
    * Motorcycle
* [`classes_tests.py`](./classes_tests.py) implements unit tests with 100% statement and branch coverage

## `Datetime`

* [`datime_tests.py`](./datetime_tests.py) implements unit tests to demonstrate the use of the `date`, `datetime`, `time`, and `deltatime` classes

## `Factorial` functions

* [`factorial.py`](./factorial.py) implements [Factorial](https://en.wikipedia.org/wiki/Factorial) functions

  * `factorial_iterative(n)` returns `n!` through an iterative implementation
  * `factorial_recursive(n)` returns `n!` through a recursive implementation

* [`factorial_tests.py`](./factorial_tests.py) implements unit tests with 100% statement and branch coverage

## `Fibonacci` functions

* [`fibonacci.py`](./fibonacci.py) implements functions related to the [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence), defined as:
    > `F(0) = 0, F(1) = 1`
    >
    > `F(n) = F(n - 1) + F(n - 2), with n > 1`

  * `fibonacci_nth_iterative(n)` returns F(n) through an iterative implementation
  * `fibonacci_nth_recursive(n)` returns F(n) through a recursive implementation
  * `fibonacci_nth_recursive_with_memoization(n)` returns F(n) through a recursive implementation using [memoization](https://en.wikipedia.org/wiki/Memoization) to store past results
  * `fibonacci_sequence(n)` returns a string representing a list of Fibonacci numbers from F(0) to F(n)
  * `fibonacci_generator()` implements a `Generator` function

* [`fibonacci_tests.py`](./fibonacci_tests.py) implements unit tests with 100% statement and branch coverage

## `Files`

* [`files.py`](./files.py) illustrates file manipulation

## `Functions`

* [`functions.py`](./functions.py) illustrates different types of functions with:

  * no arguments
  * named arguments
  * variable number of arguments
  * variable number of keyword arguments
  * weak argument type validation
  * strong argument type validation
  * function decorator

* [`functions_tests.py`](./functions_tests.py) implements unit tests with 100% statement and branch coverage

## `Graph` class

* [`Graph.py`](./Graph.py) implements a graph object with the following methods:
  * `add_edge()`
  * `add_node()`
  * `bfs()` # bread-first search
  * `find_node()`
  * `get_weight()`
  * `has_edge()`
  * `print_matrix()`
  * `remove_edge()`
  * `search_route()` # alias for `bfs()`
  * `__repr__()`

* [`Graph_test.py`](./Graph_test.py) implement unit tests with 100% statement and branch coverage

## `GraphNode` class

* [`GraphNode.py`](./GraphNode.py) implements a graph node object with the following properties and methods:

  * `NodeState` property
  * `add_neighbor()`
  * `get_neighbors()`
  * `is_visited()`
  * `mark_visited()`
  * `mark_unvisited()`
  * `remove_neighbor()`
  * `__eq__()`
  * `__format__()`
  * `__hash__()`
  * `__lt__()`
  * `__repr__()`

* [`GraphNode_test.py`](./GraphNode_test.py) implements unit tests with 100% statement and branch coverage

## Internet

* [`internet_test.py`](./internet_test.py) illustrates usage of the `urllib.request` library

## `is_prime` function

* [`is_prime.py`](./is_prime.py) implements a function to determine the [primality](https://en.wikipedia.org/wiki/Primality_test) of a given number:

  * `is_prime(n)` returns True if n is prime, False otherwise

    * Uses the `isinstance()` function to verify if an argument is of the expected type

* [`is_prime_tests.py`](./isPrime_tests.py) implements unit tests with 100% statement and branch coverage

## `LinkedList` class

* [`LinkedList.py`](./LinkedList.py) implements a `LinkedList` class with supporting methods:

  * `append()`
  * `append_from_list()`
  * `prepend()`
  * `insert()`
  * `delete()`
  * `to_list()`
  * `clear()`
  * `find()`
  * `pop_head()`
  * `__str__()`
  * `__len__()`
  * `__iter__()`
  * `__eq__()`
  * `__contains__()`

* [`LinkedList_tests.py`](./LinkedList_tests.py) implements unit tests with 100% statement and branch coverage

  * Uses the `mock_print` function to verify `print()` output

## `Queue` class

* [`Queue.py`](./Queue.py) implements a queue node and a queue object with the following methods:

  * `__init__()`
  * `add()`, and `enqueue` alias
  * `clear()`
  * `copy()`
  * `is_empty()`
  * `peek()`
  * `remove()`, and `dequeue` alias
  * `_add_from_iterable()`
  * `__bool__()`
  * `__contains__()`
  * `__iter__()`
  * `__eq__()`
  * `__len__()`
  * `__repr__()`
  * `__str__()`

* [`Queue_test.py`](./Queue_test.py) implements unit tests with 100% statement and branch coverage

## `Sequences`

* [`sequences_tests.py`](./sequences_tests.py) defines unit tests to illustrate how to access sequences of items

## `SortedList` class

* [`SortedList.py`](./SortedList.py) implements a `SortedList` subclass of the `list` class.
* [`SortedList_tests.py`](./SortedList_tests.py) implements unit tests with 100% statement and branch coverage

## `Stack` class

* [`Stack.py`](./Stack.py) implements a stack node and a stack object with the following methods:

  * `__init__()`
  * `push()`
  * `push_from_list()`
  * `pop()`
  * `peek()`
  * `is_empty()`
  * `min()`
  * `clear()`
  * `__len__()`
  * `__iter__()`
  * `__str__()`

* [`Stack_test.py`](./Stack_test.py) implements unit tests with 100% statement and branch coverage

## `Types`

* [`types_tests.py`](./types_tests.py) defines unit tests to illustrate all basic data types:

  * `int`
  * `float`
  * `complex`
  * `str`
  * `bool`
  * `list`
  * `tuple`
  * `range`
  * `dict`
  * `set`
  * `frozenset`
  * `NoneType`

***
