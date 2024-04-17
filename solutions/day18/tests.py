import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        self.assertEqual(solution.evaluate(
            "1 + 2 * 3 + 4 * 5 + 6"), 71, "Oops")
        self.assertEqual(solution.evaluate(
            "1 + (2 * 3) + (4 * (5 + 6))"), 51, "Oops")
        self.assertEqual(solution.evaluate(
            "2 * 3 + (4 * 5)"), 26, "Oops")
        self.assertEqual(solution.evaluate(
            "5 + (8 * 3 + 9 + 3 * 4 * 3)"), 437, "Oops")
        self.assertEqual(solution.evaluate(
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"), 1_2240, "Oops")
        self.assertEqual(solution.evaluate(
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13_632, "Oops")

    def test_part2(self):
        self.assertEqual(solution.evaluate(
            "1 + 2 * 3 + 4 * 5 + 6", True), 231, "Oops")
        self.assertEqual(solution.evaluate(
            "1 + (2 * 3) + (4 * (5 + 6))", True), 51, "Oops")
        self.assertEqual(solution.evaluate(
            "2 * 3 + (4 * 5)", True), 46, "Oops")
        self.assertEqual(solution.evaluate(
            "5 + (8 * 3 + 9 + 3 * 4 * 3)", True), 1445, "Oops")
        self.assertEqual(solution.evaluate(
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", True), 669_060, "Oops")
        self.assertEqual(solution.evaluate(
            "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", True), 23_340, "Oops")
        self.assertEqual(solution.evaluate(
            "3 + (2 * 2 + (7 * 3) * 2) + 7 + 4 + (2 + 6 * 4 + 9 * 4 * 5)", True), 2186, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
