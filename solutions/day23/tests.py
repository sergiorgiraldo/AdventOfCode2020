import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = "389125467"

        self.assertEqual(solution.play(list, 10), "92658374")
        self.assertEqual(solution.play(list, 100), "67384529")

    def test_part2(self):
        list = "389125467"

        self.assertEqual(solution.play_a_lot(list), 149_245_887_792)

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
