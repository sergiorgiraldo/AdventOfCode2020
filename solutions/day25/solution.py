# puzzle prompt: https://adventofcode.com/2020/day/25

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from itertools import count

class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 25

    def get_encryption_key(self, keys):
        card_key, door_key = *map(int, keys),

        cycles = 1
        subject_number = 1

        while True:
            subject_number *= 7         #magic number from puzzle
            subject_number %= 20201227  #magic number from puzzle
            if subject_number == door_key:
                break
            else:
                cycles += 1

        sum = 1
        for _ in range(cycles):
            sum *= card_key
            sum %= 20201227

        return sum
    
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

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()