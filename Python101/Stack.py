'''
Implements a stack object.

A stack uses LIFO (Last-In, First-Out) ordering. It allows constant-time adds and removes.
'''

from typing import Generic, Iterator, List, Optional, TypeVar
T = TypeVar("T")


class StackNode(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data
        self._sub_min: int = data
        self.next: Optional[StackNode[T]] = None


class Stack(Generic[T]):
    def __init__(self, nodes: Optional[List[T]] = None) -> None:
        """Initializes a Stack object. Optionally populates it with a list of items."""
        self.head = None
        self._size = 0
        if nodes:
            self.push_from_list(nodes)

    def push(self, data: T) -> None:
        """Add an item at the top of the stack"""
        new_node = StackNode(data)
        new_node.next = self.head
        if self.head:
            new_node._sub_min = min(new_node.data, self.head._sub_min)
        self.head = new_node
        self._size += 1

    def push_from_list(self, lst: Optional[List[T]]) -> None:
        """Add a list of nodes at the top of the stack"""
        if lst is None:
            return
        for val in lst:
            self.push(val)

    def pop(self) -> Optional[T]:
        """Remove and return the data at the top of the stack, or None if empty"""
        if self.is_empty():
            return None
        pop_value = self.head.data
        self.head = self.head.next
        self._size -= 1
        if self.head and self.head.next:
            self.head._sub_min = min(self.head._sub_min, self.head.next._sub_min)
        return pop_value

    def peek(self) -> Optional[T]:
        """Return the data at the top of the stack, or None if empty"""
        if self.head:
            return self.head.data
        else:
            return None

    def is_empty(self) -> bool:
        """Return true if and only if the stack is empty"""
        return self._size == 0

    def min(self) -> int:
        """Return the minimum eledment in the stack"""
        return self.head._sub_min if self.head else None

    def __len__(self) -> int:
        """Return the number of nodes in the stack"""
        return self._size

    def __iter__(self) -> Iterator[T]:
        """Allows iteration like: for i in stack"""
        current = self.head
        while current:
            yield current.data
            current = current.next
