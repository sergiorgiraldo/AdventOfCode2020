# puzzle prompt: https://adventofcode.com/2020/day/1

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 1

    def find_2020_2entries(self, lines):
        entries = [int(n.strip()) for n in lines]

        for i in range(len(entries)):
            for j in range(i, len(entries)):
                if entries[i] + entries[j] == 2020:
                    return entries[i] * entries[j]

    def find_2020_3entries(self, lines):
        entries = [int(n.strip()) for n in lines]

        for i in range(len(entries)):
            for j in range(i, len(entries)):
                for k in range(j, len(entries)):
                    if entries[i] + entries[j] + entries[k] == 2020:
                        return entries[i] * entries[j] * entries[k]

    def part_1(self):
        start_time = time.time()

        res = self.find_2020_2entries(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.find_2020_3entries(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
