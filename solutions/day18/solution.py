# puzzle prompt: https://adventofcode.com/2020/day/18

import time
import sys

sys.path.insert(0, "..")

from base.advent import *


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 18

    def perform_operation(self, num_stack, operation):
        if operation == "":
            return
        a = num_stack.pop()
        b = num_stack.pop()

        if operation == "+":
            result = a + b
        else:
            result = a * b

        num_stack.append(result)

    def calculate_with_parentheses(self, expr, advanced):
        opens: int = 0
        open_start: int = -1

        for i, c in enumerate(expr):
            if c == "(":
                opens += 1
                if open_start == -1:
                    open_start = i
            elif c == ")":
                opens -= 1
                if opens == 0:
                    # Calculate the expression inside parentheses first
                    # then create calculate a new expression with the stuff
                    # inside parentheses replaced by its result
                    value = self.evaluate(expr[open_start + 1 : i], advanced)
                    return self.evaluate(
                        expr[:open_start] + str(value) + expr[i + 1 :], advanced
                    )

    def calculate_without_parentheses(self, expr, advanced):
        curr_num = ""
        curr_operation = ""
        num_stack = []
        operation_stack = []

        for c in expr:
            if c.isdigit():
                curr_num += c
            else:
                if curr_num != "":
                    num_stack.append(int(curr_num))
                curr_num = ""

                if not advanced or curr_operation == "+":
                    self.perform_operation(num_stack, curr_operation)
                elif advanced:
                    operation_stack.append(curr_operation)
                curr_operation = c

        if curr_num != "":
            num_stack.append(int(curr_num))
        operation_stack.append(curr_operation)
        while len(operation_stack) != 0:
            self.perform_operation(num_stack, operation_stack.pop())

        return num_stack[0]

    def evaluate(self, expr, advanced=False):
        expr = expr.replace(" ", "")

        if "(" in expr:
            return self.calculate_with_parentheses(expr, advanced)
        else:
            return self.calculate_without_parentheses(expr, advanced)

    def part_1(self):
        start_time = time.time()

        res = sum([self.evaluate(expression) for expression in self.input])

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = sum([self.evaluate(expression, True) for expression in self.input])

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
