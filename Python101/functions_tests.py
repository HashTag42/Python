import unittest
from functions import function
from functions import power
from functions import multi_add
from functions import echo_kwargs
from functions import echo_any
from functions import echo_int_weak_typed
from functions import echo_int_strong_typed


class functions_tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_function(self):
        self.assertEqual(function(), "I am a function")

    def test_power_1(self):
        self.assertEqual(power(1), 1)

    def test_power_10_2(self):
        self.assertEqual(power(10, 2), 100)

    def test_power_10_2_named_arguments(self):
        self.assertEqual(power(x=2, num=10), 100)

    def test_multi_add_no_arguments(self):
        self.assertEqual(multi_add(), 0)

    def test_multi_add_one_argument(self):
        self.assertEqual(multi_add(1), 1)

    def test_multi_add_two_arguments(self):
        self.assertEqual(multi_add(1, 2), 3)

    def test_multi_add_four_arguments(self):
        self.assertEqual(multi_add(4, 5, -10, 4), 3)

    def test_echo_kwargs(self):
        self.assertEqual(echo_kwargs(name="Alice", age=25), "name: Alice, age: 25, ")

    def test_echo_any_number(self):
        self.assertEqual(echo_any(0), 0)

    def test_echo_any_string(self):
        str = "Yadda"
        self.assertEqual(echo_any(str), str)

    def test_echo_int_number(self):
        self.assertEqual(echo_int_weak_typed(0), 0)

    def test_echo_int_string(self):
        str = "Yadda"
        self.assertEqual(echo_int_weak_typed(str), str)

    def test_echo_int_strong_number(self):
        self.assertEqual(echo_int_strong_typed(1), 1)

    def test_echo_int_string_string(self):
        with self.assertRaises(TypeError):
            echo_int_strong_typed("Yadda")
