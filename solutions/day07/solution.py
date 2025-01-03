# puzzle prompt: https://adventofcode.com/2020/day/7

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 7

    def parse(self, lines):
        rules = dict()

        for line in lines:
            bag, contents = line.split(" bags contain ")

            rules[bag] = (
                dict(
                    (words[1] + " " + words[2], int(words[0]))
                    for words in (bag.split() for bag in contents.split(", "))
                )
                if contents != "no other bags."
                else dict()
            )

        return rules

    def get_shiny_gold_bags(self, lines):
        def holds(bag, target):
            return any(held == target or holds(held, target) for held in rules[bag])

        rules = self.parse(lines)

        return sum(1 for bag in rules if holds(bag, "shiny gold"))

    def count_bags(self, rules, bag="shiny gold"):
        return sum(
            n * (1 + self.count_bags(rules, other)) for other, n in rules[bag].items()
        )

    def get_contents_of_single_shiny_gold_bag(self, lines):
        rules = self.parse(lines)

        return self.count_bags(rules)

    def part_1(self):
        start_time = time.time()

        res = self.get_shiny_gold_bags(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_contents_of_single_shiny_gold_bag(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
