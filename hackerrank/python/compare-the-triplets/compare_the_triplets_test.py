import unittest
from compare_the_triplets import compare_the_triplets


class CompareTheTripletsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(compare_the_triplets([5, 6, 7], [3, 6, 10]), [1, 1])

    def test_2(self):
        self.assertEqual(compare_the_triplets([17, 28, 30], [99, 16, 8]), [2, 1])


if __name__ == '__main__':
    unittest.main()
