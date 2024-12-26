import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = """abc

a
b
c

ab
ac

a
a
a
a

b"""

        self.assertEqual(solution.get_questions_with_any_yes(list), 11, "Oops")

    def test_part2(self):
        list = """abc

a
b
c

ab
ac

a
a
a
a

b"""

        self.assertEqual(solution.get_questions_with_all_yes(list), 6, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
