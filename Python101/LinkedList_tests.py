import unittest
from LinkedList import LinkedList


class LinkedList_init_tests(unittest.TestCase):
    def test_LinkedList_object_creation(self):
        ll = LinkedList()
        self.assertTrue(isinstance(ll, LinkedList))


class LinkedList_append_tests(unittest.TestCase):
    def test_LinkedList_append_one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(str(ll), "A -> ")

    def test_LinkedList_append_three_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(str(ll), "A -> B -> C -> ")

    def test_LinkedList_append_duplicate_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("A")
        self.assertEqual(str(ll), "A -> A -> ")


class LinkedList_append_from_list_tests(unittest.TestCase):
    def test_LinkedList_append_from_list_one_node(self):
        ll = LinkedList()
        ll.append_from_list([1])
        self.assertTrue(str(ll), "1 -> ")

    def test_LinkedList_append_from_list_three_node(self):
        ll = LinkedList()
        ll.append_from_list(["A", "B", "C"])
        self.assertTrue(str(ll), "A -> B -> C -> ")


class LinkedList_prepend_tests(unittest.TestCase):
    def test_LinkedList_prepend_no_nodes(self):
        ll = LinkedList()
        ll.prepend("A")
        self.assertEqual(str(ll), "A -> ")

    def test_LinkedList_prepend_one_node(self):
        ll = LinkedList()
        ll.append("B")
        ll.prepend("A")
        self.assertEqual(str(ll), "A -> B -> ")


class LinkedList_insert_tests(unittest.TestCase):
    def test_LinkedList_insert_empty_list(self):
        ll = LinkedList()
        ll.insert("", "A")
        self.assertEqual(str(ll), "A -> ")

    def test_LinkedList_insert_middle_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("C")
        ll.insert("A", "B")
        self.assertEqual(str(ll), "A -> B -> C -> ")

    def test_LinkedList_insert_last_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.insert("B", "C")
        self.assertEqual(str(ll), "A -> B -> C -> ")


class LinkedList_delete_tests(unittest.TestCase):
    def test_LinkedList_delete_one_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.delete("A")
        self.assertEqual(str(ll), "")

    def test_LinkedList_delete_from_two_nodes_delete_first_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.delete("A")
        self.assertEqual(str(ll), "B -> ")

    def test_LinkedList_delete_from_two_nodes_delete_last_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.delete("B")
        self.assertEqual(str(ll), "A -> ")

    def test_LinkedList_delete_from_three_nodes_delete_middle_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        ll.delete("B")
        self.assertEqual(str(ll), "A -> C -> ")

    def test_LinkedList_delete_from_one_node_delete_non_existing_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.delete("D")
        self.assertEqual(str(ll), "A -> ")


class LinkedList_str_tests(unittest.TestCase):
    def test_LinkedList_str_no_nodes(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "")

    def test_LinkedList_str_one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(str(ll), "A -> ")

    def test_LinkedList_str_two_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        self.assertEqual(str(ll), "A -> B -> ")


class LinkedList_len_tests(unittest.TestCase):
    def test_LinkedList_len_no_nodes(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)

    def test_LinkedList_len_one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(len(ll), 1)
