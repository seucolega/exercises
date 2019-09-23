import unittest
from a_very_big_sum import a_very_big_sum


class AVeryGigSumTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(a_very_big_sum([2, 3]), 5)

    def test_2(self):
        self.assertEqual(a_very_big_sum([-2**31, 2**31 - 1]), -1)

    def test_3(self):
        self.assertEqual(a_very_big_sum([2**31 - 1, 2**31 - 1]), 2 * (2**31 -1))


if __name__ == '__main__':
    unittest.main()
