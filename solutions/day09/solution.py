# puzzle prompt: https://adventofcode.com/2020/day/9

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 9

    def is_sum_of_previous(self, input, window, index):
        for i in range(index - window, index):
            for j in range(i + 1, index):
                if input[i] + input[j] == input[index]:
                    return True
                
        return False

    def find_weak_number(self, lines, window=25):
        input = [int(n.strip()) for n in lines]

        for index in range(window, len(input)):
            if not self.is_sum_of_previous(input, window, index):
                return input[index]
        
    def find_encryption_weakness(self, lines, window=25):
        input = [int(n.strip()) for n in lines]

        weak_number = self.find_weak_number(lines, window)

        for size in range(2, len(input)):
            terms = self.find_contiguous_set(input, weak_number, size)
            
            if len(terms):
                return min(terms) + max(terms)

    def find_contiguous_set(self, input, number, size):
        for i in range(0, len(input) - size + 1):
            terms = []
            
            for j in range(i, i + size):
                terms.append(input[j])

            if sum(terms) == number:
                return terms
        
        return []
                
    def part_1(self):
        start_time = time.time()

        res = self.find_weak_number(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.find_encryption_weakness(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == '__main__':
    solution = Solution()

    solution.part_1()
    
    solution.part_2()