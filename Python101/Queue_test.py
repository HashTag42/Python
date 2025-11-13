import pytest
from Queue import Queue


################################################################################
# region Queue
def test_Queue_mixed_operations():
    # Empty queue operations
    q = Queue()
    assert q.peek() is None
    assert len(q) == 0
    assert list(q) == []
    assert q == Queue()

    # Single element
    q = Queue([1])
    assert q.remove() == 1
    assert q.is_empty()

    # Copy independence
    q1 = Queue([1, 2, 3])
    q2 = q1.copy()
    q2.remove()
    assert len(q1) == 3  # Original unchanged

    # Equality with different types
    q = Queue([1, 2])
    assert (q.__eq__([1, 2])) == NotImplemented
    assert q != [1, 2]  # Falls back to identity check

    # Contains with None
    q = Queue([None, 1, 2])
    assert None in q

    # Test complex sequence of operations
    q = Queue()
    q.add(1)
    q.add(2)
    assert q.remove() == 1
    q.add(3)
    assert q.remove() == 2
    q.add(4)
    assert list(q) == [3, 4]


def test_Queue_multiple_iterations():
    q = Queue([1, 2, 3])
    list1 = list(q)
    list2 = list(q)
    assert list1 == list2 == [1, 2, 3]


def test_Queue_with_custom_objects():
    class Item:
        def __init__(self, val):
            self.val = val

        def __eq__(self, other):
            return isinstance(other, Item) and self.val == other.val

    q = Queue([Item(1), Item(2)])
    assert Item(1) in q
# endregion
################################################################################


# region Queue.__init__(items)
@pytest.mark.parametrize("values, length, peek", [
    (None, 0, None),
    ([], 0, None),
    (["A"], 1, "A"),
    (["A", "B"], 2, "A"),
    (["A", "B", "C"], 3, "A"),
])
def test_Queue__init__(values, length, peek):
    q = Queue(values)
    assert isinstance(q, Queue)
    assert len(q) == length
    assert q.peek() == peek
# endregion
################################################################################


################################################################################
# region Queue.__bool__(item)
@pytest.mark.parametrize("values, expected", [
    ([], False),
    (["A"], True),
])
def test_Queue__bool__(values, expected):
    q = Queue(values)
    assert bool(q) == expected
# endregion
################################################################################


################################################################################
# region Queue.__contains__(item)
@pytest.mark.parametrize("values, item, expected", [
    ([], "A", False),
    (["A"], "A", True),
    (["A"], "B", False),
    (["A", "B", "C"], "A", True),
    (["A", "B", "C"], "B", True),
    (["A", "B", "C"], "C", True),
    (["A", "B", "C"], "D", False),
])
def test_Queue__contains__(values, item, expected):
    q = Queue(values)
    assert (item in q) == expected
# endregion
################################################################################


################################################################################
# region Queue.__eq__(object)
@pytest.mark.parametrize("queue1, queue2, expected", [
    (Queue([]), Queue([]), True),
    (Queue(["A"]), Queue([]), False),
    (Queue(["A"]), Queue(["A"]), True),
    (Queue(["A"]), Queue(["B"]), False),
])
def test_Queue__eq__(queue1, queue2, expected):
    assert (queue1 == queue2) == expected


def test_Queue__eq__with_non_queue():
    q = Queue([1, 2, 3])
    # Direct call to __eq__ should return NotImplemented
    result = q.__eq__([1, 2, 3])   # comparing to a list
    assert result == NotImplemented
    # Using == should evaluate to False
    assert (q == [1, 2, 3]) is False
    # Comparing to an unrelated type
    assert (q == "not a queue") is False
    assert (q.__eq__("not a queue")) == NotImplemented


def test_Queue__eq__after_mutation():
    q1 = Queue([1, 2])
    q2 = Queue([1, 2])
    q1.remove()
    assert q1 != q2
# endregion
################################################################################


