# puzzle prompt: https://adventofcode.com/2020/day/15

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsStringSolution):
    _year = 2020
    _day = 15

    # i didn't optimize, part 2 ran in 5 secs ¯\_(ツ)_/¯
    def get_nth_number(self, input, turns):
        numbers = [int(x) for x in input.split(",")]

        mem = {nr: x+1 for x, nr in enumerate(numbers[:-1])}
        last = numbers[-1]

        for count in range(len(numbers), turns):
            mem[last], last = count, count - mem[last] if last in mem else 0
        
        return last

    def part_1(self):
        start_time = time.time()

        res = self.get_nth_number(self.input, 2020)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_nth_number(self.input, 30_000_000)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()