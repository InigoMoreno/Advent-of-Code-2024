#!/bin/env python3
import re
from utils import Day


class Day03(Day):
    def __init__(self):
        super().__init__("03")

    def parse(self, input_data):
        self.input = input_data

    def part1(self):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, self.input)
        return sum(int(a) * int(b) for a, b in matches)

    def part2(self):
        pattern = r"(do\(\)|don't\(\)|mul\((\d{1,3}),(\d{1,3})\))"
        matches = re.findall(pattern, self.input)
        enabled = True
        result = 0

        for match in matches:
            if match[0] == "do()":
                enabled = True
            elif match[0] == "don't()":
                enabled = False
            elif enabled:
                result += int(match[1]) * int(match[2])

        return result


if __name__ == '__main__':
    Day03().main(example=False)
