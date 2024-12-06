#!/bin/env python3
from utils import Day
from collections import deque
import numpy as np


class Day06(Day):
    def __init__(self):
        super().__init__("06")

    def parse(self, input_data):
        self.grid = np.array([list(line) for line in input_data.splitlines()])
        self.grid = np.pad(self.grid, 1, mode='constant', constant_values='@')
        # Find initial position and direction of the guard
        self.guard_pos = np.where(self.grid == '^')
        self.grid[self.guard_pos] = '.'

    def part1(self):
        guard_pos = tuple(x[0] for x in self.guard_pos)
        direction = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
        self.visited1 = set()
        while self.grid[guard_pos] != '@':
            self.visited1.add(guard_pos)
            next_pos = tuple(np.add(guard_pos, direction[0]))
            while self.grid[next_pos] == '#':
                direction.rotate(-1)
                next_pos = tuple(np.add(guard_pos, direction[0]))
            guard_pos = next_pos
        return len(self.visited1)

    def has_loop(self, grid):
        guard_pos = tuple(x[0] for x in self.guard_pos)
        direction = deque([(-1, 0), (0, 1), (1, 0), (0, -1)])
        visited = set()
        while grid[guard_pos] != '@':
            if (guard_pos, direction[0]) in visited:
                return True
            visited.add((guard_pos, direction[0]))
            next_pos = tuple(np.add(guard_pos, direction[0]))
            while grid[next_pos] == '#':
                direction.rotate(-1)
                next_pos = tuple(np.add(guard_pos, direction[0]))
            guard_pos = next_pos
        return False

    def part2(self):
        s = 0
        for i, j in self.visited1:
            if self.grid[i, j] == '.':
                grid = self.grid.copy()
                grid[i, j] = '#'
                if self.has_loop(grid):
                    s += 1
        return s


if __name__ == '__main__':
    Day06().main(example=False)
