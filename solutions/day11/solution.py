# puzzle prompt: https://adventofcode.com/2020/day/11

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class SeatMap:
    # o o o
    # o | o
    # o o o
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    def __init__(self, layout):
        self.layout_original = [[ch for ch in row] for row in layout]

    def check_valid_position(self, row, col):
        return (
            row >= 0
            and row < len(self.layout)
            and col >= 0
            and col < len(self.layout[0])
        )

    def check_occupied(self, row: int, col: int, direction, first_visible):
        row += direction[0]
        col += direction[1]

        if self.check_valid_position(row, col):
            if self.layout[row][col] == "#":
                return True
            if self.layout[row][col] == "." and first_visible:
                return self.check_occupied(row, col, direction, first_visible)

        return False

    def count_occupied_around(self, row, col, first_visible):
        cnt = 0

        for direction in self.directions:
            if self.check_occupied(row, col, direction, first_visible):
                cnt += 1

        return cnt

    def count_occupied_seats(self, first_visible=False, rule=4):
        self.layout = [[ch for ch in row] for row in self.layout_original]
        new_layout = [[ch for ch in row] for row in self.layout]

        is_changing = True

        while is_changing:
            is_changing = False

            for i in range(len(self.layout)):
                for j in range(len(self.layout[0])):
                    if self.layout[i][j] == ".":
                        continue

                    occupied_around = self.count_occupied_around(i, j, first_visible)

                    if self.layout[i][j] == "L" and occupied_around == 0:
                        new_layout[i][j] = "#"
                        is_changing = True
                    elif self.layout[i][j] == "#" and occupied_around >= rule:
                        new_layout[i][j] = "L"
                        is_changing = True
                    else:
                        new_layout[i][j] = self.layout[i][j]

            new_layout, self.layout = self.layout, new_layout

        return sum([sum([i == "#" for i in row]) for row in self.layout])


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 11

    def get_occupied_seats(self, lines):
        seatMap = SeatMap(lines)

        return seatMap.count_occupied_seats()

    def get_occupied_seats_in_sight(self, lines):
        seatMap = SeatMap(lines)

        return seatMap.count_occupied_seats(True, 5)

    def part_1(self):
        start_time = time.time()

        res = self.get_occupied_seats(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_occupied_seats_in_sight(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
