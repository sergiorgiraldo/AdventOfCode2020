# puzzle prompt: https://adventofcode.com/2020/day/6

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Group:
    def __init__(self, group):
        group = group.splitlines()
        self.num_of_people = len(group)
        self.answers = [0] * 26
        for person in group:
            for answer in person:
                self.answers[ord(answer) - 97] += 1

    def get_any_yes_answers(self):
        return sum([answer > 0 for answer in self.answers])

    def get_all_yes_answers(self):
        return sum([answer == self.num_of_people for answer in self.answers])

class Solution(InputAsStringSolution):
    _year = 2020
    _day = 6

    def get_questions_with_any_yes(self, lines):
        groups = [Group(group) for group in lines.split("\n\n")]

        return sum([group.get_any_yes_answers() for group in groups])

    def get_questions_with_all_yes(self, lines):
        groups = [Group(group) for group in lines.split("\n\n")]

        return sum([group.get_all_yes_answers() for group in groups])
    
    def part_1(self):
        start_time = time.time()

        res = self.get_questions_with_any_yes(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_questions_with_all_yes(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()