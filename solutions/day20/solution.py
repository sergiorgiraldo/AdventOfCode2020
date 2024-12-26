# puzzle prompt: https://adventofcode.com/2020/day/20

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from enum import Enum
from collections import defaultdict


class Border(Enum):
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3


class Movement:
    def rotate(image):
        new_image = []
        n = len(image)
        for i in range(n):
            new_row = ""
            for j in range(n):
                new_row += image[j][n - 1 - i]
            new_image.append(new_row)
        return new_image

    def flip(image):
        return [row[::-1] for row in image]


class Tile:
    def __init__(self, tile_info):
        tile_info = tile_info.splitlines()
        self.tile_id = int(tile_info[0][5:-1])
        self.tile = tile_info[1:]
        self.borders = set()
        # top border
        self.borders.add(tile_info[1])
        self.borders.add(tile_info[1][::-1])
        # right border
        right_border = "".join([row[-1] for row in tile_info[1:]])
        self.borders.add(right_border)
        self.borders.add(right_border[::-1])
        # bottom border
        self.borders.add(tile_info[-1])
        self.borders.add(tile_info[-1][::-1])
        # left border
        left_border = "".join([row[0] for row in tile_info[1:]])
        self.borders.add(left_border)
        self.borders.add(left_border[::-1])

    def is_neighbor(self, other):
        if other.tile_id == self.tile_id:
            # Same tile
            return False
        return len(self.borders.intersection(other.borders)) > 0

    def get_border(self, border):
        if border == Border.TOP:
            return self.tile[0]
        if border == Border.BOTTOM:
            return self.tile[-1]
        if border == Border.LEFT:
            index = 0
        else:
            index = -1
        return "".join([row[index] for row in self.tile])

    def match_border(self, other, border):
        border = self.get_border(border)
        return len(other.borders.intersection(set([border]))) > 0

    def rotate(self):
        self.tile = Movement.rotate(self.tile)

    def flip(self):
        self.tile = Movement.flip(self.tile)

    def _adapt_rotate(self, edge, border):
        for _ in range(4):
            if edge == self.get_border(border):
                return True
            self.rotate()
        return False

    def adapt(self, edge, border):
        if self._adapt_rotate(edge, border):
            return
        self.flip()
        self._adapt_rotate(edge, border)

    def tile_without_borders(self):
        return [row[1:-1] for row in self.tile[1:-1]]

    def _is_top_left(self, right_neighbor, bottom_neighbor):
        return self.match_border(right_neighbor, Border.RIGHT) and self.match_border(
            bottom_neighbor, Border.BOTTOM
        )

    def is_top_left(self, neighbor_0, neighbor_1):
        for _ in range(4):
            if self._is_top_left(neighbor_0, neighbor_1) or self._is_top_left(
                neighbor_1, neighbor_0
            ):
                return True
            self.rotate()
        self.flip()
        for _ in range(4):
            if self._is_top_left(neighbor_0, neighbor_1) or self._is_top_left(
                neighbor_1, neighbor_0
            ):
                return True
            self.rotate()
        return False


class Monster:
    # from the puzzle, this is the image from a monster
    #              11111111112
    #    012345678901234567890
    # -1                    #
    # 0  #    ##    ##    ###
    # 1   #  #  #  #  #  #

    monster_relative_position = [
        (0, 0),
        (1, 1),
        (1, 4),
        (0, 5),
        (0, 6),
        (1, 7),
        (1, 10),
        (0, 11),
        (0, 12),
        (1, 13),
        (1, 16),
        (0, 17),
        (-1, 18),
        (0, 18),
        (0, 19),
    ]

    def is_monster_body(image, row, col):
        return (
            0 <= row < len(image)
            and 0 <= col < len(image[row])
            and image[row][col] == "#"
        )

    def is_monster_here(image, row, col):
        return all(
            map(
                lambda offset: Monster.is_monster_body(
                    image, row + offset[0], col + offset[1]
                ),
                Monster.monster_relative_position,
            )
        )

    def count_monsters(image):
        monsters = 0

        for i in range(len(image)):
            for j in range(len(image[0])):
                monsters += 1 if Monster.is_monster_here(image, i, j) else 0

        return monsters

    def count_safe_position(image):
        total_hash = sum([row.count("#") for row in image])
        for _ in range(4):
            monsters = Monster.count_monsters(image)
            if monsters != 0:
                return total_hash - monsters * len(Monster.monster_relative_position)
            image = Movement.rotate(image)

        image = Movement.flip(image)
        for _ in range(4):
            monsters = Monster.count_monsters(image)
            if monsters != 0:
                return total_hash - monsters * len(Monster.monster_relative_position)
            image = Movement.rotate(image)
        return total_hash

    def get_roughness(image):
        return Monster.count_safe_position(image)


