import unittest
from my_module import sort_list  # Replace with your actual file/module

class TestSortList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(sort_list([]), [])

    def test_single_element(self):
        self.assertEqual(sort_list([3]), [3])

    def test_unsorted_small_list(self):
        self.assertEqual(sort_list([3, 1, 2]), [1, 2, 3])

    def test_with_duplicates(self):
        self.assertEqual(sort_list([5, 2, 9, 1, 5, 6]), [1, 2, 5, 5, 6, 9])

    def test_reversed_list(self):
        self.assertEqual(sort_list([9, 7, 5, 3, 1]), [1, 3, 5, 7, 9])

    def test_already_sorted(self):
        self.assertEqual(sort_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_negative_and_positive(self):
        self.assertEqual(sort_list([-1, -3, 0, 2, 1]), [-3, -1, 0, 1, 2])

    def test_large_numbers(self):
        self.assertEqual(sort_list([1000, 500, 2000]), [500, 1000, 2000])

if __name__ == '__main__':
    unittest.main()
