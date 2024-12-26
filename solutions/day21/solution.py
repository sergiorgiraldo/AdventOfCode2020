# puzzle prompt: https://adventofcode.com/2020/day/21

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from collections import Counter


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 21

    def get_safe_ingredients(self, lines):
        allergen_suspects = dict()
        ingredient_occurrences = Counter()

        for line in lines:
            left, right = line.split(" (contains ")
            ingredients = set(left.split())
            allergens = set(right[:-1].split(", "))

            for allergen in allergens:
                if allergen not in allergen_suspects:
                    allergen_suspects[allergen] = ingredients.copy()
                else:
                    allergen_suspects[allergen] &= ingredients

            for ingredient in ingredients:
                ingredient_occurrences[ingredient] += 1

        return (
            sum(
                n
                for i, n in ingredient_occurrences.items()
                if all(i not in suspects for suspects in allergen_suspects.values())
            ),
            allergen_suspects,
        )

    def get_unsafe_ingredients(self, lines):
        allergen_suspects = self.get_safe_ingredients(lines)[1]
        allergen_confirmed = dict()

        while len(allergen_confirmed) < len(allergen_suspects):
            for allergen, suspects in allergen_suspects.items():
                if allergen not in allergen_confirmed:
                    if len(suspects) == 1:
                        allergen_confirmed[allergen] = next(iter(suspects))
                    else:
                        suspects -= set(allergen_confirmed.values())

        unsafe_ingredients = [
            allergen_confirmed[allergen]
            for allergen in sorted(allergen_confirmed.keys())
        ]

        return ",".join(unsafe_ingredients)

    def part_1(self):
        start_time = time.time()

        res = self.get_safe_ingredients(self.input)[0]

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_unsafe_ingredients(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
