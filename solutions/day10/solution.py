# puzzle prompt: https://adventofcode.com/2020/day/10

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from functools import lru_cache
from collections import defaultdict

class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 10

    def parse(self, lines):
        input_ = tuple(map(int, lines))
        self.input = sorted((0,) + input_ + (max(input_) + 3,)) #must use an instance variable because of lru_cache,
                                                              #tuples are not hashable and can't be passed
                                                              #as parameter      

    def find_jolt_differences(self, lines):
        self.parse(lines)

        differences = defaultdict(int)
        
        for adapter, other_adapter in zip(self.input, self.input[1:]):
            differences[abs(other_adapter - adapter)] += 1

        return differences[1] * differences[3]        

    #for each adapter, i check if there is the next adapter that is 1, 2, or 3 jolts away and then recurse
    #e.g adapters [10,11,14,15,17,20]
    ##begin 10 -> 11 -> 14 ...
    #when I am at adapter 14, i check for adapters 15, 16, 17, so 2 branches
    #start  10 -> 11 -> 14 -> 15 -> 17 -> 20
    #also   10 -> 11 -> 14 -> 17 -> 20
    #when I reach the end (20) I count 1
    #also memoize, there are trillions of combinations
    @lru_cache 
    def count_arrangements(self, adapter):
        if adapter == self.input[-1]: 
            return 1
        
        count = 0
        
        for i in 1, 2, 3:
            if adapter + i in self.input:
                count += self.count_arrangements(adapter + i)

        return count

    def arrange_adapters(self, lines):
        self.parse(lines)
        
        return self.count_arrangements(self.input[0])

    def part_1(self):
        start_time = time.time()

        res = self.find_jolt_differences(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.arrange_adapters(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()