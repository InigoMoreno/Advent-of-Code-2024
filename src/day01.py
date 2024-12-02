#!/bin/env python3
from collections import Counter

from utils import Day


class Day01(Day):
    def __init__(self):
        super().__init__("01")

    def parse(self, input_data):
        self.a = []
        self.b = []
        for line in input_data.split("\n"):
            # print(line)
            a, b = line.split("   ")
            self.a.append(int(a))
            self.b.append(int(b))

    def part1(self):
        diff = 0
        for a, b in zip(sorted(self.a), sorted(self.b)):
            diff += abs(a - b)
        return diff

    def part2(self):
        simm = 0
        counter = Counter(self.b)
        for a in self.a:
            simm += a * counter[a]
        return simm


if __name__ == '__main__':
    Day01().main(example=False)
