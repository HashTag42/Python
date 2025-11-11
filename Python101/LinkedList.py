'''
    The LinkedList class implements a singly linked list.
'''

from typing import List, Optional, TypeVar, Generic, Iterator
T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data: T = data  # value of the node
        self.next: Optional[Node[T]] = None  # pointer to the next node


class LinkedList(Generic[T]):
    def __init__(self, nodes: Optional[List[T]] = None) -> None:
        """ Creates a LinkedList, optionally initialized from a list of nodes """
        self.head = None
        self.tail = None
        self._size = 0
        if nodes:
            self.append_from_list(nodes)

    def append(self, data: T) -> None:
        """ Adds a node to the end of the list """
        new_node = Node(data)
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
        self._size += 1

    def append_from_list(self, lst: Optional[List[T]]) -> None:
        """ Appends nodes with values from a list """
        if lst is None:
            return
        for val in lst:
            self.append(val)

    def prepend(self, data: T) -> None:
        """ Adds a node to the beginning of the list """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, node_data: T, new_data: T) -> bool:
        """ Inserts a node after the first node with the given value """
        new_node = Node(new_data)
        current = self.head
        while current:
            if current.data == node_data:
                new_node.next = current.next
                current.next = new_node
                if current == self.tail:
                    self.tail = new_node
                self._size += 1
                return True
            current = current.next
        return False

    def delete(self, data: T) -> bool:
        """ Deletes the first node with the given value. Returns True if deleted, False if not found. """
        current = self.head
        prev = None

        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current.next is None:
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.next

        return False

    def to_list(self) -> List[T]:
        """ Returns a list with the values from the LinkedList """
        return list(iter(self))

    def clear(self) -> None:
        """ Clears the LinkedList """
        self.head = None
        self.tail = None
        self._size = 0

    def find(self, data: T) -> Optional[Node[T]]:
        """ Returns the first node found with the data """
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def __str__(self) -> str:
        """ Returns a string representation of the linked list """
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " -> ".join(values)

    def __len__(self) -> int:
        """ Returns the number of nodes in the list """
        return self._size

    def __iter__(self) -> Iterator[T]:
        """ Allows iteration like: for x in linked_list """
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __eq__(self, other: object) -> bool:
        """ Allows usage of the '==' equality comparison between objects """
        if not isinstance(other, LinkedList):
            return NotImplemented

        cur1, cur2 = self.head, other.head
        while cur1 and cur2:
            if cur1.data != cur2.data:
                return False
            cur1, cur2 = cur1.next, cur2.next
        return cur1 is None and cur2 is None

    def __contains__(self, item: T) -> bool:
        """Supports the 'in' operator"""
        return self.find(item) is not None
