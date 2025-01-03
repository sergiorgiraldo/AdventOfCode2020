# puzzle prompt: https://adventofcode.com/2020/day/16

import time
import sys

sys.path.insert(0, "..")

from base.advent import *
from collections import defaultdict


class FieldRule:
    def __init__(self, rule: str):
        rule = rule.split(" or ")
        self.first_range = self._read_range(rule[0])
        self.second_range = self._read_range(rule[1])

    def _read_range(self, range):
        range = range.split("-")
        return int(range[0]), int(range[1])

    def validate(self, value):
        return (
            self.first_range[0] <= value <= self.first_range[1]
            or self.second_range[0] <= value <= self.second_range[1]
        )


class TicketRule:
    def __init__(self, rules: str):
        self.rules = {}
        self.rule_index = {}
        self.valid_tickets = []
        for rule in rules.splitlines():
            self.set_rule(rule)

    def set_rule(self, rule):
        parts = rule.split(": ")
        field = parts[0]
        self.rules[field] = FieldRule(parts[1])

    def _validate_value(self, value):
        return any(map(lambda rule: rule.validate(value), self.rules.values()))

    def count_invalid(self, ticket):
        invalid = 0
        valid = True
        for value in ticket:
            if not self._validate_value(value):
                valid = False
                invalid += value
        if valid:
            self.valid_tickets.append(ticket)
        return invalid

    def validate_rule(self, field, ticket_idx):
        rule: FieldRule = self.rules[field]
        for ticket in self.valid_tickets:
            if not rule.validate(ticket[ticket_idx]):
                return False
        return True

    def detect_index(self):
        # Find the possible indices for each field
        possile_idx = defaultdict(list)
        for field in self.rules:
            for i in range(len(self.rules)):
                if self.validate_rule(field, i):
                    possile_idx[field].append(i)

        # Sort by len of possible choices to help find faster.
        possible_idx_len = [(len(possile_idx[field]), field) for field in self.rules]
        possible_idx_len.sort()

        used_indices = [False] * len(self.rules)

        def helper(field_idx):
            if field_idx == len(self.rules):
                return True

            field = possible_idx_len[field_idx][1]
            for idx in possile_idx[field]:
                if not used_indices[idx]:
                    used_indices[idx] = True
                    if helper(field_idx + 1):
                        self.rule_index[field] = idx
                        return True
                    used_indices[idx] = False

        helper(0)


class Solution(InputAsStringSolution):
    _year = 2020
    _day = 16

    def parse(self, lines):
        parts = lines.split("\n\n")
        rule = TicketRule(parts[0])

        my_ticket = parts[1].splitlines()[1]
        my_ticket = [int(value) for value in my_ticket.split(",")]

        nearby_tickets = parts[2].splitlines()[1:]
        nearby_tickets = [
            [int(value) for value in ticket.split(",")] for ticket in nearby_tickets
        ]

        return rule, my_ticket, nearby_tickets

    def get_error_rate(self, lines):
        rule, _, nearby_tickets = self.parse(lines)

        error_rate = sum([rule.count_invalid(ticket) for ticket in nearby_tickets])

        return rule, error_rate

    def determine_my_ticket(self, lines):
        _, my_ticket, _ = self.parse(lines)

        rule = self.get_error_rate(lines)[0]  # get rid of invalid tickets

        rule.detect_index()
        indices = []
        for field in rule.rules:
            if "departure" in field:
                indices.append(rule.rule_index[field])

        result = 1
        for idx in indices:
            result *= my_ticket[idx]

        return rule, result

    def part_1(self):
        start_time = time.time()

        res = self.get_error_rate(self.input)[1]

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.determine_my_ticket(self.input)[1]

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))


if __name__ == "__main__":
    solution = Solution()

    solution.part_1()

    solution.part_2()
