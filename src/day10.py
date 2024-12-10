#!/bin/env python3
from utils import Day
import numpy as np


class Day10(Day):
    def __init__(self):
        super().__init__("10")

    def parse(self, input_data):
        self.map = np.matrix([list(map(int, line.strip())) for line in input_data.strip().splitlines()])
        self.map = np.pad(self.map, 1, mode='constant', constant_values=-1)

    def explore1(self, pos):
        if self.map[pos] == 9:
            return {pos}
        reachable_ends = set()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            next_pos = (pos[0] + dx, pos[1] + dy)
            if self.map[next_pos] - self.map[pos] == 1:
                reachable_ends.update(self.explore1(next_pos))
        return reachable_ends

    def part1(self):
        total = 0
        for start_pos in np.argwhere(self.map == 0):
            reachable_ends = self.explore1(tuple(start_pos))
            total += len(reachable_ends)
        return total

    def explore2(self, pos, visited=[]):
        next_visited = visited + [pos]
        if self.map[pos] == 9:
            return {tuple(next_visited)}
        distinct_trails = set()
        for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            next_pos = (pos[0] + dx, pos[1] + dy)
            if self.map[next_pos] - self.map[pos] == 1:
                distinct_trails.update(self.explore2(next_pos, next_visited))
        return distinct_trails

    def part2(self):
        total = 0
        for start_pos in np.argwhere(self.map == 0):
            reachable_ends = self.explore2(tuple(start_pos))
            total += len(reachable_ends)
        return total


if __name__ == '__main__':
    Day10().main(example=False)