class Arrangement:
    def __init__(self, tiles):
        tiles = [Tile(tile) for tile in tiles]
        self.tiles = {tile.tile_id: tile for tile in tiles}
        self.neighbors = defaultdict(list)

        for tile in self.tiles.values():
            for other in self.tiles.values():
                if tile.is_neighbor(other):
                    self.neighbors[tile.tile_id].append(other.tile_id)

    def _is_top_left_tile(self, tile_id):
        tile = self.tiles[tile_id]
        neighbor_0 = self.tiles[self.neighbors[tile_id][0]]
        neighbor_1 = self.tiles[self.neighbors[tile_id][1]]
        return tile.is_top_left(neighbor_0, neighbor_1)

    def _find_top_left_tile(self):
        for tile_id in self.corners:
            if self._is_top_left_tile(tile_id):
                return tile_id

        raise Exception("Should not reach this point")

    def _find_next_tile(self, current_id, match_border, adapt_border):
        current_tile = self.tiles[current_id]
        neighbors = self.neighbors[current_id]
        for neighbor_id in neighbors:
            neighbor = self.tiles[neighbor_id]
            if current_tile.match_border(neighbor, match_border):
                neighbor.adapt(current_tile.get_border(match_border), adapt_border)
                return neighbor_id
        return None

    def _construct_row(self, first_tile_in_row):
        current_id = first_tile_in_row
        row = []
        while current_id:
            current_tile = self.tiles[current_id]
            row.append(current_tile)
            current_id = self._find_next_tile(current_id, Border.RIGHT, Border.LEFT)

        self.image_tiles.append(row)
        return self._find_next_tile(row[0].tile_id, Border.BOTTOM, Border.TOP)

    def _construct_image_tiles(self):
        self.image_tiles = []
        first_tile_id = self._find_top_left_tile()
        while first_tile_id:
            first_tile_id = self._construct_row(first_tile_id)

    def line_adjacent_borders(self):
        self.corners = []
        result = 1
        for tile_id, neighbors in self.neighbors.items():
            if len(neighbors) == 2:
                result *= tile_id
                self.corners.append(tile_id)

        return result

    def construct_image(self):
        self._construct_image_tiles()
        image_without_borders = []
        for tiles in self.image_tiles:
            tiles_without_borders = [tile.tile_without_borders() for tile in tiles]
            tiles_without_borders_concatenated = []
            for i in range(len(tiles_without_borders[0])):
                row = ""
                for j in range(len(tiles_without_borders)):
                    row += tiles_without_borders[j][i]
                tiles_without_borders_concatenated.append(row)
            image_without_borders.extend(tiles_without_borders_concatenated)
        self.image_without_borders = image_without_borders


class Solution(InputAsStringSolution):
    _year = 2020
    _day = 20

    def assemble_image(self, lines):
        tiles = lines.split("\n\n")

        arrangement = Arrangement(tiles)

        return arrangement.line_adjacent_borders()

    def check_monsters(self, lines):
        tiles = lines.split("\n\n")

        arrangement = Arrangement(tiles)
        arrangement.line_adjacent_borders()
        arrangement.construct_image()

        return Monster.get_roughness(arrangement.image_without_borders)

    def part_1(self):
        start_time = time.time()

        res = self.assemble_image(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.check_monsters(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
