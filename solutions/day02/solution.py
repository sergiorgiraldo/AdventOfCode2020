# puzzle prompt: https://adventofcode.com/2020/day/2


import time
import sys

sys.path.insert(0, "..")

from base.advent import *
import re


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 2

    def policy_1(self, word, chr, lo, hi):
        return word.count(chr) in range(lo, hi + 1)

    def policy_2(self, word, chr, lo, hi):
        return (word[lo - 1] == chr and word[hi - 1] != chr) or (
            word[lo - 1] != chr and word[hi - 1] == chr
        )

    def count_passwords(self, lines, in_policy):
        regex = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+)")  # 4-5 m: mmpth

        count = 0

        for line in lines:
            groups = regex.match(line).groups()
            lo = int(groups[0])
            hi = int(groups[1])
            chr = groups[2]
            word = groups[3]

            if in_policy(word, chr, lo, hi):
                count += 1

        return count

    def part_1(self):
        start_time = time.time()

        res = self.count_passwords(self.input, self.policy_1)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.count_passwords(self.input, self.policy_2)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
