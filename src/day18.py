#!/bin/env python3
from utils import Day
from astar import find_path
import numpy as np


class Pos(tuple):
    def __add__(self, other):
        return Pos(s + o for s, o in zip(self, other))

    def __sub__(self, other):
        return Pos(s - o for s, o in zip(self, other))


class Day18(Day):
    def __init__(self):
        super().__init__("18")

    def parse(self, input_data):
        self.N = 7 if self.example else 71
        self.grid = np.zeros((self.N, self.N), dtype=int)
        self.blocks = []
        for i, line in enumerate(input_data.splitlines()):
            x, y = map(int, line.split(','))
            self.grid[y, x] = i + 1
            self.blocks.append(Pos((y, x)))

    def part1(self):
        return len(self.astar(12 if self.example else 1024)) - 1

    def astar(self, t):
        grid = (self.grid > 0) & (self.grid <= t)
        grid = np.pad(grid, 1, 'constant', constant_values=1)

        neighbors = [Pos(p) for p in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        res = find_path(
            Pos((1, 1)),
            Pos((self.N, self.N)),
            neighbors_fnct=lambda pos: (pos + n for n in neighbors if not grid[pos + n]),
            heuristic_cost_estimate_fnct=lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1]),
        )
        if res is None:
            return []
        return list(res)

    def part2(self):
        t = 12 if self.example else 1024
        path = self.astar(t)
        while path:
            t += 1
            if self.blocks[t - 1] + Pos((1, 1)) in path:
                path = self.astar(t)

        return f"{self.blocks[t - 1][1]},{self.blocks[t - 1][0]}"


if __name__ == '__main__':
    Day18().main(example=False)
