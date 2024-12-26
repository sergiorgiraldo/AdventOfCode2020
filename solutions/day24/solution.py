# puzzle prompt: https://adventofcode.com/2020/day/24

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from collections import defaultdict
import re


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 24

    neighbourhood = {}

    def neighbours_of(self, position):
        if position in self.neighbourhood:
            return self.neighbourhood[position]

        positions = [
            (position[0] + 1, position[1] + 1),
            (position[0] - 1, position[1] + 1),
            (position[0] - 2, position[1]),
            (position[0] + 2, position[1]),
            (position[0] - 1, position[1] - 1),
            (position[0] + 1, position[1] - 1),
        ]

        self.neighbourhood[position] = positions

        return positions

    def get_black_tiles(self, rows):
        tiles = defaultdict(bool)

        for row in rows:
            pos = (0, 0)
            flips = re.findall(r"se|sw|w|e|nw|ne", row)
            for flip in flips:
                if flip == "se":
                    pos = (pos[0] + 1, pos[1] + 1)
                elif flip == "sw":
                    pos = (pos[0] - 1, pos[1] + 1)
                elif flip == "w":
                    pos = (pos[0] - 2, pos[1])
                elif flip == "e":
                    pos = (pos[0] + 2, pos[1])
                elif flip == "nw":
                    pos = (pos[0] - 1, pos[1] - 1)
                elif flip == "ne":
                    pos = (pos[0] + 1, pos[1] - 1)

            tiles[pos] = not tiles[pos]

        return len([x for x, y in tiles.items() if y]), tiles

    def build_art_piece(self, rows):
        tiles = self.get_black_tiles(rows)[1]

        for _ in range(100):
            new_tiles = {}
            tiles_to_consider = tiles.copy()
            for k in tiles.keys():
                neighbours = self.neighbours_of(k)
                for neighbour in neighbours:
                    if neighbour not in tiles_to_consider:
                        tiles_to_consider[neighbour] = False

            for k, v in tiles_to_consider.items():
                neighbours = self.neighbours_of(k)

                colors = [
                    tiles[neighbour] if neighbour in tiles else False
                    for neighbour in neighbours
                ]

                if v:
                    new_tiles[k] = not (
                        colors.count(True) == 0 or colors.count(True) > 2
                    )
                else:
                    new_tiles[k] = colors.count(True) == 2

            tiles = new_tiles

        return len([x for x, y in tiles.items() if y])

    def part_1(self):
        start_time = time.time()

        res = self.get_black_tiles(self.input)[0]

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.build_art_piece(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
