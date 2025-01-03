# puzzle prompt: https://adventofcode.com/2020/day/13

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from math import gcd


class Solution(InputAsLinesSolution):
    _year = 2020
    _day = 13

    def parse(self, lines):
        input = [line.strip() for line in lines]

        time_to_leave = int(input[0])
        buses = input[1].split(",")

        return time_to_leave, buses

    def get_shuttle_bus(self, lines):
        time_to_leave, buses = self.parse(lines)

        buses_in_service = []
        wait_times = []

        for i in range(len(buses)):
            bus = buses[i]
            if bus == "x":
                continue

            interval = int(bus)
            departures = int(time_to_leave / interval)
            next_bus = (departures + 1) * interval  # next bus after my time to leave
            wait_time = next_bus - time_to_leave
            buses_in_service.append(interval)
            wait_times.append(wait_time)

        my_bus = wait_times.index(min(wait_times))

        return buses_in_service[my_bus] * wait_times[my_bus]

    # we need to find a number such that the remainders of all the buses are consecutive after N departures
    # suppose we have 3 buses: 3, 5, 7. After N departures, from perspective of the third bus, time elapsed is 7N
    # from 2nd bus perspective, to win the gold coin, it left at 7N - 1, so the remainder of 7N divided by 5 is 1
    # from 1st bus perspective, to win the gold coin, it left at 7N - 2, so the remainder of 7N divided by 3 is 2

    # from the example, bus 19 leaves at t=1068788 -> 56252 * 19
    #                   bus 31 leaves at t=1068787 -> 34477 * 31 + 1 (1068788 / 31 gives remainder 1)
    #                   bus 59 leaves at t=1068786 -> 18115 * 59 + 2 (1068788 / 59 gives remainder 2)

    # the **Chinese remainder theorem** states that if one knows the remainders of the Euclidean division of
    # an integer n by several integers, then one can determine uniquely the remainder of the division of n by
    # the product of these integers, under the condition that the divisors are pairwise coprime (no two divisors
    # share a common factor other than 1).
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem

    # for the algorithm below to find the solution, refer to these
    # https://www.math.cmu.edu/~mradclif/teaching/127S19/Notes/ChineseRemainderTheorem.pdf
    # https://www.youtube.com/watch?v=ru7mWZJlRQg

    def coprime(self, n):
        coprimes = 0
        for i in range(1, n + 1):
            if gcd(n, i) == 1:
                coprimes += 1
        return coprimes

    def win_gold_coin(self, lines):
        _, buses = self.parse(lines)

        buses_in_service = []
        offsets = []

        for i in range(len(buses)):
            bus = buses[i]
            if bus != "x":
                buses_in_service.append(int(bus))
                offsets.append(i)

        buses_product = 1

        for bus in buses_in_service:
            buses_product *= bus

        sum = 0

        for i in range(len(buses_in_service)):
            bus = buses_in_service[i]
            remainder = (bus - offsets[i]) % bus
            b = int(buses_product / bus) ** (self.coprime(bus) - 1) % bus
            sum += b * remainder * int(buses_product / bus)

        return sum % buses_product

    def part_1(self):
        start_time = time.time()

        res = self.get_shuttle_bus(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.win_gold_coin(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
