import unittest

from fibonacci import fibonacci_series, fibonacci_nth_iterative, fibonacci_nth_recursive


class fibonacci_series_Tests(unittest.TestCase):
    def test_fibonacci_series_1(self):
        self.assertEqual(fibonacci_series(1), "1")

    def test_fibonacci_series_2(self):
        self.assertEqual(fibonacci_series(2), "1, 1")

    def test_fibonacci_series_3(self):
        self.assertEqual(fibonacci_series(3), "1, 1, 2")

    def test_fibonacci_series_5(self):
        self.assertEqual(fibonacci_series(5), "1, 1, 2, 3, 5")

    def test_fibonacci_series_10(self):
        self.assertEqual(fibonacci_series(10), "1, 1, 2, 3, 5, 8, 13, 21, 34, 55")

    def test_fibonacci_series_0_raises_exception_ValueError(self):
        with self.assertRaises(ValueError):
            fibonacci_series(0)


class fibonacci_nth_iterative_Tests(unittest.TestCase):
    def test_fibonacci_nth_iterative_1_is_1(self):
        self.assertEqual(fibonacci_nth_iterative(1), 1)

    def test_fibonacci_nth_iterative_2_is_1(self):
        self.assertEqual(fibonacci_nth_iterative(2), 1)

    def test_fibonacci_nth_iterative_3_is_2(self):
        self.assertEqual(fibonacci_nth_iterative(3), 2)

    def test_fibonacci_nth_iterative_5_is_5(self):
        self.assertEqual(fibonacci_nth_iterative(5), 5)

    def test_fibonacci_nth_iterative_10_is_55(self):
        self.assertEqual(fibonacci_nth_iterative(10), 55)

    def test_fibonacci_nth_iterative_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_iterative(-1)

    def test_fibonacci_nth_iterative_Zero_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_iterative(0)

    def test_fibonacci_nth_iterative_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            fibonacci_nth_iterative("A")


class fibonacci_nth_recursive_Tests(unittest.TestCase):
    def test_fibonacci_nth_recursive_1_is_1(self):
        self.assertEqual(fibonacci_nth_recursive(1), 1)

    def test_fibonacci_nth_recursive_2_is_1(self):
        self.assertEqual(fibonacci_nth_recursive(2), 1)

    def test_fibonacci_nth_recursive_3_is_2(self):
        self.assertEqual(fibonacci_nth_recursive(3), 2)

    def test_fibonacci_nth_recursive_5_is_5(self):
        self.assertEqual(fibonacci_nth_recursive(5), 5)

    def test_fibonacci_nth_recursive_10_is_55(self):
        self.assertEqual(fibonacci_nth_recursive(10), 55)

    def test_fibonacci_nth_recursive_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_recursive(-1)

    def test_fibonacci_nth_recursive_Zero_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_recursive(0)

    def test_fibonacci_nth_recursive_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            fibonacci_nth_recursive("A")
