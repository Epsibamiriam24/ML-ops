import unittest
from my_module import prime
class palin(unittest.TestCase):
    def test_for_negative_numbers(self):
        assert prime(-5) == False, "-5 is not a prime" 
        # Non-prime numbers
        assert prime(4) == False, "4 is not a prime"
    def test_for_0s_1s(self):
        assert prime(
            0) == False, "not a prime"
        assert prime(1) == False, "not a prime"
    def test_for_prime(self):
        # Prime numbers
        assert prime(2) == True, "2 should be prime"
    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            prime("abc")
        with self.assertRaises(TypeError):
            prime(3.5)
        with self.assertRaises(TypeError):
            prime(None)
     #Large Non-Prime Numbers
    def test_large_non_primes(self):
        self.assertFalse(prime(100), "100 is not prime")
        self.assertFalse(prime(1000), "1000 is not prime")
     #Large Prime Numbers
    def test_large_primes(self):
        self.assertTrue(prime(97), "97 should be prime")
# Run the test
if __name__== '__main__':
     unittest.main()
