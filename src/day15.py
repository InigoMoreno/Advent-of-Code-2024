#!/bin/env python3
from utils import Day
import numpy as np

directions = {
    '<': (0, -1),
    '>': (0, 1),
    '^': (-1, 0),
    'v': (1, 0),
}


class Pos(tuple):
    def __add__(self, other):
        return Pos(s + o for s, o in zip(self, other))


class Day15(Day):
    def __init__(self):
        super().__init__("15")

    def parse(self, input_data):
        block1, block2 = input_data.split('\n\n')
        self.grid = np.array([list(line) for line in block1.splitlines()])
        self.initial_position = Pos(np.argwhere(self.grid == '@')[0])
        self.grid[self.initial_position] = '.'
        self.movements = ''.join(block2.split())

    def part1(self):
        pos = self.initial_position
        for movement in self.movements:
            direction = directions[movement]
            next_pos = pos + direction
            box_moved = False
            while self.grid[next_pos] == 'O':
                box_moved = True
                next_pos += direction
            if self.grid[next_pos] == '#':
                continue
            if box_moved:
                self.grid[next_pos], self.grid[pos + direction] = self.grid[pos + direction], self.grid[next_pos]
            pos = pos + direction
        total = 0
        for box in np.argwhere(self.grid == 'O'):
            total += box[0] * 100 + box[1]
        return total

    def part2(self):
        return None


if __name__ == '__main__':
    Day15().main(example=True)
