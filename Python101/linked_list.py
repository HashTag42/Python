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

    def prepend(self, data):
        """Add a node to the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

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

    def display(self):
        """Print the list."""
        print(str(self))

    def __str__(self):
        """ Returns a string representation of the linked list"""
        result = ""
        current = self.head
        while current:
            result += current.data + " -> "
            current = current.next
        return result
