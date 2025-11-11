import unittest
import pytest
from LinkedList import LinkedList


class LinkedList__init__tests(unittest.TestCase):
    def test_LinkedList__init__object_creation(self):
        ll = LinkedList()
        self.assertTrue(isinstance(ll, LinkedList))

    def test_LinkedList__init__with_list(self):
        ll = LinkedList([1, 2, 3])
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_LinkedList__init__with_empty_list(self):
        ll = LinkedList([])
        self.assertEqual(ll.to_list(), [])


class LinkedList__append__tests(unittest.TestCase):
    def test_LinkedList__append__one_node(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.to_list(), [1])

    def test_LinkedList__append__three_nodes(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_LinkedList__append__duplicate_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("A")
        self.assertEqual(ll.to_list(), ["A", "A"])


class LinkedList__append_from_list__tests(unittest.TestCase):
    def test_LinkedList__append_from_list__None(self):
        ll = LinkedList()
        ll.append_from_list(None)
        self.assertEqual(ll.to_list(), [])

    def test_LinkedList__append_from_list__one_node(self):
        ll = LinkedList()
        ll.append_from_list([1])
        self.assertEqual(ll.to_list(), [1])

    def test_LinkedList__append_from_list__three_node(self):
        ll = LinkedList()
        ll.append_from_list(["A", "B", "C"])
        self.assertEqual(ll.to_list(), ["A", "B", "C"])

    def test_LinkedList__append_from_list__with_preexisting_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append_from_list(["C", "D"])
        self.assertEqual(ll.to_list(), ["A", "B", "C", "D"])


class LinkedList__prepend__tests(unittest.TestCase):
    def test_LinkedList__prepend__no_nodes(self):
        ll = LinkedList()
        ll.prepend("A")
        self.assertEqual(ll.to_list(), ["A"])

    def test_LinkedList__prepend__one_node(self):
        ll = LinkedList()
        ll.append("B")
        ll.prepend("A")
        self.assertEqual(ll.to_list(), ["A", "B"])


class LinkedList__insert__tests(unittest.TestCase):
    def test_LinkedList__insert__empty_list(self):
        ll = LinkedList()
        ll.insert("", "A")
        self.assertEqual(ll.to_list(), [])

    def test_LinkedList__insert__middle_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("C")
        ll.insert("A", "B")
        self.assertEqual(ll.to_list(), ["A", "B", "C"])

    def test_LinkedList__insert__last_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.insert("B", "C")
        self.assertEqual(ll.to_list(), ["A", "B", "C"])


class LinkedList__delete__tests(unittest.TestCase):
    def test_LinkedList__delete__one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertTrue(ll.delete("A"))
        self.assertEqual(ll.to_list(), [])

    def test_LinkedList__delete__from_two_nodes_delete_first_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        self.assertTrue(ll.delete("A"))
        self.assertEqual(ll.to_list(), ["B"])

    def test_LinkedList__delete__from_two_nodes_delete_last_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        self.assertTrue(ll.delete("B"))
        self.assertEqual(ll.to_list(), ["A"])

    def test_LinkedList__delete__from_three_nodes_delete_middle_node(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertTrue(ll.delete("B"))
        self.assertEqual(ll.to_list(), ["A", "C"])

    def test_LinkedList__delete__from_one_node_delete_non_existing_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertFalse(ll.delete("D"))
        self.assertEqual(ll.to_list(), ["A"])


class LinkedList__to_list__tests(unittest.TestCase):
    def test_LinkedList__to_list__three_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(ll.to_list(), ["A", "B", "C"])


class LinkedList__clear__tests(unittest.TestCase):
    def test_LinkedList__clear__three_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        ll.clear()
        self.assertEqual(ll.to_list(), [])


class LinkedList__find__tests(unittest.TestCase):
    def test_LinkedList__find__first_node_found(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(ll.find("A").data, "A")

    def test_LinkedList__find__middle_node_found(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(ll.find("B").data, "B")

    def test_LinkedList__find__last_node_found(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(ll.find("C").data, "C")

    def test_LinkedList__find__no_node_found(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        ll.append("C")
        self.assertEqual(ll.find("D"), None)


class LinkedList__str__tests(unittest.TestCase):
    def test_LinkedList__str__no_nodes(self):
        ll = LinkedList()
        self.assertEqual(str(ll), "")

    def test_LinkedList__str__one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(str(ll), "A")

    def test_LinkedList__str__two_nodes(self):
        ll = LinkedList()
        ll.append("A")
        ll.append("B")
        self.assertEqual(str(ll), "A -> B")


class LinkedList__len__tests(unittest.TestCase):
    def test_LinkedList__len__no_nodes(self):
        ll = LinkedList()
        self.assertEqual(len(ll), 0)

    def test_LinkedList__len__one_node(self):
        ll = LinkedList()
        ll.append("A")
        self.assertEqual(len(ll), 1)


class LinkedList__iter__tests(unittest.TestCase):
    def test_LinkedList__iter__three_nodes(self):
        ll = LinkedList()
        ll.append_from_list(["A", "B", "C"])
        items = []
        for x in ll:
            items.append(x)
        self.assertEqual(items, ["A", "B", "C"])


class LinkedList__sorted__tests(unittest.TestCase):
    def test_LinkedList__sort__empty_list(self):
        ll = LinkedList()
        ll.append_from_list([])
        self.assertEqual(sorted(ll), [])

    def test_LinkedList__sorted__one_node(self):
        ll = LinkedList()
        ll.append_from_list(["A"])
        self.assertEqual(sorted(ll), ["A"])

    def test_LinkedList__sorted__three_nodes_reversed(self):
        ll = LinkedList()
        ll.append_from_list(["C", "B", "A"])
        self.assertEqual(sorted(ll), ["A", "B", "C"])

    def test_LinkedList__sorted__three_nodes_presorted(self):
        ll = LinkedList()
        ll.append_from_list(["A", "B", "C"])
        self.assertEqual(sorted(ll), ["A", "B", "C"])


@pytest.mark.parametrize("list1, list2, expected", [
    # Positive cases
    (None, None, True),
    ([], [], True),
    ([1], [1], True),
    ([1, 2, 3], [1, 2, 3], True),
    # Negative cases
    (None, [1], False),
    ([], [1], False),
    ([1], [2], False),
    ([1], [1, 2], False),
    ([1, 2], [1, 2, 3], False),
    ([1, 9, 3], [1, 2, 3], False),
])
def test_LinkedList__eq__(list1, list2, expected):
    assert (LinkedList(list1) == LinkedList(list2)) == expected


def test_LinkedList__eq__NotImplemented():
    ll = LinkedList([1, 2, 3])
    assert ll.__eq__("not a linked list") is NotImplemented


@pytest.mark.parametrize("list, item, expected", [
    ([1, 2, 3], 2, True),
    ([], 2, False),
    ([1, 2, 3], 4, False),
])
def test_LinkedList__contains__(list, item, expected):
    assert (item in LinkedList(list)) == expected
