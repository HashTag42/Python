from generators import (
    csv_row_reader,
    cumulative_sum,
    fibonacci_generator,
    infinite_repeater,
)


def test_csv_row_reader():
    reader = csv_row_reader('data.csv')
    expected: list[tuple[str, str]] = [
        ['name', ' age'],
        ['Bob', ' 20'],
        ['James', ' 32'],
        ['Charlotte', ' 23'],
        ['Ashley', ' 45'],
        ['Anna', ' 25'],
    ]
    for i in range(5 + 1):
        assert next(reader) == expected[i]
    try:
        next(reader)
    except StopIteration:
        assert True


def test_cumulative_sum():
    cumulative_generator = cumulative_sum()
    # start the generator
    next(cumulative_generator)
    current_sum: int = 0
    for value in range(1, 5 + 1):
        current_sum = cumulative_generator.send(value)
    assert current_sum == 15


def test_fibonacci_generator():
    fib_gen = fibonacci_generator()
    n = 10
    result = ""
    for i in range(n):
        result += f"{next(fib_gen)}, "
    assert result == "0, 1, 1, 2, 3, 5, 8, 13, 21, 34, "


def test_infinite_repeater():
    repeater = infinite_repeater([1, 2, 3, 4])
    result: list[int] = []
    for _ in range(10):
        result.append(next(repeater))
    assert result == [1, 2, 3, 4, 1, 2, 3, 4, 1, 2]
