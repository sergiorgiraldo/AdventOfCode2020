# puzzle prompt: https://adventofcode.com/2020/day/8

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 8

    # simple computer, i dont bother write an interpreter
    def run(self, program):
        acc, ip, offset = 0, 0, 1

        visited = {}

        while True:
            if ip >= len(program):
                return "fixed", acc
            if ip in visited:
                return "loop", acc
            visited[ip] = True

            instruction = program[ip]
            offset = 1

            # nop instruction just increase the instruction pointer by 1
            if instruction.startswith("acc"):
                increment = int(instruction.split("acc")[1])
                acc += increment
            elif instruction.startswith("jmp"):
                offset = int(instruction.split("jmp")[1])

            ip += offset

    def get_accumulator_before_loop(self, program):
        return self.run(program)[1]

    def get_accumulator_after_fix(self, program):
        for instruction in range(len(program)):
            new_program = program.copy()

            if program[instruction].startswith("nop"):
                new_program[instruction] = program[instruction].replace("nop", "jmp")
            elif program[instruction].startswith("jmp"):
                new_program[instruction] = program[instruction].replace("jmp", "nop")

            result = self.run(new_program)

            if result[0] == "fixed":
                return result[1]

    def part_1(self):
        start_time = time.time()

        res = self.get_accumulator_before_loop(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_accumulator_after_fix(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
