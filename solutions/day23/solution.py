# puzzle prompt: https://adventofcode.com/2020/day/23

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from itertools import islice, chain, count


# poor man's linked list
class Cup:
    label: int
    succ: "Cup"

    def __init__(self, label, succ=None):
        self.label = label
        if succ is None:
            self.succ = self
        else:
            self.succ = succ

    def insert_succ(self, cup):
        cup.succ = self.succ
        self.succ = cup

    def remove_succ(self):
        succ = self.succ
        self.succ = succ.succ
        return succ

    def labels(self):
        yield self.label
        cup = self.succ
        while cup != self:
            yield cup.label
            cup = cup.succ

    def cups(self):
        yield self
        cup = self.succ
        while cup != self:
            yield cup
            cup = cup.succ


class Solution(InputAsStringSolution):
    _year = 2020
    _day = 23

    def make_circle(self, labels):
        reversed_labels = iter(reversed(list(labels)))
        head = last = Cup(next(reversed_labels))

        for label in reversed_labels:
            head = Cup(label, head)

        last.succ = head

        return head

    def get_cups(self, head, moves):
        cups = dict((cup.label, cup) for cup in head.cups())
        lowest, highest = min(cups), max(cups)

        for _ in range(moves):
            picked = [head.remove_succ() for _ in range(3)]
            picked_labels = {cup.label for cup in picked}
            dest = head.label - 1

            while (a := dest < lowest) or (_ := dest in picked_labels):
                if a:
                    dest = highest
                else:
                    dest -= 1

            while picked:
                cups[dest].insert_succ(picked.pop())

            head = head.succ

        return cups[1]

    def play(self, input, moves=100):
        labels = list(map(int, input))

        return "".join(
            map(str, self.get_cups(self.make_circle(labels), moves).labels())
        )[1:]

    def play_a_lot(self, input):
        labels = list(map(int, input))

        highest = max(labels)
        head = self.make_circle(islice(chain(labels, count(highest + 1)), 1_000_000))
        head = self.get_cups(head, 10_000_000)
        return head.succ.label * head.succ.succ.label

    def part_1(self):
        start_time = time.time()

        res = self.play(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.play_a_lot(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
