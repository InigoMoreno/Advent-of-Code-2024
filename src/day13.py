#!/bin/env python3
from utils import Day
import math


class Day13(Day):
    def __init__(self):
        super().__init__("13")

    def parse(self, input_data):
        self.machines = [
            tuple(
                tuple(map(lambda x: int(x[2:]), line.split(': ')[1].split(', ')))
                for line in block.split('\n')
            )
            for block in input_data.strip().split('\n\n')
        ]

    def solve(self, ax, ay, bx, by, x, y):
        smallest_tokens = math.inf
        for Na in range(0, x // ax + 1):
            Nbx, modx = divmod(x - ax * Na, bx)
            if modx != 0:
                continue
            Nby, mody = divmod(y - ay * Na, by)
            if mody != 0 or Nbx != Nby:
                continue
            tokens = Na * 3 + Nbx
            if tokens < smallest_tokens:
                smallest_tokens = tokens
        if smallest_tokens < math.inf:
            return smallest_tokens
        return 0

    def part1(self):
        return sum(self.solve(ax, ay, bx, by, x, y) for (ax, ay), (bx, by), (x, y) in self.machines)

    def part2(self):
        return sum(self.solve(ax, ay, bx, by, x + 10000000000000, y + 10000000000000)
                   for (ax, ay), (bx, by), (x, y) in self.machines)


if __name__ == '__main__':
    Day13().main(example=False)
