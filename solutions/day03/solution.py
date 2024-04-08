# puzzle prompt: https://adventofcode.com/2020/day/3

import time
import sys
sys.path.insert(0,"..")

from base.advent import *

class Solution(InputAs2DSolution):
    _year = 2020
    _day = 3

    def find_trees_single(self, map, right, down):
        trees,i,j = 0,0,0
        
        width = len(map[0])

        while True:
            i += down
            j += right
            
            if i >= len(map): break

            if map[i][j % width] == "#":
                trees += 1
        
        return trees

    def find_trees_multiple(self, map):
        return \
            self.find_trees_single(map, 1, 1) * \
            self.find_trees_single(map, 3, 1) * \
            self.find_trees_single(map, 5, 1) * \
            self.find_trees_single(map, 7, 1) * \
            self.find_trees_single(map, 1, 2)

    def part_1(self):
        start_time = time.time()
        
        res = self.find_trees_single(self.input, 3, 1)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.find_trees_multiple(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == '__main__':
    solution = Solution()

    solution.part_1()

    solution.part_2()
