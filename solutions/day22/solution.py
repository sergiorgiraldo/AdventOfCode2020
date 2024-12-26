# puzzle prompt: https://adventofcode.com/2020/day/22

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from collections import defaultdict, deque


class Solution(InputAsBlockSolution):
    _year = 2020
    _day = 22

    def score(self, deck):
        return sum([(i + 1) * card for i, card in enumerate(reversed(deck))])

    def play_combat(self, players):
        deck1 = [int(card) for card in players[0].splitlines()[1:]]
        deck2 = [int(card) for card in players[1].splitlines()[1:]]

        while len(deck1) and len(deck2):
            card1 = deck1[0]
            card2 = deck2[0]

            if card1 > card2:
                deck1 = deck1[1:] + [card1, card2]
                deck2 = deck2[1:]
            else:
                deck1 = deck1[1:]
                deck2 = deck2[1:] + [card2, card1]

        return self.score(deck1) if len(deck1) else self.score(deck2)

    def play_recursive(self, players):
        deck1 = [int(card) for card in players[0].splitlines()[1:]]
        deck2 = [int(card) for card in players[1].splitlines()[1:]]

        return self.score(self.play_recursive_(deck1, deck2)[1])

    # do the optimization from `curious_sapi3n`. If player 1 is holding the
    # highest card in the sub game decks, it is a win for player 1.
    # cuts down thousands of calls.
    # m > len(deck1) + len(deck2) will check that this is a sub game , see line (*)
    # https://www.reddit.com/r/adventofcode/comments/khyjgv/comment/ggpcsnd/
    def play_recursive_(self, deck1, deck2):
        m = max(deck1)

        if m > max(deck2) and m > len(deck1) + len(deck2):  # (*)
            return True, deck1

        memory = set()
        while len(deck1) and len(deck2):
            s = (tuple(deck1), tuple(deck2))
            if s in memory:
                return True, deck1
            memory.add(s)

            card1 = deck1[0]
            card2 = deck2[0]

            if len(deck1) > card1 and len(deck2) > card2:
                win, _ = self.play_recursive_(
                    deck1[1 : card1 + 1], deck2[1 : card2 + 1]
                )
            else:
                win = card1 > card2

            if win:
                deck1 = deck1[1:] + [card1, card2]
                deck2 = deck2[1:]
            else:
                deck1 = deck1[1:]
                deck2 = deck2[1:] + [card2, card1]

        if len(deck1):
            return True, deck1
        else:
            return False, deck2

    def part_1(self):
        start_time = time.time()

        res = self.play_combat(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.play_recursive(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
