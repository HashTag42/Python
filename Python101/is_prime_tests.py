import unittest
from is_prime import is_prime


class is_prime_Tests(unittest.TestCase):
    def test_is_prime_negative_is_False(self):
        self.assertEqual(is_prime(-1), False)

    def test_is_prime_0_is_False(self):
        self.assertEqual(is_prime(0), False)

    def test_is_prime_1_is_False(self):
        self.assertEqual(is_prime(1), False)

    def test_is_prime_2_is_True(self):
        self.assertEqual(is_prime(2), True)

    def test_is_prime_3_is_True(self):
        self.assertEqual(is_prime(3), True)

    def test_is_prime_4_is_False(self):
        self.assertEqual(is_prime(4), False)

    def test_is_prime_35_is_False(self):
        self.assertEqual(is_prime(35), False)

    def test_is_prime_37_is_True(self):
        self.assertEqual(is_prime(37), True)

    def test_is_prime_Float_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            is_prime(3.14)

    def test_is_prime_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            is_prime("A")
