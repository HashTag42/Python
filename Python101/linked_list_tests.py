import unittest
from unittest.mock import patch
from linked_list import LinkedList


class linked_list_display_tests(unittest.TestCase):
    @patch("builtins.print")
    def test_linked_list_display_with_no_nodes(self, mock_print):
        ll = LinkedList()   # Empty list
        ll.display()
        mock_print.assert_called_with("")

    @patch("builtins.print")
    def test_linked_list_display_with_one_node(self, mock_print):
        ll = LinkedList()
        ll.append("A")
        ll.display()
        mock_print.assert_called_with("A -> ")

    @patch("builtins.print")
    def test_linked_list_display_with_two_nodes(self, mock_print):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.display()
        mock_print.assert_called_with("A -> B -> ")


class linked_list_str_tests(unittest.TestCase):
    def test_linked_list_str_no_nodes(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "")

    def test_linked_list_str_one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(str(ll), "A -> ")

    def test_linked_list_str_two_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        self.assertEqual(str(ll), "A -> B -> ")


class linked_list_append_tests(unittest.TestCase):
    def test_linked_list_append_one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(str(ll), "A -> ")

    def test_linked_list_append_three_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(str(ll), "A -> B -> C -> ")

    def test_linked_list_append_duplicate_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("A")
        self.assertEqual(str(ll), "A -> A -> ")


class linked_list_prepend_tests(unittest.TestCase):
    def test_linked_list_prepend_no_nodes(self):
        ll = LinkedList()
        ll.prepend("A")
        self.assertEqual(str(ll), "A -> ")

    def test_linked_list_prepend_one_node(self):
        ll = LinkedList()
        ll.append("B")
        ll.prepend("A")
        self.assertEqual(str(ll), "A -> B -> ")


class linked_list_delete_tests(unittest.TestCase):
    def test_linked_list_delete_one_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.delete("A")
        self.assertEqual(str(ll), "")

    def test_linked_list_delete_tow_nodes_delete_first_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.delete("A")
        self.assertEqual(str(ll), "B -> ")

    def test_linked_list_delete_two_nodes_delete_last_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.delete("B")
        self.assertEqual(str(ll), "A -> ")

    def test_linked_list_delete_three_nodes_delete_middle_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        ll.delete("B")
        self.assertEqual(str(ll), "A -> C -> ")

    def test_linked_list_delete_three_nodes_delete_non_existing_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.delete("D")
        self.assertEqual(str(ll), "A -> ")
