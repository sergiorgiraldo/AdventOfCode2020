# puzzle prompt: https://adventofcode.com/2020/day/17

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from collections import defaultdict
from operator import itemgetter as get


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 17

    def parse(self, lines):
        self.space3d = defaultdict(bool)
        self.space4d = defaultdict(bool)

        self.offsets3d = set()
        self.offsets4d = set()

        for x in range(-1, 2):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    for w in range(-1, 2):
                        self.offsets4d.add((x, y, z, w))
                    self.offsets3d.add((x, y, z))

        self.offsets3d.remove((0,) * 3)
        self.offsets4d.remove((0,) * 4)

        for y, line in enumerate(lines):
            for x, char in enumerate(line):
                val = char == "#"
                self.space3d[x, y, 0] = val
                self.space4d[x, y, 0, 0] = val

        self.prev_space3d = self.space3d.copy()
        self.prev_space4d = self.space4d.copy()

    def get_maxes(self, four):
        keys = (self.space4d if four else self.space3d).keys()

        boundaries = [max(keys, key=get(i))[i] + 1 for i in range(3)]

        if four:
            max_w = max(keys, key=get(3))[3] + 1
            boundaries = *boundaries, max_w

        return boundaries

    def get_mins(self, four):
        keys = (self.space4d if four else self.space3d).keys()

        boundaries = [min(keys, key=get(i))[i] for i in range(3)]

        if four:
            min_w = min(keys, key=get(3))[3]
            boundaries = *boundaries, min_w

        return boundaries

    def get_cubes3d(self, x, y, z):
        count = 0

        for offset in self.offsets3d:
            if self.prev_space3d[x + offset[0], y + offset[1], z + offset[2]]:
                count += 1

        return count

    def get_cubes4d(self, x, y, z, w):
        count = 0

        for offset in self.offsets4d:
            if self.prev_space4d[
                x + offset[0], y + offset[1], z + offset[2], w + offset[3]
            ]:
                count += 1

        return count

    def boot_3d(self, lines, maxstep=6):
        self.parse(lines)

        for _ in range(maxstep):
            self.prev_space3d = self.space3d.copy()
            min_x, min_y, min_z = self.get_mins(False)
            max_x, max_y, max_z = self.get_maxes(False)

            for x in range(min_x - 1, max_x + 1):
                for y in range(min_y - 1, max_y + 1):
                    for z in range(min_z - 1, max_z + 1):
                        active = self.prev_space3d[x, y, z]
                        cubes_count = self.get_cubes3d(x, y, z)

                        if active and not cubes_count in (2, 3):
                            self.space3d[x, y, z] = False
                        if not active and cubes_count == 3:
                            self.space3d[x, y, z] = True

        return sum(self.space3d.values())

    def boot_4d(self, lines, maxstep=6):
        self.parse(lines)

        for _ in range(maxstep):
            self.prev_space4d = self.space4d.copy()
            min_x, min_y, min_z, min_w = self.get_mins(True)
            max_x, maxy, max_z, max_w = self.get_maxes(True)

            for x in range(min_x - 1, max_x + 1):
                for y in range(min_y - 1, maxy + 1):
                    for z in range(min_z - 1, max_z + 1):
                        for w in range(min_w - 1, max_w + 1):
                            active = self.prev_space4d[x, y, z, w]
                            cubes_count = self.get_cubes4d(x, y, z, w)

                            if active and not cubes_count in (2, 3):
                                self.space4d[x, y, z, w] = False
                            if not active and cubes_count == 3:
                                self.space4d[x, y, z, w] = True

        return sum(self.space4d.values())

    def part_1(self):
        start_time = time.time()

        res = self.boot_3d(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.boot_4d(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
