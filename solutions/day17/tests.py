import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            ".#.",
            "..#",
            "###"
        ]
        self.assertEqual(solution.boot_3d(list), 112, "Oops")

    def test_part2(self):
        list = [
            ".#.",
            "..#",
            "###"
        ]
        self.assertEqual(solution.boot_4d(list), 848, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()