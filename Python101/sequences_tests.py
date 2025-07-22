import unittest


class sequence_tests(unittest.TestCase):

    ''' You can access items in sequences by using [] brackets '''

    def setUp(self):
        self.mydict = {"i0": 0, "i1": 1, "i2": "two", "i3": 3.2, "i4": False}
        self.mylist = [0, 1, "two", 3.2, False]
        self.mytuple = (0, 1, "two", 3.2, False)

    def test_dict_item(self):
        self.assertEqual(self.mydict["i1"], 1)

    def test_list_item(self):
        self.assertEqual(self.mylist[2], "two")

    def test_list_slice(self):
        self.assertEqual(self.mylist[1:3], [1, "two"])

    def test_list_slice_with_step(self):
        self.assertEqual(self.mylist[1:5:2], [1, 3.2])

    def test_list_slice_reverse(self):
        self.assertEqual(self.mylist[::-1], [False, 3.2, "two", 1, 0])

    def test_tuple_item(self):
        self.assertEqual(self.mytuple[2], "two")

    def test_tuple_slice(self):
        self.assertEqual(self.mytuple[1:3], (1, "two"))