################################################################################
# region Queue.__iter__()
def test_Queue__iter__iteration_independence():
    """Test that iteration doesn't modify the queue"""
    q = Queue([1, 2, 3])
    # Iterate multiple times without modification
    assert list(q) == [1, 2, 3]
    assert list(q) == [1, 2, 3]  # Should still be the same
# endregion
################################################################################


################################################################################
# region Queue.__len__()
def test_Queue__len__():
    q = Queue([1, 2, 3])
    assert len(q) == 3
    q.remove()
    assert len(q) == 2
# endregion
################################################################################


################################################################################
# region Queue.__repr__()
def test_Queue__repr__():
    q = Queue([1, 2, 3])
    assert repr(q) == "Queue([1, 2, 3])"
# endregion
################################################################################


################################################################################
# region Queue.__str__()
@pytest.mark.parametrize("values, expected", [
    ([], "Queue(empty)"),
    ([1], "Queue([1])"),
    ([1, 2, 3], "Queue([1 <- 2 <- 3])"),
])
def test_Queue__str__(values, expected):
    q = Queue(values)
    assert str(q) == expected
# endregion
################################################################################


################################################################################
# region Queue.add(data) and enqueue(data)
def test_Queue_add_and_enqueue():
    q = Queue()
    q.add("A")
    q.enqueue("B")
    assert list(q) == ["A", "B"]
    assert q.peek() == "A"
# endregion


################################################################################
# region Queue.clear()
def test_Queue_clear():
    q = Queue([1, 2, 3])
    q.clear()
    assert len(q) == 0


def test_Queue_clear_then_reuse():
    q = Queue([1, 2, 3])
    q.clear()
    q.add(4)
    assert list(q) == [4]
    assert not q.is_empty()
# endregion
################################################################################


################################################################################
# region Queue.copy()
def test_Queue_copy():
    q1 = Queue([1, 2, 3])
    q2 = q1.copy()
    assert list(q2) == [1, 2, 3]
# endregion
################################################################################


################################################################################
# region Queue.is_empty()
@pytest.mark.parametrize("values, expected", [
    ([], True),
    (["A"], False)
])
def test_Queue_is_empty(values, expected):
    q = Queue(values)
    assert q.is_empty() == expected
# endregion
################################################################################


################################################################################
# region Queue.remove()
@pytest.mark.parametrize("add_values, remove_count, length, peek", [
    (["A"], 1, 0, None),
    (["A", "B", "C"], 1, 2, "B"),
    (["A", "B", "C"], 2, 1, "C"),
])
def test_Queue_remove(add_values, remove_count, length, peek):
    q = Queue(add_values)
    for _ in range(remove_count):
        q.remove()
    assert len(q) == length
    assert q.peek() == peek


def test_Queue_remove_raises_on_empty():
    q = Queue([])
    with pytest.raises(IndexError):
        q.remove()


def test_Queue_remove_last_item_then_add():
    """Tests that 'tail' is correctly reset after removing the last item."""
    q = Queue(["A"])

    # Remove the last item
    q.remove()
    assert q.is_empty()
    assert q.head is None
    assert q.tail is None

    # Add a new item
    q.add("B")
    assert len(q) == 1
    assert q.peek() == "B"
    assert q.head is not None
    # Check that both head and tail point to the new node
    assert q.head is q.tail
    assert q.head.data == "B"


def test_Queue_dequeue():
    q = Queue([1, 2, 3])
    assert q.dequeue() == 1
    assert q.dequeue() == 2
# endregion
################################################################################


################################################################################
# region Queue.to_list()
@pytest.mark.parametrize("values, expected", [
    ([], []),
    (["A"], ["A"]),
    (["A", "B"], ["A", "B"]),
    (["A", "B", "C"], ["A", "B", "C"]),
])
def test_Queue_to_list(values, expected):
    q = Queue(values)
    assert q.to_list() == expected
# endregion
################################################################################
