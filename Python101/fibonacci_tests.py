import unittest

from fibonacci import fibonacci_iterative, fibonacci_recursive


class fibonacci_iterative_Tests(unittest.TestCase):
    def test_fibonacci_iterative_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_iterative(-1)

    def test_fibonacci_iterative_0_is_0(self):
        self.assertEqual(fibonacci_iterative(0), 0)

    def test_fibonacci_iterative_1_is_1(self):
        self.assertEqual(fibonacci_iterative(1), 1)

    def test_fibonacci_iterative_2_is_1(self):
        self.assertEqual(fibonacci_iterative(2), 1)

    def test_fibonacci_iterative_3_is_2(self):
        self.assertEqual(fibonacci_iterative(3), 2)

    def test_fibonacci_iterative_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            fibonacci_iterative("A")


class fibonacci_recursive_Tests(unittest.TestCase):
    def test_fibonacci_recursive_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            fibonacci_recursive(-1)

    def test_fibonacci_recursive_0_is_0(self):
        self.assertEqual(fibonacci_recursive(0), 0)

    def test_fibonacci_recursive_1_is_1(self):
        self.assertEqual(fibonacci_recursive(1), 1)

    def test_fibonacci_recursive_2_is_1(self):
        self.assertEqual(fibonacci_recursive(2), 1)

    def test_fibonacci_recursive_3_is_2(self):
        self.assertEqual(fibonacci_recursive(3), 2)

    def test_fibonacci_recursive_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            fibonacci_recursive("A")
