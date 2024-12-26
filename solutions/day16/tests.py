import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""
        self.assertEqual(solution.get_error_rate(list)[1], 71, "Oops")

    def test_part2(self):
        list = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""

        row = solution.determine_my_ticket(list)[0].rule_index.get("row")
        self.assertEqual(row, 0, "Oops")

        class_ = solution.determine_my_ticket(list)[0].rule_index.get("class")
        self.assertEqual(class_, 1, "Oops")

        seat = solution.determine_my_ticket(list)[0].rule_index.get("seat")
        self.assertEqual(seat, 2, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
