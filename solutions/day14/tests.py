import unittest

from solution import Solution

solution = Solution()

class Tests(unittest.TestCase):
    def test_part1(self):
        list = [
            "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
            "mem[8] = 11",
            "mem[7] = 101",
            "mem[8] = 0"
        ]
        self.assertEqual(solution.get_memory_v1(list), 165, "Oops")

    def test_part2(self):
        list = [
            "mask = 000000000000000000000000000000X1001X",
            "mem[42] = 100",
            "mask = 00000000000000000000000000000000X0XX",
            "mem[26] = 1"
        ]
        self.assertEqual(solution.get_memory_v2(list), 208, "Oops")

    def test_sanity_check(self):
        self.assertEqual(1 + 1, 2, "Oops")

if __name__ == "__main__":
    unittest.main()