import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

        self.assertEqual(solution.play_combat(list.split("\n\n")), 306, "Oops")

    def test_part2(self):
        list = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""

        self.assertEqual(solution.play_recursive(list.split("\n\n")), 291, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()