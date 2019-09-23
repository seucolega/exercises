import unittest
from if_else import if_else


class IfElseTest(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(if_else(3), 'Weird')

    def test_even_between_2_and_5(self):
        self.assertEqual(if_else(2), 'Not Weird')

    def test_not_even_between_2_and_5(self):
        self.assertEqual(if_else(5), 'Weird')

    def test_even_between_6_and_20__6(self):
        self.assertEqual(if_else(6), 'Weird')

    def test_even_between_6_and_20__20(self):
        self.assertEqual(if_else(20), 'Weird')

    def test_not_even_greater_20(self):
        self.assertEqual(if_else(21), 'Weird')

    def test_even_greater_20(self):
        self.assertEqual(if_else(22), 'Not Weird')


if __name__ == '__main__':
    unittest.main()
