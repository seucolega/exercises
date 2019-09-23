import unittest
from simple_array_sum import simple_array_sum


class SimpleArraySumTest(unittest.TestCase):
    def test_1(self):
        self.assertIs(simple_array_sum([2, 3]), 5)


if __name__ == '__main__':
    unittest.main()
