import pytest
from Stack import Stack


################################################################################
# region Stack.__init__(nodes)
@pytest.mark.parametrize("data, length, peek", [
    (None, 0, None),
    ([], 0, None),
    (["A", "B", "C"], 3, "C"),
])
def test_Stack__init__(data, length, peek):
    stack = Stack(data)
    assert isinstance(stack, Stack)
    assert len(stack) == length
    assert stack.peek() == peek
# endregion
################################################################################


################################################################################
# region Stack.__iter__()
@pytest.mark.parametrize("values, expected", [
    ([], []),
    ([1], [1]),
    ([1, 2, 3], [3, 2, 1]),
])
def test_Stack__iter__(values, expected):
    stack = Stack(values)
    items = []
    for i in stack:
        items.append(i)
    assert items == expected
# endregion
################################################################################


################################################################################
# region Stack.__len__()
@pytest.mark.parametrize("data, expected", [
    (None, 0),
    ([], 0),
    ([1], 1),
    ([1, 2, 3], 3),
])
def test_Stack__len__(data, expected):
    stack = Stack(data)
    assert len(stack) == expected
# endregion
################################################################################


################################################################################
# region Stack.is_empty()
@pytest.mark.parametrize("data, expected", [
    (None, True),
    ([], True),
    ([1], False),
    ([1, 2, 3], False),
])
def test_Stack_is_empty(data, expected):
    stack = Stack(data)
    assert stack.is_empty() == expected
# endregion
################################################################################


################################################################################
# region Stack_min()
@pytest.mark.parametrize("nodes, expected", [
    (None,  None),
    ([], None),
    ([2, 1, 3], 1),
    ([2, 1, 0], 0),
    ([-2, -1, 0], -2),
    (["A", "B", "C"], "A"),
])
def test_Stack_min(nodes, expected):
    stack = Stack(nodes)
    assert stack.min() == expected


def test_Stack_min_multiple_operations_1():
    stack = Stack([2, 1, 0])
    assert stack.peek() == 0
    assert stack.min() == 0
    stack.pop()
    assert stack.peek() == 1
    assert stack.min() == 1


def test_Stack_min_multiple_operations_2():
    stack = Stack()
    assert stack.min() is None
    stack.push(5)
    assert stack.min() == 5
    stack.push(6)
    assert stack.min() == 5
    stack.push(3)
    assert stack.min() == 3
    stack.push(7)
    assert stack.min() == 3
    stack.push(3)
    assert stack.min() == 3
    stack.pop()
    assert stack.min() == 3
    stack.pop()
    assert stack.min() == 3
    stack.pop()
    assert stack.min() == 5
    stack.pop()
    assert stack.min() == 5
    stack.pop()
    assert stack.min() is None
# endregion
################################################################################


################################################################################
# region Stack.peek()
@pytest.mark.parametrize("data, peek", [
    # data, peek
    (None, None),
    ([], None),
    (["A"], "A"),
    (["A", "B"], "B"),
    (["A", "B", "C"], "C"),
])
def test_Stack_peek(data, peek):
    stack = Stack()
    stack.push_from_list(data)
    assert stack.peek() == peek
# endregion
################################################################################


################################################################################
# region Stack.pop()
@pytest.mark.parametrize("data, pop_count, pop_values, length, peek", [
    ([], 1, [None], 0, None),
    ([], 2, [None, None], 0, None),
    (["A"], 1, ["A"], 0, None),
    (["A"], 2, ["A", None], 0, None),
    (["A", "B"], 1, ["B"], 1, "A"),
    (["A", "B"], 2, ["B", "A"], 0, None),
    (["A", "B"], 3, ["B", "A", None], 0, None),
])
def test_Stack_pop(data, pop_count, pop_values, length, peek):
    stack = Stack(data)
    for i in range(pop_count):
        assert stack.pop() == pop_values[i]
    assert len(stack) == length
    assert stack.peek() == peek
# endregion
################################################################################


################################################################################
# region Stack.push(data)
@pytest.mark.parametrize("data, length, peek", [
    ([], 0, None),
    (["A"], 1, "A"),
    (["A", "B"], 2, "B"),
    (["A", "B", "C"], 3, "C"),
])
def test_Stack_push(data, length, peek):
    stack = Stack()
    for item in data:
        stack.push(item)
    assert len(stack) == length
    assert stack.peek() == peek
# endregion
################################################################################


################################################################################
# region Stack.push_from_list(list)
@pytest.mark.parametrize("data, length, peek", [
    (None, 0, None),
    ([], 0, None),
    (["A"], 1, "A"),
    (["A", "B"], 2, "B"),
    (["A", "B", "C"], 3, "C"),
])
def test_Stack_push_from_list(data, length, peek):
    stack = Stack()
    stack.push_from_list(data)
    assert len(stack) == length
    assert stack.peek() == peek
# endregion
################################################################################
