import unittest

from solution import Solution

solution = Solution()


class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "..##.........##.........##.........##.........##.........##.......",
            "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
            ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
            "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
            ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
            "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
            ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
            ".#........#.#........#.#........#.#........#.#........#.#........#",
            "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
            "#...##....##...##....##...##....##...##....##...##....##...##....#",
            ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#",
        ]
        self.assertEqual(solution.find_trees_single(list, 3, 1), 7, "Oops")

    def test_part2(self):
        list = [
            "..##.........##.........##.........##.........##.........##.......",
            "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
            ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
            "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
            ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
            "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
            ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
            ".#........#.#........#.#........#.#........#.#........#.#........#",
            "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
            "#...##....##...##....##...##....##...##....##...##....##...##....#",
            ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#",
        ]
        self.assertEqual(solution.find_trees_multiple(list), 336, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")


if __name__ == "__main__":
    unittest.main()
