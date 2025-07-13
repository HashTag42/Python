import unittest
from isPrime import isPrime

class isPrimeTests(unittest.TestCase):
    def test_isPrime_negative_False(self):
        self.assertEqual(isPrime(-1), False)
    def test_isPrime_0_False(self):
        self.assertEqual(isPrime(0), False)
    def test_isPrime_1_False(self):
        self.assertEqual(isPrime(1), False)
    def test_isPrime_2_True(self):
        self.assertEqual(isPrime(2), True)
    def test_isPrime_3_True(self):
        self.assertEqual(isPrime(3), True)
    def test_isPrime_4_True(self):
        self.assertEqual(isPrime(4), False)
    def test_isPrime_5_True(self):
        self.assertEqual(isPrime(5), True)
    def test_isPrime_9_True(self):
        self.assertEqual(isPrime(9), False)
    def test_isPrime_String_Raises_TypeError_Exception(self):
        with self.assertRaises(TypeError):
            isPrime("A")
