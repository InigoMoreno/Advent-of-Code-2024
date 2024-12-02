#!/bin/env python3
import numpy as np

from utils import Day


class Day02(Day):
    def __init__(self):
        super().__init__("02")

    def parse(self, input_data):
        self.input = [list(map(int, line.split())) for line in input_data.strip().split('\n')]

    def is_safe(self, level):
        diff = np.diff(level)
        return all((d > 0 and d <= 3) for d in diff) or all((d < 0 and d >= -3) for d in diff)

    def part1(self):
        return sum(self.is_safe(level) for level in self.input)

    def part2(self):
        counter = 0
        for level in self.input:
            if self.is_safe(level):
                counter += 1
                continue
            for i in range(len(level)):
                if self.is_safe(level[:i] + level[i + 1:]):
                    counter += 1
                    break
        return counter


if __name__ == '__main__':
    Day02().main(example=False)
