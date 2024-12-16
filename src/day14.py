#!/bin/env python3
from utils import Day
import numpy as np
from collections import Counter
import math


class Day14(Day):
    def __init__(self):
        super().__init__("14")

    def parse(self, input_data):
        self.input = np.array([
            tuple(tuple(map(int, part[2:].split(',')))
                  for part in line.split(" "))
            for line in input_data.splitlines()
        ])
        self.shape = np.array((np.max(self.input[:, 0, 0]), np.max(self.input[:, 0, 1]))) + 1

    def quadrant(self, position):
        rel_pos = position / (self.shape - 1)
        if any(rel_pos == 0.5):
            return None
        return (rel_pos[0] < .5, rel_pos[1] < .5)

    def part1(self):
        T = 100
        future_positions = np.mod(self.input[:, 0, :] + self.input[:, 1, :] * T, self.shape)
        quadrant_counts = Counter(list(map(self.quadrant, future_positions)))
        return math.prod([c for q, c in quadrant_counts.items() if q])

    def part2(self):
        with open('day14_output.txt', 'w') as f:
            for t in range(10000):
                if (t % self.shape[0] == 11) and (t % self.shape[1] == 65):
                    # values found by seeing a repeating pattern where sometimes all robots
                    # would be mosly in a horizontal line or vertical line
                    f.write(f"\n\n{t}\n")
                    positions = np.mod(self.input[:, 0, :] + self.input[:, 1, :] * t, self.shape)
                    c = Counter(list(map(tuple, positions)))
                    for j in range(self.shape[1]):
                        for i in range(self.shape[0]):
                            f.write(str(c[(i, j)]) if c[(i, j)] else '.')
                        f.write('\n')
                return t


if __name__ == '__main__':
    Day14().main(example=False)
