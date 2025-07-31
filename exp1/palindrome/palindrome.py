import unittest
from my_module import palindrome
class palin(unittest.TestCase):
    def test_all_string(self):
            with self.assertRaises(TypeError):
                palindrome(123)
            with self.assertRaises(TypeError):
                palindrome(True)
            with self.assertRaises(TypeError):
                palindrome(None)   

    def test_check_with_string(self):
        self.assertEqual(palindrome("madam"), "madam")
        self.assertEqual(palindrome(""), "", "Empty string should be a palindrome")
        self.assertEqual(palindrome("a"), "a", "Single character string should be a palindrome")
       
if __name__== '__main__':
     unittest.main()

































