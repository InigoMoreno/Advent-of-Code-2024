#!/bin/env python3
from utils import Day
from tqdm import tqdm
from functools import cache

class Day19(Day):
    def __init__(self):
        super().__init__("19")

    def parse(self, input_data):
        block1, block2 = input_data.split('\n\n')
        self.patterns = list(block1.split(', '))
        self.designs = list(block2.splitlines())

    @cache
    def is_design_possible(self, design):
        if len(design) == 0:
            return True
        for pattern in self.patterns:
            if design.startswith(pattern):
                rest = design[len(pattern):]
                if self.is_design_possible(rest):
                    return True
        return False

    def part1(self):
        res = sum(self.is_design_possible(design) for design in self.designs)
        # print(self.is_design_possible.cache_info())
        return res

    @cache
    def count_possible_ways(self, design):
        if len(design) == 0:
            return 1
        possible = 0
        for pattern in self.patterns:
            if design.startswith(pattern):
                rest = design[len(pattern):]
                possible += self.count_possible_ways(rest)
        return possible

    def part2(self):
        res = sum(self.count_possible_ways(design) for design in self.designs)
        # print(self.count_possible_ways.cache_info())
        return res


if __name__ == '__main__':
    Day19().main(example=False)
