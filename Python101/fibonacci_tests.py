import unittest

from fibonacci import fibonacci_sequence, fibonacci_nth_iterative, fibonacci_nth_recursive


class fibonacci_sequence_Tests(unittest.TestCase):
    def test_fibonacci_sequence_1(self):
        self.assertEqual(fibonacci_sequence(1), "0")

    def test_fibonacci_sequence_3(self):
        self.assertEqual(fibonacci_sequence(3), "0, 1, 1")

    def test_fibonacci_sequence_5(self):
        self.assertEqual(fibonacci_sequence(5), "0, 1, 1, 2, 3")

    def test_fibonacci_sequence_10(self):
        self.assertEqual(fibonacci_sequence(10), "0, 1, 1, 2, 3, 5, 8, 13, 21, 34")

    def test_fibonacci_sequence_Zero_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence(0)

    def test_fibonacci_sequence_Negative_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_sequence(-1)


class fibonacci_nth_iterative_Tests(unittest.TestCase):
    def test_fibonacci_nth_iterative_1(self):
        self.assertEqual(fibonacci_nth_iterative(1), 0)

    def test_fibonacci_nth_iterative_2(self):
        self.assertEqual(fibonacci_nth_iterative(2), 1)

    def test_fibonacci_nth_iterative_3(self):
        self.assertEqual(fibonacci_nth_iterative(3), 1)

    def test_fibonacci_nth_iterative_5(self):
        self.assertEqual(fibonacci_nth_iterative(5), 3)

    def test_fibonacci_nth_iterative_10(self):
        self.assertEqual(fibonacci_nth_iterative(10), 34)

    def test_fibonacci_nth_iterative_Negative_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_iterative(-1)

    def test_fibonacci_nth_iterative_Zero_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_iterative(0)

    def test_fibonacci_nth_iterative_String_raises_TypeError_exception(self):
        with self.assertRaises(TypeError):
            fibonacci_nth_iterative("A")


class fibonacci_nth_recursive_Tests(unittest.TestCase):
    def test_fibonacci_nth_recursive_1(self):
        self.assertEqual(fibonacci_nth_recursive(1), 0)

    def test_fibonacci_nth_recursive_2(self):
        self.assertEqual(fibonacci_nth_recursive(2), 1)

    def test_fibonacci_nth_recursive_3(self):
        self.assertEqual(fibonacci_nth_recursive(3), 1)

    def test_fibonacci_nth_recursive_5(self):
        self.assertEqual(fibonacci_nth_recursive(5), 3)

    def test_fibonacci_nth_recursive_10(self):
        self.assertEqual(fibonacci_nth_recursive(10), 34)

    def test_fibonacci_nth_recursive_Negative_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_recursive(-1)

    def test_fibonacci_nth_recursive_Zero_raises_ValueError_exception(self):
        with self.assertRaises(ValueError):
            fibonacci_nth_recursive(0)

    def test_fibonacci_nth_recursive_String_raises_TypeError_exception(self):
        with self.assertRaises(TypeError):
            fibonacci_nth_recursive("A")
