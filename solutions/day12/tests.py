import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = ["F10", "N3", "F7", "R90", "F11"]
        self.assertEqual(solution.get_distance(list)[0], 25, "Oops")

    def test_part2(self):
        list = ["F10", "N3", "F7", "R90", "F11"]
        self.assertEqual(solution.get_distance(list)[1], 286, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
