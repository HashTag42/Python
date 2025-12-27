from typing import Any, Generator
import csv


def csv_row_reader(file_path: str) -> Generator[list[str], None, None]:
    with open(file_path, 'r') as csv_file:
        for row in csv.reader(csv_file):
            yield row


def cumulative_sum() -> Generator[int, int, None]:
    total: int = 0
    while True:
        total += yield total


def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, (a + b)


def infinite_repeater(sequence: list[Any]) -> Generator[Any, None, None]:
    while True:
        for item in sequence:
            yield item
