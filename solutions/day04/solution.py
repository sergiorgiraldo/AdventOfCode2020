# puzzle prompt: https://adventofcode.com/2020/day/4

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
import re


class Solution(InputAsStringSolution):
    _year = 2020
    _day = 4

    def parse(self, lines):
        entries = lines.split("\n\n")
        passports = []
        for entry in entries:
            passport = {}
            for e in entry.replace("\n", " ").split(" "):
                k, v = e.split(":")
                passport[k] = v
            passports.append(passport)

        return passports

    def check_byr(self, field):
        return 1920 <= int(field) <= 2002

    def check_iyr(self, field):
        return 2010 <= int(field) <= 2020

    def check_eyr(self, field):
        return 2020 <= int(field) <= 2030

    def check_hgt(self, field):
        match = re.match(r"^([0-9]+)(cm|in)$", field)
        if match:
            groups = match.groups()
            return (groups[1] == "cm" and 150 <= int(groups[0]) <= 193) or (
                groups[1] == "in" and 59 <= int(groups[0]) <= 76
            )

    def check_hcl(self, field):
        return re.match(r"^#[0-9a-f]{6}$", field)

    def check_pid(self, field):
        return re.match(r"^[0-9]{9}$", field)

    def check_ecl(self, field):
        return field in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def has_required_fields(self, passport):
        return all(
            key in passport for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
        )

    def check_passports_loose(self, lines):
        valids = 0

        passports = self.parse(lines)

        for passport in passports:
            if self.has_required_fields(passport):
                valids += 1

        return valids

    def check_passports_strict(self, lines):
        valids = 0

        passports = self.parse(lines)

        for passport in passports:
            if self.has_required_fields(passport):
                if all(
                    (
                        self.check_byr(passport["byr"]),
                        self.check_iyr(passport["iyr"]),
                        self.check_eyr(passport["eyr"]),
                        self.check_hgt(passport["hgt"]),
                        self.check_hcl(passport["hcl"]),
                        self.check_ecl(passport["ecl"]),
                        self.check_pid(passport["pid"]),
                    )
                ):
                    valids += 1

        return valids

    def part_1(self):
        start_time = time.time()

        res = self.check_passports_loose(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.check_passports_strict(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
