import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = ["1721", "979", "366", "299", "675", "1456"]
        self.assertEqual(solution.find_2020_2entries(list), 514_579, "Oops")

    def test_part2(self):
        list = ["1721", "979", "366", "299", "675", "1456"]
        self.assertEqual(solution.find_2020_3entries(list), 241_861_950, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
