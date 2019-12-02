import unittest

from .fizz_buzz import fizz_buzz


class TestFizzBuzz(unittest.TestCase):
    def test_with_number_3(self):
        self.assertEqual(fizz_buzz(3), 'Fizz')

    def test_with_number_5(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')

    def test_with_number_9(self):
        self.assertEqual(fizz_buzz(9), 'Fizz')

    def test_with_number_15(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')

    def test_with_number_20(self):
        self.assertEqual(fizz_buzz(5), 'Buzz')

    def test_with_number_22(self):
        self.assertEqual(fizz_buzz(22), '22')


if __name__ == '__main__':
    unittest.main()
