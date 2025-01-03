# puzzle prompt: https://adventofcode.com/2020/day/14

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from abc import ABC, abstractmethod
from typing import final

SIZE = 36


class DockingProgram(ABC):
    def __init__(self, instructions):
        self.mask_string = None
        self.memory = {}
        self.instructions = instructions

    @abstractmethod
    def mask_bit(self, mask, bit):
        pass

    @abstractmethod
    def write(self, mem_addr, value):
        pass

    @final
    def mask(self, value):
        if self.mask_string is None:
            return value

        masked_value = ""
        value = bin(value)[2:]

        if len(value) < SIZE:
            value = "0" * (SIZE - len(value)) + value

        for mask, bit in zip(self.mask_string, value):
            masked_value += self.mask_bit(mask, bit)

        return masked_value

    @final
    def run(self):
        for instruction in self.instructions:
            if instruction.startswith("mask"):
                # Ignore the `mask = ` part in the instruction
                self.mask_string = instruction[7:]
            else:
                parts = instruction.split(" = ")
                start_index = parts[0].find("[") + 1
                mem_addr = int(parts[0][start_index:-1])
                value = int(parts[1])
                self.write(mem_addr, value)

    @property
    @final
    def memory_status(self):
        return sum(self.memory.values())


class DockingProgram_V1(DockingProgram):
    def mask_bit(self, mask, bit):
        return bit if mask == "X" else mask

    def write(self, mem_addr, value):
        masked_value = self.mask(value)
        self.memory[mem_addr] = int(masked_value, 2)


class DockingProgram_V2(DockingProgram):
    def mask_bit(self, mask, bit):
        return bit if mask == "0" else mask

    def write(self, mem_addr, value):
        def helper(masked_addr):
            if "X" not in masked_addr:
                addr = int(masked_addr, 2)
                self.memory[addr] = value
            else:
                index = masked_addr.find("X")
                helper(masked_addr[:index] + "1" + masked_addr[index + 1 :])
                helper(masked_addr[:index] + "0" + masked_addr[index + 1 :])

        masked_addr = self.mask(mem_addr)

        helper(masked_addr)


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 14

    def get_memory_v1(self, instructions):
        program = DockingProgram_V1(instructions)

        program.run()

        return program.memory_status

    def get_memory_v2(self, instructions):
        program = DockingProgram_V2(instructions)

        program.run()

        return program.memory_status

    def part_1(self):
        start_time = time.time()

        res = self.get_memory_v1(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_memory_v2(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
