import unittest
from SortedList import SortedList


class TestSortedList(unittest.TestCase):

    def setUp(self):
        self.SortedList = SortedList
        pass

    def test_initialization_with_no_iterable_creates_empty_list(self):
        sl = self.SortedList()
        self.assertEqual(sl, [])
        self.assertIsInstance(sl, list)

    def test_initialization_sorts_elements(self):
        sl = self.SortedList([5, 1, 3])
        self.assertEqual(sl, [1, 3, 5])

    def test_append_maintains_sort_order(self):
        sl = self.SortedList([1, 3, 5])
        sl.append(2)
        self.assertEqual(sl, [1, 2, 3, 5])

    def test_extend_maintains_sort_order(self):
        sl = self.SortedList([1, 4])
        sl.extend([3, 2])
        self.assertEqual(sl, [1, 2, 3, 4])

    def test_insert_maintains_sort_order(self):
        sl = self.SortedList([1, 4])
        sl.insert(0, 3)  # index ignored; should insert sorted
        self.assertEqual(sl, [1, 3, 4])

    def test_setitem_single_value_re_sorts(self):
        sl = self.SortedList([1, 3, 5])
        sl[1] = 4
        self.assertEqual(sl, [1, 4, 5])

    def test_setitem_slice_re_sorts(self):
        sl = self.SortedList([1, 3, 5, 7])
        sl[1:3] = [6, 2]
        self.assertEqual(sl, [1, 2, 6, 7])

    def test_iadd_maintains_sort_order(self):
        sl = self.SortedList([1, 3])
        sl += [2, 0]
        self.assertEqual(sl, [0, 1, 2, 3])
