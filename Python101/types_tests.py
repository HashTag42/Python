import unittest


class types_tests(unittest.TestCase):

    # NUMERIC TYPES
    def test_int(self):
        i = 0
        self.assertEqual(type(i), int)

    def test_float(self):
        f = 0.0
        self.assertEqual(type(f), float)

    def test_complex(self):
        c = 2 + 3j
        self.assertEqual(type(c), complex)

    # TEXT TYPE
    def test_str(self):
        s = " "
        c = 'ab'
        self.assertEqual(type(s), str)
        self.assertEqual(type(c), str)

    # BOOLEAN TYPE
    def test_bool(self):
        t = True
        f = False
        self.assertEqual(type(t), bool)
        self.assertEqual(type(f), bool)

    # SEQUENCE TYPES
    def test_list(self):
        numbers = [1, 2, 3]
        self.assertEqual(type(numbers), list)

    def test_tuple(self):
        t = (1, 2, 3)
        self.assertEqual(type(t), tuple)

    def test_range(self):
        r = range(0, 10)
        self.assertEqual(type(r), range)

    # MAPPING TYPE
    def test_dict(self):
        d = {"name": "César", "role": "SDET"}
        self.assertEqual(type(d), dict)

    # SET TYPES
    def test_set(self):
        s = {1, 2, 3}
        self.assertEqual(type(s), set)

    def test_frozentest(self):
        fs = frozenset([1, 2])
        self.assertEqual(type(fs), frozenset)

    # NONE TYPE
    def test_NoneType(self):
        n = None
        # This is the Pythonic way to do a type check of None:
        self.assertTrue(n is None)
