# puzzle prompt: https://adventofcode.com/2020/day/19

import time
import sys
sys.path.insert(0,"..")

from base.advent import *
from collections import defaultdict
from functools import lru_cache

# i kept it simple, there are only 3 possible rules
# strings "a" or "b"  
# concatenate other rules i.e. numbers -> 8 11
# options, it is always a pair of rules separated by pipe -> 14 3 | 1 12 
class Rules:
    def __init__(self, rule_specs):
        self.rules = defaultdict(list)

        for rule in rule_specs.splitlines():
            rule = rule.split(": ")
            rule_number = rule[0]
            matches = rule[1].split(" | ")
        
            for match in matches:
                if "\"" in match:
                    self.rules[rule_number].append(match.replace("\"", ""))
                else:
                    self.rules[rule_number].append(match.split(" "))

    def match(self, message):
        results = self._match("0", 0, message)
        return any([result == len(message) for result in results])

    @lru_cache
    def _match(self, rule, idx, message):
        if idx == len(message):
            return []
        
        results = []
        
        for rule in self.rules[rule]:
            if type(rule) == str: # "a" or "b"
                if rule == message[idx]:
                    # return the length matched
                    return [idx+1]
                else:
                    return []
            start_idx = [idx]
        
            for sub_rule in rule:
                new_start_idx = []
                for i in start_idx:
                    sub_results = self._match(sub_rule, i, message)
                    new_start_idx.extend(sub_results)
                start_idx = new_start_idx
            results.extend(start_idx)
        
        return results


class Solution(InputAsStringSolution):
    _year = 2020
    _day = 19

    def parse(self, lines):
        data = lines.split("\n\n")
        rule_specs = data[0]
        messages = data[1].splitlines()

        return rule_specs, messages

    def count_match_message(self, rule, messages):
        return sum([rule.match(message) for message in messages])

    def get_matches_rule0(self, lines):
        rule_specs, messages = self.parse(lines)

        rules = Rules(rule_specs)
        
        return self.count_match_message(rules, messages)

    def get_matches_rule0_after_fix(self, lines):
        rule_specs, messages = self.parse(lines)
        
        fixed_rules = rule_specs                                        \
                        .replace("11: 42 31", "11: 42 31 | 42 11 31")   \
                        .replace("8: 42", "8: 42 | 42 8") # fix from the puzzle

        rules = Rules(fixed_rules)

        return self.count_match_message(rules, messages)

    def part_1(self):
        start_time = time.time()

        res = self.get_matches_rule0(self.input)

        end_time = time.time()

        self.solve("1", res, (end_time - start_time))

    def part_2(self):
        start_time = time.time()

        res = self.get_matches_rule0_after_fix(self.input)

        end_time = time.time()

        self.solve("2", res, (end_time - start_time))

if __name__ == "__main__":
    solution = Solution()

    solution.part_1()
    
    solution.part_2()