#!/bin/env python3
from utils import Day
import math
import numpy as np


def close_to_int(a, sigma=1e-8):
    remainder = math.modf(a + .5)[0] - .5
    return abs(remainder) < sigma


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
        A = np.matrix([[ax, bx], [ay, by]])
        B = np.matrix([[x], [y]])
        Na, Nb = np.linalg.solve(A, B).flat
        if close_to_int(Na) and close_to_int(Nb):
            return round(Na * 3 + Nb)
        return 0

    def part1(self):
        return sum(self.solve(ax, ay, bx, by, x, y) for (ax, ay), (bx, by), (x, y) in self.machines)

    def part2(self):
        return sum(self.solve(ax, ay, bx, by, x + 10000000000000, y + 10000000000000)
                   for (ax, ay), (bx, by), (x, y) in self.machines)


if __name__ == '__main__':
    Day13().main(example=False)
