import unittest

from .division import integer_division, float_division


class TestDivision(unittest.TestCase):
    def test_integer_division_7_in_3(self):
        self.assertEqual(integer_division(7, 3), 2)

    def test_integer_division_5_in_2(self):
        self.assertEqual(integer_division(5, 2), 2)

    def test_float_division_7_in_3(self):
        self.assertEqual(float_division(7, 3), 7 / 3)


if __name__ == '__main__':
    unittest.main()
