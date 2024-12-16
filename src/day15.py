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
        grid = self.grid.copy()
        for movement in self.movements:
            direction = directions[movement]
            next_pos = pos + direction
            box_moved = False
            while grid[next_pos] == 'O':
                box_moved = True
                next_pos += direction
            if grid[next_pos] == '#':
                continue
            if box_moved:
                grid[next_pos], grid[pos + direction] = grid[pos + direction], grid[next_pos]
            pos = pos + direction
        return sum(box[0] * 100 + box[1] for box in np.argwhere(grid == 'O'))

    def show(self, grid, pos, pos2=None):
        grid2 = grid.copy()
        grid2[pos] = '@'
        if pos2:
            grid2[pos2] = 'W'
        print('\n'.join([''.join(line) for line in grid2]))

    def pushable(self, grid, pos, direction):
        if grid[pos] == '#':
            return False
        if grid[pos] == '.':
            return True
        if direction[0] == 0:
            return self.pushable(grid, pos + direction + direction, direction)
        else:
            if grid[pos] == '[':
                other_pos = pos + Pos((0, 1))
            elif grid[pos] == ']':
                other_pos = pos + Pos((0, -1))
            else:
                return True
            return self.pushable(grid, pos + direction, direction) and self.pushable(grid, other_pos + direction, direction)

    def push(self, grid, pos, direction):
        if grid[pos] == '#':
            return False
        if grid[pos] == '.':
            return True
        if direction[0] == 0:
            # self.show(grid, pos)
            self.push(grid, pos + direction + direction, direction)
            grid[pos], grid[pos + direction], grid[pos + direction + direction] = grid[pos + direction + direction], grid[pos], grid[pos + direction]
        else:
            if grid[pos] == '[':
                other_pos = pos + Pos((0, 1))
            elif grid[pos] == ']':
                other_pos = pos + Pos((0, -1))
            else:
                return True
            self.push(grid, pos + direction, direction)
            self.push(grid, other_pos + direction, direction)
            grid[pos], grid[pos + direction] = grid[pos + direction], grid[pos]
            grid[other_pos], grid[other_pos + direction] = grid[other_pos + direction], grid[other_pos]
            # self.show(grid, pos)

    def part2(self):
        duplicator = {
            '#': '##',
            'O': '[]',
            '.': '..',
        }
        grid = np.array([list(''.join([duplicator[c] for c in line])) for line in self.grid])
        pos = Pos((self.initial_position[0], self.initial_position[1] * 2))
        # print('Initial state:')
        # self.show(grid, pos)
        for movement in self.movements:
            direction = directions[movement]
            # print(f'\nMovement {movement}:')
            pusheable = self.pushable(grid, pos + direction, direction)
            if pusheable:
                self.push(grid, pos + direction, direction)
                pos += direction
            # self.show(grid, pos)
        return sum(box[0] * 100 + box[1] for box in np.argwhere(grid == '['))


if __name__ == '__main__':
    Day15().main(example=True)
