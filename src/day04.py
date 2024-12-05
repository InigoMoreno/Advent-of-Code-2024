#!/bin/env python3
import numpy as np
from utils import Day


class Day04(Day):
    def __init__(self):
        super().__init__("04")
        self.padding = 3

    def parse(self, input_data):
        grid = [list(line) for line in input_data.strip().split('\n')]
        padded_grid = np.pad(grid, pad_width=self.padding, mode='constant', constant_values='.')
        self.grid = np.array(padded_grid)
        self.rows = range(self.padding, self.grid.shape[0] - self.padding)
        self.cols = range(self.padding, self.grid.shape[1] - self.padding)

    def search1(self, x, y, dx, dy, word):
        for i in range(len(word)):
            if self.grid[x + i * dx, y + i * dy] != word[i]:
                return False
        return True

    def part1(self):
        word = "XMAS"
        count = 0
        directions = [
            (0, 1), (1, 0), (1, 1), (1, -1),
            (0, -1), (-1, 0), (-1, -1), (-1, 1)
        ]

        for r in self.rows:
            for c in self.cols:
                for dx, dy in directions:
                    if self.search1(r, c, dx, dy, word):
                        count += 1

        return count

    def search2(self, x, y, da, db, word):
        if not self.search1(x - da, y - da, da, da, word):
            return False
        if not self.search1(x + db, y - db, -db, db, word):
            return False
        return True

    def part2(self):
        word = "MAS"
        count = 0
        directions = [
            (1, 1), (1, -1), (-1, -1), (-1, 1)
        ]

        for r in self.rows:
            for c in self.cols:
                if self.grid[r, c] != 'A':
                    continue
                for dx, dy in directions:
                    if self.search2(r, c, dx, dy, word):
                        count += 1
                        break

        return count


if __name__ == '__main__':
    Day04().main(example=False)
