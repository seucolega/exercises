import unittest
from solve_me_first import solve_me_first


class SolveMeFirstTest(unittest.TestCase):
    def test_1(self):
        self.assertIs(solve_me_first(2, 3), 5)


if __name__ == '__main__':
    unittest.main()
