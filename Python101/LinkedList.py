from typing import List


class Node:
    def __init__(self, data):
        self.data = data  # value of the node
        self.next = None  # pointer to the next node


class LinkedList:
    def __init__(self):
        self.head = None  # start with an empty list

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def append_from_list(self, lst: List):
        if lst:
            self.head = Node(lst[0])
            current = self.head
            for val in lst[1:]:
                current.next = Node(val)
                current = current.next

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, node_data, new_data):
        """Inserts a node after the first node with the given value"""
        new_node = Node(new_data)
        if not self.head:
            # Handle an empty list
            self.head = new_node
            return

        current = self.head
        while current.next:
            if current.data == node_data:
                break
            current = current.next
        next_node = current.next
        current.next = new_node
        new_node.next = next_node

    def delete(self, data):
        """Delete the first node with the given value."""
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def __str__(self):
        """Returns a string representation of the linked list"""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " -> "
            current = current.next
        return result

    def __len__(self):
        """Returns the number of nodes in the list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
