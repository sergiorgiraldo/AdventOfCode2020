# puzzle prompt: https://adventofcode.com/2020/day/5

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 5

    def get_seat_id(self, boarding_pass):
        row, mid_row, max_row = 0, 0, 128
        seat, mid_seat, max_seat = 0, 0, 8

        for char in boarding_pass:
            mid_row = (row + max_row) // 2
            mid_seat = (seat + max_seat) // 2

            if char == "F":
                max_row = mid_row
            elif char == "B":
                row = mid_row
            elif char == "L":
                max_seat = mid_seat
            else:
                seat = mid_seat

        return (row * 8) + seat

    def get_passes(self, lines):
        passes = []

        for boarding_pass in lines:
            passes.append(self.get_seat_id(boarding_pass))

        return passes

    def get_highest_seat_id(self, lines):
        passes = self.get_passes(lines)

        return max(passes)

    def get_my_seat_id(self, lines):
        passes = self.get_passes(lines)

        last_seat = min(passes) - 1

        my_seat_id = 0

        for seat_id in sorted(passes):
            if last_seat != seat_id - 1:
                my_seat_id = last_seat + 1
            last_seat = seat_id

        return my_seat_id

    def part_1(self):
        start_time = time.time()

        res = self.get_highest_seat_id(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_my_seat_id(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
