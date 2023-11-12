import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_swap_k_2(self):
        """ Test swap_k with k=2. """
        nums = [1, 2, 3, 4, 5, 6]
        actual = a1.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(actual, expected)
    def test_swap_k_even_length(self):
        """ Test with an even list """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [5, 6, 3, 4, 1, 2])

    def test_swap_k_odd_length(self):
        """ Test with an odd list """
        nums = [1, 2, 3, 4, 5]
        a1.swap_k(nums, 2)
        self.assertEqual(nums, [4, 5, 3, 1, 2])

    def test_swap_k_full_swap(self):
        """ Test with full swap of list """
        nums = [1, 2, 3, 4, 5, 6]
        a1.swap_k(nums, 3)
        self.assertEqual(nums, [4, 5, 6, 1, 2, 3])

if __name__ == '__main__':
    unittest.main(exit=False)