import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solution.get_nth_number("0,3,6", 2020), 436, "Oops")

    def test_part2(self):
        self.assertEqual(solution.get_nth_number("0,3,6", 30_000_000), 175_594, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()