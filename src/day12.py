#!/bin/env python3
from utils import Day
import numpy as np
from queue import Queue

neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Day12(Day):
    def __init__(self):
        super().__init__("12")

    def parse(self, input_data):
        self.field = np.array([list(line.strip()) for line in input_data.splitlines()])
        self.field = np.pad(self.field, 1, constant_values='.')

    def part1(self):
        unique_fields = list(set(np.unique(self.field)) - {'.'})
        total = 0
        self.part1_borders = []
        for f in unique_fields:
            to_visit = set([tuple(t) for t in np.argwhere(self.field == f)])
            while to_visit:
                q = Queue()
                first = list(to_visit)[0]
                visited = set()
                border = set()
                visited.add(first)
                q.put(first)
                while not q.empty():
                    pos = q.get()
                    for n in neighbors:
                        new_pos = tuple((a + b for a, b in zip(pos, n)))
                        if new_pos in visited:
                            continue
                        if self.field[new_pos] == f:
                            visited.add(new_pos)
                            q.put(new_pos)
                        else:
                            # 1/4 so that we can distinguish between AB and BA borders
                            # not important for part1 but it is for part2
                            border.add(tuple((a + b/4 for a, b in zip(pos, n))))
                total += len(visited) * len(border)
                self.part1_borders.append((len(visited), border))
                to_visit -= visited

        return total

    def part2(self):
        total = 0

        for N, border in self.part1_borders:
            border_sides = 0
            while border:
                q2 = Queue()
                q2.put(border.pop())
                while not q2.empty():
                    pos = q2.get()
                    if pos[0] % 1 == 0:
                        neighbors2 = [(1, 0), (-1, 0)]
                    else:
                        neighbors2 = [(0, 1), (0, -1)]
                    for n2 in neighbors2:
                        new_pos2 = tuple((a + b for a, b in zip(pos, n2)))
                        if new_pos2 in border:
                            border.remove(new_pos2)
                            q2.put(new_pos2)
                border_sides += 1

            total += N * border_sides

        return total


if __name__ == '__main__':
    Day12().main(example=False)
