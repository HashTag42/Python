import unittest
from isPrime import isPrime


class isPrime_Tests(unittest.TestCase):
    def test_isPrime_negative_is_False(self):
        self.assertEqual(isPrime(-1), False)

    def test_isPrime_0_is_False(self):
        self.assertEqual(isPrime(0), False)

    def test_isPrime_1_is_False(self):
        self.assertEqual(isPrime(1), False)

    def test_isPrime_2_is_True(self):
        self.assertEqual(isPrime(2), True)

    def test_isPrime_3_is_True(self):
        self.assertEqual(isPrime(3), True)

    def test_isPrime_4_is_False(self):
        self.assertEqual(isPrime(4), False)

    def test_isPrime_35_is_False(self):
        self.assertEqual(isPrime(35), False)

    def test_isPrime_37_is_True(self):
        self.assertEqual(isPrime(37), True)

    def test_isPrime_Float_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            isPrime(3.14)

    def test_isPrime_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            isPrime("A")
