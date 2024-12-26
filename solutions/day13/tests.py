import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = ["939", "7,13,x,x,59,x,31,19"]
        self.assertEqual(solution.get_shuttle_bus(list), 295, "Oops")

    def test_part2(self):
        list = ["939", "7,13,x,x,59,x,31,19"]
        self.assertEqual(solution.win_gold_coin(list), 1_068_781, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
