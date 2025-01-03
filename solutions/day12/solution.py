# puzzle prompt: https://adventofcode.com/2020/day/12

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 12

    def parse(self, lines):
        instructions = [(line[0], int(line[1:])) for line in lines]

        return instructions

    def get_distance(self, lines):
        instructions = self.parse(lines)

        # complex numbers rock for manhattan distance :)
        #           North: -1j
        #                |
        #                |
        #   West:-1  ----o----  East:1
        #                |
        #                |
        #           South: 1j

        location_1 = 0 + 0j
        location_2 = 0 + 0j
        direction = 1

        waypoint = 10 - 1j  # 10 east, 1 north, magic number from puzzle

        for instruction in instructions:
            if instruction[0] == "N":
                location_1 -= instruction[1] * 1j
                waypoint -= instruction[1] * 1j

            elif instruction[0] == "S":
                location_1 += instruction[1] * 1j
                waypoint += instruction[1] * 1j

            elif instruction[0] == "W":
                location_1 -= instruction[1]
                waypoint -= instruction[1]

            elif instruction[0] == "E":
                location_1 += instruction[1]
                waypoint += instruction[1]

            elif instruction[0] == "L":
                for _ in range(instruction[1] // 90):
                    direction *= -1j
                    waypoint *= -1j

            elif instruction[0] == "R":
                for _ in range(instruction[1] // 90):
                    direction *= 1j
                    waypoint *= 1j

            elif instruction[0] == "F":
                location_1 += instruction[1] * direction
                location_2 += instruction[1] * waypoint

            else:
                raise Exception(f"Unknown instruction: {instruction[0]}")

        # get manhattan distance, since it is from origin, just add coordinates
        distance_1 = int(abs(location_1.real) + abs(location_1.imag))
        distance_2 = int(abs(location_2.real) + abs(location_2.imag))

        return distance_1, distance_2

    def part_1(self):
        start_time = time.time()

        res = self.get_distance(self.input)[0]

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_distance(self.input)[1]

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
