import unittest
from my_module import Palindrome
class palin(unittest.TestCase):
    def test_all_string(self):
            with self.assertRaises(TypeError):
                Palindrome(123)
            with self.assertRaises(TypeError):
                Palindrome(True)
            with self.assertRaises(TypeError):
                Palindrome(None)   

    def test_check_with_string(self):
        self.assertEqual(Palindrome("madam"), "madam")
        self.assertEqual(Palindrome(""), "", "Empty string should be a palindrome")
        self.assertEqual(Palindrome("a"), "a", "Single character string should be a palindrome")
       
if __name__== '__main__':
     unittest.main()

































