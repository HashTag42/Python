import unittest
from is_prime import is_prime


class is_prime_Tests(unittest.TestCase):
    def test_is_prime_negative_is_False(self):
        self.assertFalse(is_prime(-1))

    def test_is_prime_0_is_False(self):
        self.assertFalse(is_prime(0))

    def test_is_prime_1_is_False(self):
        self.assertFalse(is_prime(1))

    def test_is_prime_2_is_True(self):
        self.assertTrue(is_prime(2))

    def test_is_prime_3_is_True(self):
        self.assertTrue(is_prime(3))

    def test_is_prime_4_is_False(self):
        self.assertFalse(is_prime(4))

    def test_is_prime_35_is_False(self):
        self.assertFalse(is_prime(35))

    def test_is_prime_37_is_True(self):
        self.assertTrue(is_prime(37))

    def test_is_prime_Float_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            is_prime(3.14)

    def test_is_prime_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            is_prime("A")
