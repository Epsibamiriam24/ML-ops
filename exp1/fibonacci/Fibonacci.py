import unittest
from my_module import fibonacci_upto  # Replace with your actual filename

class TestFibonacciUpto(unittest.TestCase):

    def test_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci_upto(-5)

    def test_zero(self):
        self.assertEqual(fibonacci_upto(0), [0])

    def test_one(self):
        self.assertEqual(fibonacci_upto(1), [0, 1, 1])

    def test_up_to_10(self):
        self.assertEqual(fibonacci_upto(10), [0, 1, 1, 2, 3, 5, 8])

    def test_up_to_25(self):
        self.assertEqual(fibonacci_upto(25), [0, 1, 1, 2, 3, 5, 8, 13, 21])

    def test_string_input(self):
        with self.assertRaises(TypeError):
            fibonacci_upto("abc")

    def test_float_input(self):
        with self.assertRaises(TypeError):
            fibonacci_upto(3.5)

if __name__ == '__main__':
    unittest.main()