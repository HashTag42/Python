'''
Implements a queue object.

A queue implements FIFO (First-In, First-Out) ordering.
'''

from typing import Generic, Iterable, Iterator, List, Optional, TypeVar
T = TypeVar("T")


class QueueNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self.next: Optional[QueueNode[T]] = None


class Queue(Generic[T]):
    def __init__(self, items: Optional[Iterable[T]] = None) -> None:
        """Initializes a queue object. Optionally populates it with an iterable of items."""
        self.head: Optional[QueueNode[T]] = None
        self.tail: Optional[QueueNode[T]] = None
        self._size: int = 0
        if items is not None:
            self._add_from_iterable(items)

    def add(self, data: T) -> None:
        """Add an item to the end of the queue"""
        new_node = QueueNode(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    # Alias for add (standard queue terminology)
    enqueue = add

    def clear(self) -> None:
        """Clears the queue"""
        self.head = self.tail = None
        self._size = 0

    def copy(self) -> "Queue[T]":
        """Return a shallow copy of the queue"""
        return Queue(self)

    def is_empty(self) -> bool:
        """Return True if and only if the queue is empty"""
        return self._size == 0

    def peek(self) -> Optional[T]:
        """Return the first item in the queue. Return None if the queue is empty"""
        return self.head.data if self.head else None

    def remove(self) -> T:
        """Remove and return the first item in the queue. Raises IndexError if the queue is empty"""
        if self.head:
            data = self.head.data
            self.head = self.head.next
            self._size -= 1
            if not self.head:
                self.tail = None
            return data
        else:
            raise IndexError("remove from empty queue")

    def to_list(self) -> List[T]:
        return list(self)

    # Alias for remove (standard queue terminology)
    dequeue = remove

    def _add_from_iterable(self, values: Iterable[T]) -> None:
        """Add items to the queue using values from an iterable"""
        for val in values:
            self.add(val)

    def __bool__(self) -> bool:
        """Return True if the queue is not empty, False otherwise"""
        return not self.is_empty()

    def __contains__(self, item: T) -> bool:
        """Support: item in queue"""
        return any(item == x for x in self)

    def __iter__(self) -> Iterator[T]:
        """Support: for item in queue"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __eq__(self, other: object) -> bool:
        """Support usage of the '==' equality comparison between queues"""
        if not isinstance(other, Queue):
            return NotImplemented
        if len(self) != len(other):
            return False
        # Type checker now knows 'other' is a Queue
        return all(a == b for a, b in zip(self, other))

    def __len__(self) -> int:
        """Return the number of items in the queue"""
        return self._size

    def __repr__(self) -> str:
        """Return a developer-friendly string representation"""
        return f"Queue({list(self)})"

    def __str__(self) -> str:
        """Return a user-friendly string representation"""
        if self.is_empty():
            return "Queue(empty)"
        return f"Queue([{' <- '.join(str(item) for item in self)}])"
