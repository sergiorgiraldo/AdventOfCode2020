import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
            "trh fvjkl sbzzf mxmxvkd (contains dairy)",
            "sqjhc fvjkl (contains soy)",
            "sqjhc mxmxvkd sbzzf (contains fish)",
        ]
        self.assertEqual(solution.get_safe_ingredients(list)[0], 5, "Oops")

    def test_part2(self):
        list = [
            "mxmxvkd kfcds sqjhc nhms (contains dairy, fish)",
            "trh fvjkl sbzzf mxmxvkd (contains dairy)",
            "sqjhc fvjkl (contains soy)",
            "sqjhc mxmxvkd sbzzf (contains fish)",
        ]
        self.assertEqual(
            solution.get_unsafe_ingredients(list), "mxmxvkd,sqjhc,fvjkl", "Oops"
        )

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
