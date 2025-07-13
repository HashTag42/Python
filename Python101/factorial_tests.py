import unittest
from factorial import factorial_iterative, factorial_recursive

class factorial_iterative_Tests(unittest.TestCase):
    def test_factorial_iterative_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)
    def test_factorial_iterative_0_is_1(self):
        self.assertEqual(factorial_iterative(0), 1)
    def test_factorial_iterative_1_is_1(self):
        self.assertEqual(factorial_iterative(1), 1)
    def test_factorial_iterative_2_is_2(self):
        self.assertEqual(factorial_iterative(2), 2)
    def test_factorial_iterative_3_is_6(self):
        self.assertEqual(factorial_iterative(3), 6)
    def test_factorial_iterative_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            factorial_iterative("A")

class factorial_recursive_Tests(unittest.TestCase):
    def test_factorial_recursive_Negative_Raises_ValueError_Exception(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
    def test_factorial_recursive_0_is_1(self):
        self.assertEqual(factorial_recursive(0), 1)
    def test_factorial_recursive_1_is_1(self):
        self.assertEqual(factorial_recursive(1), 1)
    def test_factorial_recursive_2_is_2(self):
        self.assertEqual(factorial_recursive(2), 2)
    def test_factorial_recursive_3_is_6(self):
        self.assertEqual(factorial_recursive(3), 6)
    def test_factorial_recursive_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            factorial_recursive("A")
