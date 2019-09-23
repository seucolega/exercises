import unittest
from arithmetic_operators import arithmetic_operators


class ArithmeticOperatorsTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(arithmetic_operators(2, 3), [5, -1, 6])

    def test_2(self):
        self.assertEqual(arithmetic_operators(6, 4), [10, 2, 24])


if __name__ == '__main__':
    unittest.main()
