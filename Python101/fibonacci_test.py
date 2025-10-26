import pytest
from fibonacci import (
    fibonacci_nth_iterative,
    fibonacci_nth_recursive,
    fibonacci_nth_recursive_with_memoization,
    fibonacci_sequence
)


fibonacci_cases = [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (5, 5),
    (10, 55),
]

fibonacci_sequence_cases = [
    (0, [0]),
    (1, [0, 1]),
    (2, [0, 1, 1]),
    (5, [0, 1, 1, 2, 3, 5]),
    (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
]

fibonacci_exception_cases = [
    (-1, ValueError),
    ("A", TypeError),
]


@pytest.mark.parametrize("n, expected", fibonacci_cases)
def test__fibonacci_nth_iterative__(n, expected):
    assert expected == fibonacci_nth_iterative(n)


@pytest.mark.parametrize("n, expected", fibonacci_exception_cases)
def test__fibonacci_nth_iterative__exceptions(n, expected):
    with pytest.raises(expected):
        fibonacci_nth_iterative(n)


@pytest.mark.parametrize("n, expected", fibonacci_cases)
def test__fibonacci_nth_recursive__(n, expected):
    assert expected == fibonacci_nth_recursive(n)


@pytest.mark.parametrize("n, expected", fibonacci_exception_cases)
def test__fibonacci_nth_recursive__exceptions(n, expected):
    with pytest.raises(expected):
        fibonacci_nth_recursive(n)


@pytest.mark.parametrize("n, expected", fibonacci_cases)
def test__fibonacci_nth_recursive_with_memoization__(n, expected):
    assert expected == fibonacci_nth_recursive_with_memoization(n)


@pytest.mark.parametrize("n, expected", fibonacci_exception_cases)
def test__fibonacci_nth_recursive_with_memoization__exceptions(n, expected):
    with pytest.raises(expected):
        fibonacci_nth_recursive_with_memoization(n)


@pytest.mark.parametrize("n, expected", fibonacci_sequence_cases)
def test__fibonacci_sequence__(n, expected):
    assert expected == fibonacci_sequence(n)


@pytest.mark.parametrize("n, expected", fibonacci_exception_cases)
def test__fibonacci_sequence__exceptions(n, expected):
    with pytest.raises(expected):
        fibonacci_sequence(n)
