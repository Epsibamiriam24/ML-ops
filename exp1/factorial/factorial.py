#test_my_module.py
import unittest
from my_module import fact
class Factorial(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(fact(5), 120)
    def test_zero(self):
        self.assertEqual(fact(0), 1) 
    def test_negative(self):
        self.assertRaises(ValueError)
    def test_non_numeric_type(self):
        self.assertRaises(TypeError)
    def test_for_float_numbers(self):
        self.assertRaises(TypeError)
if __name__ == '__main__':
    unittest.main()

