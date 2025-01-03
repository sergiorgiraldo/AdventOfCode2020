# puzzle prompt: https://adventofcode.com/2020/day/25

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from itertools import count


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 25

    def get_encryption_key(self, keys):
        card_key, door_key = (*map(int, keys),)

        public_key = [1, 1]
        encryption_key = 1
        cycles = 0

        # algorithm is symmetric so I can perform the operations in both keys
        # at the same time, whichever matches first is my answer.
        # with this approach, I can cycle just once.
        while True:
            cycles += 1

            public_key[0] = (public_key[0] * 7) % 20201227  # magic numbers from puzzle
            public_key[1] = (public_key[1] * 7) % 20201227

            if public_key[0] == card_key:
                for _ in range(cycles):
                    encryption_key = (encryption_key * door_key) % 20201227

                return encryption_key

            elif public_key[1] == door_key:
                for _ in range(cycles):
                    encryption_key = (encryption_key * card_key) % 20201227

                return encryption_key

            # not big primes, took 4_412_860 cycles to crack, less than a sec :)

    def part_1(self):
        start_time = time.time()

        res = self.get_encryption_key(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = "0"

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
